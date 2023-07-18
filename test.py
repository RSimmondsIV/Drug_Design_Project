import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Example dataset with SMILES and corresponding labels
smiles = ['CCO', 'CCC', 'CCN', 'CNC', 'CN']
labels = [0, 0, 0, 1, 1]

# Parse SMILES and generate molecular fingerprints
mols = [Chem.MolFromSmiles(smi) for smi in smiles]
fps = [AllChem.GetMorganFingerprintAsBitVect(mol, 2) for mol in mols]
X = np.array(fps)  # Feature matrix
y = np.array(labels)  # Labels

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM model
svm = SVC()
svm.fit(X_train, y_train)

# Predict on test data
y_pred = svm.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")