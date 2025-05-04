# Screen‑Watcher Alert

Bu araç, ikinci (sol) 1080p monitörde belirli bir görseli (ör. “Converting…”
rozeti) arar. Görsel kaybolduğunda uyarı WAV dosyasını 30 kez çalar ve çıkar.

## Gereksinimler

* **Windows 10/11 (64‑bit)**
* **Python 3.9 veya üzeri**  
  – 64‑bit sürüm önerilir.

## Hızlı Kurulum

```cmd
git clone https://github.com/<kullanıcı>/screen-watcher.git
cd screen-watcher

:: Sanal ortam (önerilir)
python -m venv venv
call venv\Scripts\activate

:: Bağımlılıkları kur
python -m pip install --upgrade pip
python -m pip install -r requirements.txt


## Çalıştırma
python screen_watcher.py
