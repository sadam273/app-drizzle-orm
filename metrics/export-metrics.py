import requests
import csv
from datetime import datetime

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
    # Ganti start & end sesuai waktu pas k6 running
    with open("test_time.txt") as f:
        lines = f.readlines()
        start = lines[0].split("=")[1].strip()
        end   = lines[1].split("=")[1].strip()
        
    results = query_range(metric_query, start, end)
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", label])
        for result in results:
            for timestamp, value in result["values"]:
                dt = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([dt, value])
    print(f"Saved: {filename}")

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