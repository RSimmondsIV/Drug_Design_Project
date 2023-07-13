import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.svm import SVC

def smiles_to_fingerprint(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    fingerprint = AllChem.GetMorganFingerprintAsBitVect(molecule, 2, nBits=1024)
    fingerprint = np.array(fingerprint)
    return fingerprint

# Example SMILES sequences
smiles1 = 'CC(=O)OC1=CC=CC=C1C(=O)O'
smiles2 = 'CC(=O)NCCC1=CN=CN1C'
file = open(file='/home/Robbie/Desktop/Drug_Design_Project/' +\
            'Drug_Design_Project/atom_compounds/' +\
            'compound_ex.txt')

file2=open('/home/Robbie/Desktop/Drug_Design_Project/' +\
            'Drug_Design_Project/atom_compounds/' +\
            'morgan_fingerprint' +\
            'morgan_fingerprint_output.txt', 'w')

file2.close()

file2=open('/home/Robbie/Desktop/Drug_Design_Project/' +\
            'Drug_Design_Project/atom_compounds/' +\
            'morgan_fingerprint' +\
            'morgan_fingerprint_output.txt', 'a')

for i in file:
    print(i)
    fingerprint = smiles_to_fingerprint(i)
    print(fingerprint, '\n', file=file2)

file.close()
file2.close()
    
    
# Convert SMILES to fingerprints
"""
# Prepare the training data
X_train = np.array([fingerprint1, fingerprint2])
y_train = np.array([0, 1])  # Example labels (0 and 1)

# Train the SVM
svm = SVC()
svm.fit(X_train, y_train)

# Example prediction
test_smiles = 'CC(=O)NCC1=CC=CC=C1C(=O)O'
test_fingerprint = smiles_to_fingerprint(test_smiles)
prediction = svm.predict([test_fingerprint])
print(f'Prediction: {prediction}')
"""

from rdkit import Chem
from rdkit.Chem import AllChem

# Create a molecule object from a SMILES string
smiles = 'CCO'
mol = Chem.MolFromSmiles(smiles)

# Generate Morgan fingerprint with a radius of 2
radius = 2
fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, radius)

# Convert the fingerprint to a binary string representation
binary_string = fingerprint.ToBitString()

# Print the binary fingerprint
print(binary_string)