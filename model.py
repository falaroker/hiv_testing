import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("C:/Users/IT OFFICE/Desktop/testing.csv")
df['SEX_NUM'] = df['SEX'].map({'M': 1, 'F': 0})
df['OUTCOME'] = LabelEncoder().fit_transform(df['HIV_Test_Results_Use_codes_below'])

X = df[['AGE', 'SEX_NUM']]
y = df['OUTCOME']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
