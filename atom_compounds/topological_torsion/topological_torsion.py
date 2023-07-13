import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw

def smiles_to_fingerprint(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    fingerprint = AllChem.GetHashedTopologicalTorsionFingerprintAsBitVect(molecule)
    fingerprint = np.array(fingerprint)
    return fingerprint

file = open(file='/home/Robbie/Desktop/Drug_Design_Project/' +\
            'Drug_Design_Project/atom_compounds/' +\
            'compound_ex.txt')

file2=open('/home/Robbie/Desktop/Drug_Design_Project/' +\
            'Drug_Design_Project/atom_compounds/' +\
            'topological_torsion/' +\
            'topological_torsion_output.txt', 'w')

file2.close()

file2=open('/home/Robbie/Desktop/Drug_Design_Project/' +\
            'Drug_Design_Project/atom_compounds/' +\
            'topological_torsion/' +\
            'topological_torsion_output.txt', 'a')

for i in file:
    print(i)
    # a = Draw.MolToImage(Chem.MolFromSmiles(str(i)))
    # a.show()
    fingerprint = smiles_to_fingerprint(i)
    print(fingerprint, '\n', file=file2)

file.close()
file2.close()
    