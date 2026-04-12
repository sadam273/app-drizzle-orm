import subprocess
import datetime
import time
import os
import csv

base_dir = os.path.dirname(os.path.abspath(__file__))
k6_script_path = os.path.join(base_dir, "..", "k6", "read.js")
csv_output_path = os.path.join(base_dir, "..", "response_time_result.csv")

start_time = datetime.datetime.utcnow()
print(f"Test started at: {start_time.isoformat()}Z")

# Tambah --out csv di sini
subprocess.run(["k6", "run", "--out", f"csv={csv_output_path}", k6_script_path])

end_time = datetime.datetime.utcnow()
print(f"Test ended at: {end_time.isoformat()}Z")

with open("test_time.txt", "w") as f:
    f.write(f"start={start_time.strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
    f.write(f"end={end_time.strftime('%Y-%m-%dT%H:%M:%SZ')}\n")

print("Waktu disimpan di test_time.txt")