
import matplotlib.pyplot as plt
import seaborn as sns

# Boxplot
for col in num_cols:
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()

# Remove outliers using IQR
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Age'] >= Q1 - 1.5 * IQR) &
        (df['Age'] <= Q3 + 1.5 * IQR)]



print(df.head())
print(df.shape)

'''
OUTPUT:
"C:\Program Files\Python311\python.exe" C:\madhu\PycharmProjects\pythonProject\__pycache__\Task1\DCP.py 
   PassengerId  Survived  Pclass  ... Sex_male  Embarked_Q  Embarked_S
0            1         0       3  ...     True       False        True
1            2         1       1  ...    False       False       False
2            3         1       3  ...    False       False        True
3            4         1       1  ...    False       False        True
4            5         0       3  ...     True       False        True

[5 rows x 13 columns]
(825, 13)

Process finished with exit code 0

'''
