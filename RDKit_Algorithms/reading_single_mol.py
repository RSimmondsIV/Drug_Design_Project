from rdkit import Chem
from rdkit.Chem import Draw

# Makes a Molecule from SMILES notation
m = Chem.MolFromSmiles('Cc1ccccc1')
print(type(m))
img = Draw.MolToImage(m)
img.show()