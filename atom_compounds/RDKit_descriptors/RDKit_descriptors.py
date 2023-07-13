from rdkit import Chem
from rdkit.Chem import Descriptors

# Define the SMILES string

# Create an RDKit molecule object from the SMILES string


def calculate(smile):
# Calculate RDKit descriptors
    mol = Chem.MolFromSmiles(smile)
    descriptors = []
    for descriptor_name, descriptor_function in Descriptors.descList:
        descriptor_value = descriptor_function(mol)
        descriptors.append(descriptor_value)
    return descriptors

file = open(file='atom_compounds/' +\
            'compound_ex.txt')

file2=open('atom_compounds/' +\
            'RDKit_descriptors/' +\
            'RDKit_descriptors_output.txt', 'w')

file2.close()

file2=open('atom_compounds/' +\
            'RDKit_descriptors/' +\
            'RDKit_descriptors_output.txt', 'a')

for i in file:
    print(i)
    # a = Draw.MolToImage(Chem.MolFromSmiles(str(i)))
    # a.show()
    fingerprint = calculate(i)
    print(fingerprint, '\n', file=file2)