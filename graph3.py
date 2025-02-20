import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取CSV文件
df = pd.read_csv('sleep_pattern_with_first_pickup.csv')

# 将日期列转换为datetime类型
df['date'] = pd.to_datetime(df['date'])

# 将时间列转换为datetime.time类型
df['this_morning'] = pd.to_datetime(df['this_morning']).dt.time
df['first_pick_up'] = pd.to_datetime(df['first_pick_up']).dt.time

# 将时间转换为分钟数，便于绘图
df['this_morning_min'] = df['this_morning'].apply(lambda x: x.hour * 60 + x.minute)
df['first_pick_up_min'] = df['first_pick_up'].apply(lambda x: x.hour * 60 + x.minute)

# 创建图形
plt.figure(figsize=(12, 6))

# 绘制this_morning折线
plt.plot(df['date'], df['this_morning_min'], marker='o', linestyle='-', color='b', label='First Morning Browse')

# 绘制first_pick_up折线
plt.plot(df['date'], df['first_pick_up_min'], marker='s', linestyle='--', color='r', label='First Pick Up')

# 设置标题和标签
plt.title('Date vs This Morning & First Pick Up', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Time (HH:MM)', fontsize=12)

# 设置纵轴刻度为4:00到13:00，30分钟间隔
morning_ticks = [4 * 60, 4 * 60 + 30, 5 * 60, 5 * 60 + 30, 6 * 60, 6 * 60 + 30,
                 7 * 60, 7 * 60 + 30, 8 * 60, 8 * 60 + 30, 9 * 60, 9 * 60 + 30,
                 10 * 60, 10 * 60 + 30, 11 * 60, 11 * 60 + 30, 12 * 60, 12 * 60 + 30,
                 13 * 60]
plt.yticks(morning_ticks, ['04:00', '04:30', '05:00', '05:30', '06:00', '06:30',
                           '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
                           '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
                           '13:00'])

# 设置纵轴范围
plt.ylim(4 * 60, 13 * 60 + 30)

# 格式化日期横轴
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=45, ha='right')

# 添加图例
plt.legend(loc='upper left', fontsize=12)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()

# 保存图形
plt.savefig('this_morning_first_pick_up_plot.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()