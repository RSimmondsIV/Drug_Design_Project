import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv("/home/Robbie/Desktop/Drug_Design_Project/Data_Files/PubChem_with_toxicity.csv")

# print(df)
df = df.dropna()
numeric = df.select_dtypes(include='number').columns
df = df[numeric]
# print(df)

y = df["mouse_intraperitoneal_LD50"]
X = df.drop(
    "mouse_intraperitoneal_LD50", axis=1)
# print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# print(X_train)
# print(y_train)

lr = LinearRegression()
lr.fit(X=X_train, y=y_train)

y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)

# print(y_lr_train_pred, y_lr_test_pred)

from sklearn.metrics import mean_squared_error, r2_score

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

# print(lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2)
data = {
    'Model': ['Linear Regression'],
    'Train MSE': [lr_train_mse],
    'Train R2': [lr_train_r2],
    'Test MSE': [lr_test_mse],
    'Test R2': [lr_test_r2]
}

lr_results = pd.DataFrame(data).transpose()

print (lr_results)
