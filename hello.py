import time
from datetime import datetime

def show_time():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Şu anki saat: {current_time}")
        time.sleep(10)  # Her 10 saniyede bir saati göster

if __name__ == "__main__":
    show_time()