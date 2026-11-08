import time
import requests
import concurrent.futures

# 1. FIXED: Pointing to our stable, unblocked port 5001
URL = "http://localhost:5001/input"

def send_packet():
    try:
        response = requests.get(URL, timeout=1)
        if response.status_code == 200:
            print("🚀 Packet secured successfully (200)")
        else:
            print(f"⚠️ Warning: Telemetry anomaly detected ({response.status_code})")
    except requests.exceptions.RequestException:
        print("🚨 CRITICAL: Connection dropped. System overloaded!")

def flood_system():
    print("⚡ COMMENCING SIMULATED TRAFFIC ATTACK... Hold onto your seat.")
    # Sends batches of 20 rapid requests continuously
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        while True:
            futures = [executor.submit(send_packet) for _ in range(20)]
            concurrent.futures.wait(futures)
            # 2. FIXED: Pausing for 1 full second to let the metrics engine catch its breath
            time.sleep(1.0) # Tiny pause between waves

if __name__ == '__main__':
    flood_system()
