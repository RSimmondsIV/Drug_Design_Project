from atom_pair_fingerprint.atom_pair_fingerprints import smiles_to_fingerprint as ap
from MACCS_keys_fingerprint.MACCS_keys_fingerprints import smiles_to_fingerprint as mk
from morgan_fingerprint.morgan_fingerprints import smiles_to_fingerprint as mf
from topological_torsion_fingerprint.topological_torsion_fingerprints import smiles_to_fingerprint as tt

SMILES = "CC(Sc1nc(N)cc(N)n1)c1nc(C(C)(C)C)no1"

atom_pair = ap(SMILES)
MACCS = mk(SMILES)
morgan = mf(SMILES)
topological = tt(SMILES)

all = [atom_pair, MACCS, morgan, topological]
