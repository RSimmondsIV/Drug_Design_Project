import numpy as np
import sys
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import rdFingerprintGenerator
from rdkit.Chem import MACCSkeys
np.set_printoptions(threshold=sys.maxsize)

def smiles_to_fingerprint(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    fingerprint = MACCSkeys.GenMACCSKeys(molecule)
    np_array = fingerprint.ToBitString()
    return np_array

file = open(file='atom_compounds/' +\
            'compound_ex.txt')

file2=open('atom_compounds/' +\
            'MACCS_keys_fingerprint/' +\
            'MACCS_keys_fingerprint_output.txt', 'w')

file2.close()

file2=open('atom_compounds/' +\
            'MACCS_keys_fingerprint/' +\
            'MACCS_keys_fingerprint_output.txt', 'a')

for i in file:
    print(i)
    # a = Draw.MolToImage(Chem.MolFromSmiles(str(i)))
    # a.show()
    fingerprint = smiles_to_fingerprint(i)
    print(fingerprint, '\n', file=file2)

file.close()
file2.close()
    