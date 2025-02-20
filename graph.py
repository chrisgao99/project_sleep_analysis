import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取CSV文件
df = pd.read_csv('sleep_pattern_with_first_pickup.csv')

# 将日期列转换为datetime类型
df['date'] = pd.to_datetime(df['date'])

# 将时间列转换为datetime.time类型
df['last_night'] = pd.to_datetime(df['last_night']).dt.time
df['this_morning'] = pd.to_datetime(df['this_morning']).dt.time

# 将last_night时间转换为分钟数，处理跨午夜的情况
def convert_time_to_minutes(time):
    if time.hour < 12:  # 假设1:00是凌晨1点
        return (time.hour + 24) * 60 + time.minute  # 跨午夜的时间加上24小时
    else:
        return time.hour * 60 + time.minute

df['last_night_min'] = df['last_night'].apply(convert_time_to_minutes)

# 将this_morning时间转换为分钟数
df['this_morning_min'] = df['this_morning'].apply(lambda x: x.hour * 60 + x.minute)

# 创建第一张图：Date vs Last Night
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['last_night_min'], marker='o', linestyle='-', color='b',label='Last Night Browse')
plt.title('Date vs Last Night', fontsize=14)
plt.ylabel('Time (HH:MM)', fontsize=12)
plt.grid(True)

# 设置last_night纵轴刻度为22:00到1:00，30分钟间隔
last_night_ticks = [22 * 60, 22 * 60 + 30, 23 * 60, 23 * 60 + 30, 24 * 60, 24 * 60 + 30, 25 * 60]
plt.yticks(last_night_ticks, ['22:00', '22:30', '23:00', '23:30', '00:00', '00:30', '01:00'])

# 设置纵轴范围
plt.ylim(22 * 60, 25 * 60 + 30)

# 格式化日期横轴
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=45, ha='right')

# 调整布局
plt.tight_layout()

# 保存第一张图
plt.savefig('last_night_plot.png', dpi=300, bbox_inches='tight')

# 显示第一张图
plt.show()

# 创建第二张图：Date vs This Morning
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['this_morning_min'], marker='o', linestyle='-', color='r',label='Last Night browse')
plt.title('Date vs This Morning', fontsize=14)
plt.ylabel('Time (HH:MM)', fontsize=12)
plt.grid(True)

# 设置this_morning纵轴刻度为4:00到13:00，30分钟间隔
this_morning_ticks = [4 * 60, 4 * 60 + 30, 5 * 60, 5 * 60 + 30, 6 * 60, 6 * 60 + 30,
                      7 * 60, 7 * 60 + 30, 8 * 60, 8 * 60 + 30, 9 * 60, 9 * 60 + 30,
                      10 * 60, 10 * 60 + 30, 11 * 60, 11 * 60 + 30, 12 * 60, 12 * 60 + 30,
                      13 * 60]
plt.yticks(this_morning_ticks, ['04:00', '04:30', '05:00', '05:30', '06:00', '06:30',
                                '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
                                '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                                '13:00'])

# 设置纵轴范围
plt.ylim(4 * 60, 13 * 60 + 30)

# 格式化日期横轴
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=45, ha='right')

# 调整布局
plt.tight_layout()

# 保存第二张图
plt.savefig('this_morning_plot.png', dpi=300, bbox_inches='tight')

# 显示第二张图
plt.show()