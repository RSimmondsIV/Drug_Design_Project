from rdkit import Chem
from rdkit.Chem import Draw

compounds = []
file = open(file='atom_compounds/' +\
    'compound_list.txt')


for i in file:
    compounds.append(i)

for i in compounds:
    print(i)
    a = Draw.MolToImage(Chem.MolFromSmiles(str(i)))
    print(type(a))
    a.show()