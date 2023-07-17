import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv("/home/Robbie/Desktop/Drug_Design_Project/Data_Files/PubChem_with_toxicity.csv")

print(df)
df = df.dropna()
numeric = df.select_dtypes(include='number').columns
df = df[numeric]
print(df)

Y = df["mouse_intraperitoneal_LD50"]
X = df.drop(
    "mouse_intraperitoneal_LD50", axis=1)
print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=100)

print(X_train)
print(Y_train)

lr = LinearRegression()
lr.fit(X=X_train, y=Y_train)