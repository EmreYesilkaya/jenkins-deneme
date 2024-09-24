import time
from datetime import datetime
i = 1
while 2 > i:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Şu anki saat: {current_time}")    
    time.sleep(60)

    i = i + 1

    