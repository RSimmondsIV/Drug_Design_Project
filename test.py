from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

# Create a molecule object
mol = Chem.MolFromSmiles('CCO')

# Create the atom pair fingerprint generator
generator = rdFingerprintGenerator.GetAtomPairGenerator()

# Generate the atom pair fingerprint
fingerprint = generator.GetFingerprint(mol)

# Get the atom pair fingerprint as a bit vector
bit_vector = fingerprint.ToBitString()

# Print the atom pair fingerprint
print(bit_vector)