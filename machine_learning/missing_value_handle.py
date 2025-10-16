import pandas as pd

# 初始化数据（用None表示空值，不依赖numpy）
data = {
    'ID': ['00001000', '00002000', '00003000', '00004000', None, '00006000', '00007000', '00008000', '00009000'],
    'ST_NUM': [104, 197, None, 201, 203, 207, 'NA', 213, 215],
    'ST_NAME': ['PUTNAM', 'LEXINGTON', 'LEXINGTON', 'BERKELEY', 'BERKELEY', 'BERKELEY', 'WASHINGTON', 'TREMONT',
                'TREMONT'],
    'OWN_OCCUPIED': ['Y', 'N', 'N', 12, 'Y', 'Y', None, 'Y', 'Y'],
    'NUM_BEDROOMS': [3, 3, 'n/a', 1, 3, 'NA', 2, 1, 'na'],
    'NUM_BATH': [1, 1.5, 1, None, 2, 1, 'HURLEY', 1, 2],
    'SQ_FT': [1000, None, 850, 700, 1600, 800, 950, None, 1800]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 显示数据框
print(df)

# 查看缺失情况
print(df.isnull().sum())
print(df.info())

# 0. 空值的识别与处理
missing_values = ['n/a', 'NA', 'na', '<NA>']
print(df.replace(missing_values, None))
print(df.replace(missing_values, pd.NA))

df = df.replace(missing_values, pd.NA)
print(df.isnull().sum())

# 1. 删除缺失值
df_drop = df.dropna()
print(df_drop)

# 2. 填充缺失值
df_fill = df.fillna(
    {
        'NUM_BEDROOMS': df['NUM_BEDROOMS'].mean()
    }
)
print(df_fill)

x = df['NUM_BEDROOMS'].mean()
df["NUM_BEDROOMS"].fillna(x, inplace = True)
print(df)