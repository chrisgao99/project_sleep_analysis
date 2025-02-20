import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取CSV文件
df = pd.read_csv('sleep_pattern_with_first_pickup.csv')

# 将日期列转换为datetime类型
df['date'] = pd.to_datetime(df['date'])

# 计算平均时长
average_sleep_time = df['estimated_sleep_time'].mean()

# 创建图形
plt.figure(figsize=(12, 6))

# 绘制柱状图
plt.bar(df['date'], df['estimated_sleep_time'], color='skyblue', width=0.8, label='Estimated Sleep Time')

# 绘制平均时长虚线
plt.axhline(average_sleep_time, color='red', linestyle='--', linewidth=2, label=f'Average: {average_sleep_time:.2f} hours')

# 设置标题和标签
plt.title('Date vs Estimated Sleep Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Estimated Sleep Time (hours)', fontsize=12)

# 格式化日期横轴
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=45, ha='right')

# 设置纵轴范围（根据数据动态调整）
max_sleep_time = df['estimated_sleep_time'].max()
plt.ylim(0, max_sleep_time + 1)  # 纵轴范围从0到最大值+1

# 添加网格
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加图例
plt.legend(loc='upper right', fontsize=12)

# 调整布局
plt.tight_layout()

# 保存图形
plt.savefig('date_vs_estimated_sleep_time_with_average.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()