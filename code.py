import pandas as pd
df = pd.read_csv('titanic.csv')

print("\nВсего пассажиров:", len(df))

print("\nСтрок с пустым возрастом:", df['Age'].isna().sum())

print("\nСтатистика (числа):\n", df.describe())

print("\nСтатистика (категории):\n", df.describe(include=['object']))

print("\nМужчин:", (df['Sex'] == 'male').sum())

print("\nКают 1 класса:", (df['Pclass'] == 1).sum())

print("\nВыживших:", df['Survived'].sum())
print("Процент выживших:", round(df['Survived'].mean() * 100, 2))

print("\nВыживаемость женщин:", round(df[df['Sex'] == 'female']['Survived'].mean() * 100, 2))
print("Выживаемость мужчин:", round(df[df['Sex'] == 'male']['Survived'].mean() * 100, 2))

print("\nСредняя цена билета 1 класса:", df[df['Pclass'] == 1]['Fare'].mean())

print("\nВыживаемость 3 класса:", df[df['Pclass'] == 3]['Survived'].mean())

median_age = df['Age'].median()
print("\nМедианный возраст:", median_age)
df['Age'] = df['Age'].fillna(median_age)

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print("FamilySize у 888 пассажира:", df.iloc[888]['FamilySize'])

print("\nСредний возраст:\n", round(df.groupby('Survived')['Age'].mean(), 2))

print("\nЖенщины 1 класса выжившие:", len(df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & (df['Survived'] == 1)]))

print("\nМоложе 18 без шнурков:", len(df[(df['Age'] < 18) & (df['Parch'] == 0)]))