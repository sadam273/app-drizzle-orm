import pandas as pd

df = pd.read_csv('../response_time_result.csv')

# ambil hanya response time per request
duration = df[df['metric_name'] == 'http_req_duration'][['timestamp', 'metric_value']]
duration.columns = ['timestamp', 'response_time_ms']

duration.to_csv('response_time_clean.csv', index=False)
print(duration.describe())