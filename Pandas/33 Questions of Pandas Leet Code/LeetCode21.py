
import pandas as pd

data = [
    {"emp_id": 1, "event_day": "2020-11-28", "in_time": 4, "out_time": 32},
    {"emp_id": 1, "event_day": "2020-11-28", "in_time": 55, "out_time": 200},
    {"emp_id": 1, "event_day": "2020-12-03", "in_time": 1, "out_time": 42},
    {"emp_id": 2, "event_day": "2020-11-28", "in_time": 3, "out_time": 33},
    {"emp_id": 2, "event_day": "2020-12-09", "in_time": 47, "out_time": 74}
]

df = pd.DataFrame(data)
df1=df.groupby(["emp_id","event_day"])[['in_time','out_time']].sum()
df1['total_time'] = df1['out_time'] - df1['in_time']

print(df1)
