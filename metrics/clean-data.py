import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_input_path = os.path.join(base_dir, "..", "response_time_result.csv")
csv_output_path = os.path.join(base_dir, "..", "response_time_clean.csv")

df = pd.read_csv(csv_input_path)

duration = df[df['metric_name'] == 'http_req_duration'][['timestamp', 'metric_value']]
duration.columns = ['timestamp', 'response_time_ms']

duration.to_csv(csv_output_path, index=False)
print(duration.describe())