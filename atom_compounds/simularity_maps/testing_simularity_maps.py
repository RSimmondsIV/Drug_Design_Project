from rdkit import Chem

mol = Chem.MolFromSmiles('COc1cccc2cc(C(=O)NCCCCN3CCN(c4cccc5nccnc54)CC3)oc21')

refmol = Chem.MolFromSmiles('CCCN(CCCCN1CCN(c2ccccc2OC)CC1)Cc1ccc2ccccc2c1')

from rdkit.Chem import Draw

from rdkit.Chem.Draw import SimilarityMaps
import matplotlib
import matplotlib.pyplot as plt

fp = SimilarityMaps.GetAPFingerprint(mol, fpType='normal')

fp = SimilarityMaps.GetTTFingerprint(mol, fpType='normal')

fp = SimilarityMaps.GetMorganFingerprint(mol, fpType='bv')

fig, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol, mol, SimilarityMaps.GetMorganFingerprint)

plt.show()