import time
from datetime import datetime

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Şu anki saat: {current_time}")    
    time.sleep(60)

    