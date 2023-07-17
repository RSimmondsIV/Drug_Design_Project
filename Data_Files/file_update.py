import pandas as pd 

df = pd.read_csv('PubChem_compound_list.csv')
print(df)

df = df.drop(
    ["cmpdsynonym", 
    "mf", 
    "inchikey",
    "iupacname",
    "neighbortype",
    "meshheadings",
    "annothits",
    "aids",
    "cidcdate",
    "sidsrcname",
    "depcatg",
    "annotation"],
    axis=1)

df_2 = pd.read_csv("Acute_Toxicity_mouse_LD50.csv")

df_2 = df_2.drop(
    ["TAID",
    "IUPAC Name",
    "SMILES",
    "Canonical SMILES",
    "InChIKey"
    ],
    axis=1)

df_2 = df_2.rename(columns={'Pubchem CID': 'cid'})

print(df)
print(df_2)

merged_df = pd.merge(df, df_2, on='cid', how='left')


merged_df.to_csv('PubChem_with_toxicity.csv')