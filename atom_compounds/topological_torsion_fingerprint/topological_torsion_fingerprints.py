import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import sys

def smiles_to_fingerprint(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    fingerprint = AllChem.GetHashedTopologicalTorsionFingerprintAsBitVect(molecule)
    fingerprint = np.array(fingerprint)
    return fingerprint


if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)

    file = open(file='atom_compounds/' +\
            'compound_ex.txt')

    file2=open('atom_compounds/' +\
            'topological_torsion/' +\
            'topological_torsion_output.txt', 'w')

    file2.close()

    file2=open('atom_compounds/' +\
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