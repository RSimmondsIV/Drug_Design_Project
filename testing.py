from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw
from rdkit.Chem import AllChem


m = Chem.MolFromSmiles('Cc1ccccc1')

from rdkit.Chem import Draw

img = Draw.MolToImage(m)
img.show()



# Create a molecule from a SMILES string
smiles = "CC(=O)O" # Acetic Acid
mol = Chem.MolFromSmiles(smiles)

# Calculate the molecular weight
weight = Descriptors.MolWt(mol)

# Generate a 2D depiction of the molecule
img = Draw.MolToImage(mol)

# Display the molecular weight and the molecule image
print("Molecular Weight:", weight)
img.show()

# Define reactant molecules
reactant1 = Chem.MolFromSmiles("CCO")
reactant2 = Chem.MolFromSmiles("CC(=O)O")

# Combine reactants into a reaction
reaction = AllChem.ReactionFromSmarts("[OH:1].[C:2](=[O:3])[OH:4]>>[O:1][C:2](=[O:3])O.[H:4]")

# Run the reaction
product = reaction.RunReactants((reactant1, reactant2))

# Get the resulting product molecule
product_mol = product[0][0]

# Convert the product molecule to SMILES
product_smiles = Chem.MolToSmiles(product_mol)
image = Chem.MolFromSmiles(product_smiles)

image = Draw.MolToImage(mol)

# Print the product SMILES
image.show()
print("Product SMILES:", product_smiles)