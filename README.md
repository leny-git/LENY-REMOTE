<div align="center">

# LENY-REMOTE v1.0
**Operator: LENY // Architecture: Telegram C2**

[![Python](https://img.shields.io/badge/PYTHON-3.X-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/PLATFORM-UBUNTU%20%7C%20LINUX%20%7C%20WINDOWS-green.svg)]()
[![Security](https://img.shields.io/badge/SECURITY-ENCRYPTED-red.svg)]()

*Telegram tabanlı, arka planda hayalet modunda çalışan, tamamen özelleştirilebilir gelişmiş uzak yönetim ve operasyon framework'ü.*

</div>

---

## 🧐 Bu Kod Ne İşe Yarar?
**LENY-REMOTE**, hedef sistem üzerinde tamamen sessiz ve arka planda çalışarak, Telegram botu üzerinden uzaktan tam kontrol sağlamak için geliştirilmiş gelişmiş bir Python betiğidir (`leny-remote.py`). Sabit diske hiçbir kalıntı ve iz bırakmadan RAM üzerinden anlık ekran görüntüsü alabilir, hedef sistemde terminal komutları çalıştırabilir ve sistem yönetimi sağlayabilir.

---

## 🚀 Özellikler & Operasyon Modülleri

* **[1] Hayalet Çalışma Modu (Stealth Execution):** Windows'ta konsol penceresini tamamen gizler (`pythonw`), Linux/Ubuntu'da arka planda sessizce çalışır.
* **[2] Telegram C2 Entegrasyonu:** İnteraktif komut seti ve sadece senin Telegram `User ID`'ni tanıyan güvenlik duvarı sayesinde dışarıdan gelebilecek yetkisiz müdahalelere karşı tam korumalıdır.
* **[3] RAM Üzerinden Ekran Görüntüsü:** Diske hiçbir şey yazmadan anlık ekran görüntüsünü doğrudan RAM'e çeker ve Telegram sunucularına iletir.
* **[4] Uzaktan Terminal Komuta:** Hedef sistemde komutları yürütüp çıktısını anında mesaj olarak geri döndürür.
* **[5] Sistem Yönetimi:** Oturumu anında kilitleme ve temel sistem verilerini raporlama.

---

## ⚙️ Gereksinimler & Kütüphaneler
Projenin sorunsuz çalışması için gereken Python kütüphaneleri:
* `requests`
* `pyautogui`

---

## 🛠️ Kurulum Rehberi

### 🐧 Ubuntu / Linux Kurulumu
1. Projeyi klonlayın ve dizine girin:
   ```bash
   git clone https://github.com/leny-git/LENY-REMOTE.git
   cd LENY-REMOTE
   ```
2. Gerekli paketleri yükleyin:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-pil python3-pyautogui -y
   ```
3. Python bağımlılıklarını kurون:
   ```bash
   pip3 install requests pyautogui
   ```
4. `leny-remote.py` dosyasındaki `TOKEN` ve `AUTHORIZED_USER_ID` alanlarını kendi Telegram bilgilerinizle düzenleyin.
5. Arka planda çalıştırmak için:
   ```bash
   python3 leny-remote.py &
   ```

### 🪟 Windows Kurulumu
1. Proje klasöründe terminali açın ve bağımlılıkları yükleyin:
   ```cmd
   pip install requests pyautogui
   ```
2. `leny-remote.py` dosyasındaki bot tokeninizi ve kullanıcı ID'nizi koda işleyin.
3. Siyah CMD penceresi hiç açılmadan hayalet modda başlatmak için:
   ```cmd
   pythonw leny-remote.py
   ```

---

## 👤 Geliştirici & Kim Yapmıştır?
* **Operator / Developer:** `LENY`
* **GitHub Repository:** [leny-git/LENY-REMOTE](https://github.com/leny-git/LENY-REMOTE)
