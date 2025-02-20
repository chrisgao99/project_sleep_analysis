import pandas as pd
from datetime import datetime, timedelta

# 读取 CSV 文件
df = pd.read_csv("sleep_pattern_with_first_pickup.csv")

def calculate_sleep_time(row):
    date = datetime.strptime(row['date'], "%Y-%m-%d")
    last_night_time = datetime.strptime(row['last_night'], "%H:%M:%S").time()
    this_morning_time = datetime.strptime(row['this_morning'], "%H:%M:%S").time()
    
    this_morning = datetime.combine(date, this_morning_time)
    last_night = datetime.combine(date, last_night_time)
    
    if last_night_time.hour >= 12:  # 如果 last_night 不是 0 点多
        sleep_duration = ((this_morning + timedelta(days=1)) - last_night).total_seconds() / 3600
    else:  # 如果 last_night 是 0 点多
        sleep_duration = (this_morning - last_night).total_seconds() / 3600
    
    return sleep_duration

# 计算 estimated_sleep_time
import pandas as pd
from datetime import datetime, timedelta

# 读取 CSV 文件
df = pd.read_csv("sleep_pattern_with_first_pickup.csv")

def calculate_sleep_time(row):
    date = datetime.strptime(row['date'], "%Y-%m-%d")
    last_night_time = datetime.strptime(row['last_night'], "%H:%M:%S").time()
    this_morning_time = datetime.strptime(row['this_morning'], "%H:%M:%S").time()
    
    this_morning = datetime.combine(date, this_morning_time)
    last_night = datetime.combine(date, last_night_time)
    
    if last_night_time.hour >= 12:  # 如果 last_night 不是 0 点多
        sleep_duration = ((this_morning + timedelta(days=1)) - last_night).total_seconds() / 3600
    else:  # 如果 last_night 是 0 点多
        sleep_duration = (this_morning - last_night).total_seconds() / 3600
    
    return round(sleep_duration, 1)  # 四舍五入到 0.1 小时

# 计算 estimated_sleep_time
df['estimated_sleep_time'] = df.apply(calculate_sleep_time, axis=1)

# 将结果写入原 CSV 文件
df.to_csv("sleep_pattern_with_first_pickup.csv", index=False)

# 输出结果
print("计算完成，结果已写入 sleep_pattern_with_first_pickup.csv")

# 将结果写入原 CSV 文件
df.to_csv("sleep_pattern_with_first_pickup.csv", index=False)

# 输出结果
print("results written to sleep_pattern_with_first_pickup.csv")