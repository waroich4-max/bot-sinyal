!pip install requests beautifulsoup4

import time
import requests
from bs4 import BeautifulSoup

# --- MASUKKAN DATA ANDA DI SINI ---
TOKEN_BOT = "8395690959:AAERNZNTgaGULV7D2m3R8RO_al9DI621FU4"      
CHAT_ID = "8770086104"          

URL_TARGET = "https://tradingpoin.com/id/chart?pair=CRYIDX.B&val=Z-CRY%252FIDX&source=Binomo&description=CRYPTO+%2F+IDX&timeframe=60"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN_BOT}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Gagal mengirim pesan: {e}")

print("Bot pemantau sinyal sedang berjalan...")
send_telegram("🤖 *Bot Pemantau Sinyal Tradingpoin Diaktifkan!*")

last_signal = ""

while True:
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL_TARGET, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = soup.get_text()

            # Cek jika ada sinyal NAIK
            if "NAIK" in text_content and last_signal != "NAIK":
                msg = "📢 *SINYAL CRYPTO / IDX*\n\n🟢 **Arah:** NAIK (BUY)\n⏳ **Eksekusi:** 1-2 detik sebelum pergantian candle"
                send_telegram(msg)
                last_signal = "NAIK"
                print("Sinyal NAIK terdeteksi dan dikirim!")
                
            # Cek jika ada sinyal TURUN
            elif "TURUN" in text_content and last_signal != "TURUN":
                msg = "📢 *SINYAL CRYPTO / IDX*\n\n🔴 **Arah:** TURUN (SELL)\n⏳ **Eksekusi:** 1-2 detik sebelum pergantian candle"
                send_telegram(msg)
                last_signal = "TURUN"
                print("Sinyal TURUN terdeteksi dan dikirim!")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        
    # Cek setiap 10 detik
    time.sleep(10)
