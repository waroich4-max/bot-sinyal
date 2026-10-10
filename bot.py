import requests
from bs4 import BeautifulSoup

TOKEN = "8395690959:AAERNZNTgaGULV7D2m3R8R0_al9DI621FU4"
CHAT_ID = "8770086104"

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
            print("Berhasil terhubung ke tradingpoin.com...")
            
            # Anda bisa menyesuaikan bagian ini untuk mengambil elemen harga/sinyal tertentu dari HTML web
            # Untuk sekarang, bot akan mengirimkan laporan status pengecekan pasar aktif
            msg = "🚀 <b>Bot Sinyal CRYIDX.B</b>\nStatus: Berhasil memantau pasar TradingPoin!"
            send_telegram(msg)
        else:
            print(f"Gagal akses web: {response.status_code}")
    except Exception as e:
        print(f"Error scraping: {e}")

if __name__ == "__main__":
    check_signal()
