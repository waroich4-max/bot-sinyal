import requests
from bs4 import BeautifulSoup

TOKEN = "8395690959:AAERNZNTgaGULV7D2m3R8R0_al9DI621FU4"

CHAT_ID = "8770086104"

def check_signal():
    url = "https://tradingpoin.com/id/chart?pair=CRYIDX.B&val=Z-CRY%252FIDX&source=Binomo&description=CRYPTO+%2F+IDX&timeframe=60"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            msg = "🚀 Bot Sinyal CRYIDX.B Berhasil Mengecek Pasar!"
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
            print("Pesan terkirim ke Telegram!")
        else:
            print(f"Gagal web: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_signal()