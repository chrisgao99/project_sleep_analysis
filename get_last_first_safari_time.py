import json
import pandas as pd
from datetime import datetime, timedelta

# 读取 JSON 文件
with open("safari_history.json", "r") as file:
    data = json.load(file)

# 解析时间戳并转换为 datetime 对象
for entry in data:
    entry["timestamp"] = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")

# 设定分析时间范围
start_date = datetime(2025, 1, 13).date()  # 转换为 date 类型
end_date = datetime(2025, 2, 13).date()  # 转换为 date 类型

# 存储每天的最晚浏览记录（包括次日凌晨 2 点）和最早浏览记录（2 点之后）
results = {}

# 遍历所有数据，按天分类
for entry in data:
    timestamp = entry["timestamp"]
    date = timestamp.date()

    # 如果时间是凌晨 0-1:59，算作前一天的 "last_night"
    if timestamp.hour < 2:
        date -= timedelta(days=1)

    # 只分析范围内的日期
    if start_date <= date <= end_date:
        if date not in results:
            results[date] = {"last_night": None, "this_morning": None}

        # last_night: 最晚记录（截至凌晨 1:59）
        if timestamp.hour < 2 or timestamp.hour >= 18:
            if results[date]["last_night"] is None or timestamp > results[date]["last_night"]:
                results[date]["last_night"] = timestamp

        # this_morning: 最早记录（从凌晨 2:00 开始）
        elif timestamp.hour >= 2:
            if results[date]["this_morning"] is None or timestamp < results[date]["this_morning"]:
                results[date]["this_morning"] = timestamp

# 转换为 DataFrame 并格式化时间
df = pd.DataFrame([
    {
        "date": date.strftime("%Y-%m-%d"),
        "last_night": results[date]["last_night"].strftime("%H:%M:%S") if results[date]["last_night"] else "",
        "this_morning": results[date]["this_morning"].strftime("%H:%M:%S") if results[date]["this_morning"] else ""
    }
    for date in sorted(results.keys())
])

# 保存到 CSV 文件
csv_filename = "sleep_pattern.csv"
df.to_csv(csv_filename, index=False)

print(f"数据已保存到 {csv_filename}")
