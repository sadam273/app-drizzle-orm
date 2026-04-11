import subprocess
import datetime
import time
import os

# Cari lokasi absolut folder 'metrics' tempat script ini berada, lalu arahkan ke 'k6/read.js'
base_dir = os.path.dirname(os.path.abspath(__file__))
k6_script_path = os.path.join(base_dir, "..", "k6", "read.js")

# Catat waktu start
start_time = datetime.datetime.utcnow()
print(f"Test started at: {start_time.isoformat()}Z")

# Jalankan k6 (sekarang jalurnya sudah anti-nyasar)
subprocess.run(["k6", "run", k6_script_path])

# Catat waktu end
end_time = datetime.datetime.utcnow()
print(f"Test ended at: {end_time.isoformat()}Z")

# Simpan ke file
with open("test_time.txt", "w") as f:
    f.write(f"start={start_time.strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
    f.write(f"end={end_time.strftime('%Y-%m-%dT%H:%M:%SZ')}\n")

print("Waktu disimpan di test_time.txt")