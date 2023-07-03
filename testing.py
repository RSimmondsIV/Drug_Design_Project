from rdkit import Chem

m = Chem.MolFromSmiles('Cc1ccccc1')

from rdkit.Chem import Draw

img = Draw.MolToImage(m)