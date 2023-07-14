# From CHATGPT-4
import numpy as np
import sys
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import rdFingerprintGenerator

def smiles_to_fingerprint(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    fp_generator = rdFingerprintGenerator.GetAtomPairGenerator()
    fingerprint = fp_generator.GetFingerprint(molecule)
    np_array = fingerprint.ToBitString()
    return np_array


    
if __name__ == "__main__":
    np.set_printoptions(threshold=sys.maxsize)

    file = open(file='atom_compounds/' +\
            'compound_ex.txt')

    file2=open('atom_compounds/' +\
            'atom_pair_fingerprint/' +\
            'atom_pair_fingerprint_output.txt', 'w')

    file2.close()

    file2=open('atom_compounds/' +\
            'atom_pair_fingerprint/' +\
            'atom_pair_fingerprint_output.txt', 'a')

    for i in file:
        print(i)
        # a = Draw.MolToImage(Chem.MolFromSmiles(str(i)))
        # a.show()
        fingerprint = smiles_to_fingerprint(i)
        print(fingerprint, '\n', file=file2)

    file.close()
    file2.close()   