#Normalize / Standardize
# Select numerical columns
num_cols = ['Age', 'Fare', 'SibSp', 'Parch']

for col in num_cols:
    mean = df[col].mean()
    std = df[col].std()
    df[col] = (df[col] - mean) / std
