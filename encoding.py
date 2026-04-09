# Convert categorical → numerical
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
