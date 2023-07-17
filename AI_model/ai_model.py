import pandas as pd 


df = pd.read_csv("/home/Robbie/Desktop/Drug_Design_Project/Data_Files/PubChem_with_toxicity.csv")

print(df)
df = df.dropna()
print(df)

Y = df["mouse_intraperitoneal_LD50"]
X = df.drop("mouse_intraperitoneal_LD50", axis=1)

print(Y)
print(X)