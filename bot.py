import requests
from bs4 import BeautifulSoup

TOKEN = "7953259837:AAFYc8E8s2k1_72n0fO-lB6mN8t3J68iY_Y"
CHAT_ID = "6124806548"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        res = requests.post(url, data=payload, timeout=10)
        print(f"Respon Telegram: {res.status_code}")
    except Exception as e:
        print(f"Error kirim Telegram: {e}")

def check_signal():
    url = "https://tradingpoin.com/id/chart?pair=CRYIDX.B&val=Z-CRY%252FIDX&source=Binomo&description=CRYPTO+%2F+IDX&timeframe=60"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print("Berhasil mengecek sinyal...")
            send_telegram("🚀 <b>Bot Sinyal CRYIDX.B Berhasil Mengecek Pasar!</b>")
        else:
            print(f"Gagal akses web: {response.status_code}")
    except Exception as e:
        print(f"Error scraping: {e}")

if __name__ == "__main__":
    check_signal()
