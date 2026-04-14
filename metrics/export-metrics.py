import requests
import csv
from datetime import datetime, timedelta # <--- TAMBAH timedelta DI SINI

PROMETHEUS_URL = "http://localhost:9090"

def query_range(metric, start, end, step="1s"):
    params = {
        "query": metric,
        "start": start,
        "end": end,
        "step": step
    }
    print("Params:", params)  # tambah ini
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query_range", params=params)
    print("Response:", response.json())
    return response.json()["data"]["result"]


def export_csv(filename, metric_query, label):
    # Baca start & end sesuai waktu pas k6 running
    with open("test_time.txt") as f:
        lines = f.readlines()
        start = lines[0].split("=")[1].strip()
        end   = lines[1].split("=")[1].strip()
        
    results = query_range(metric_query, start, end)
    
    # --- MULAI DARI SINI YANG DIUBAH (LOGIKA PENAMBAL DATA BOLONG) ---
    
    # 1. Konversi teks waktu start dan end menjadi format Waktu Python
    start_dt = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
    end_dt = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ")
    
    # 2. Masukkan data dari Prometheus ke dalam Dictionary (Kamus) biar gampang dicari
    prom_data = {}
    if results:
        for timestamp, value in results[0]["values"]:
            dt_str = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
            prom_data[dt_str] = value
            
    # 3. Tulis CSV dengan looping mutlak SETIAP 1 DETIK
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", label])
        
        current_dt = start_dt
        last_val = 0 # Nilai cadangan kalau detik awal kosong
        
        while current_dt <= end_dt:
            dt_str = current_dt.strftime("%Y-%m-%d %H:%M:%S")
            
            if dt_str in prom_data:
                last_val = prom_data[dt_str] # Update nilai terakhir kalau datanya ada
                writer.writerow([dt_str, last_val])
            else:
                writer.writerow([dt_str, last_val]) # Tulis nilai terakhir kalau datanya bolong
                
            current_dt += timedelta(seconds=1) # Maju 1 detik
            
    print(f"Saved: {filename}")
    # --- AKHIR YANG DIUBAH ---
# CPU Utilization
export_csv(
    "cpu_usage.csv",
    f'rate(container_cpu_usage_seconds_total{{container_label_com_docker_compose_service="app"}}[2s])',
    "cpu_usage"
)

# RAM Usage
export_csv(
    "ram_usage.csv",
    f'container_memory_usage_bytes{{container_label_com_docker_compose_service="app"}}',
    "ram_usage"
)