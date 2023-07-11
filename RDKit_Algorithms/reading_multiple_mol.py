from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.six import StringIO
from rdkit.Chem import AllChem

m = Chem.MolFromSmiles('C1OC1')
print(type(m))
for atom in m.GetAtoms():
    print(atom.GetAtomicNum())

print(m.GetBonds()[0].GetBondType())

print(m.GetAtomWithIdx(0).GetSymbol())
img = Draw.MolToImage(m)
img.show()