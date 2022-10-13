print(1)

# 2.4
# 可视化查看数据的相关统计量
data_describe = df.describe()  # None (default) : The result will include all numeric columns.
columns = data_describe.columns
index = data_describe.index[1:]

plt.figure(figsize=(15, 10))
for i in range(len(columns)):
    ax = plt.subplot(4, 4, i + 1)  # 最多画16个小图
    ax.set_title(columns[i])
# for i in range(len(columns))
