import time
from datetime import datetime

while True:
    # Şu anki zamanı al
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Şu anki saat: {current_time}")
    
    # 60 saniye bekle
    time.sleep(60)