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

file = open(file='atom_compounds/' +\
            'compound_list.txt')

comps = []
for i in file:
    comps.append(i)

for i in range(len(comps)):
    plt.figure(i)
    fig, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(comps[i], comps[i], SimilarityMaps.GetMorganFingerprint)

plt.show()

#TODO Fix Unknown Error - rdkit.Chem.rdMolDescriptors.GetMorganFingerprintAsBitVect(str, int)
"""
did not match C++ signature: GetMorganFingerprintAsBitVect(RDKit::ROMol mol, unsigned int radius, 
unsigned int nBits=2048, boost::python::api::object invariants=[], boost::python::api::object fromAtoms=[], 
bool useChirality=False, bool useBondTypes=True, bool useFeatures=False, boost::python::api::object bitInfo=None, 
bool includeRedundantEnvironments=False)
"""