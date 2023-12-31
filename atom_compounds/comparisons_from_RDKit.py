from atom_pair_fingerprint.atom_pair_fingerprints import smiles_to_fingerprint as ap
from MACCS_keys_fingerprint.MACCS_keys_fingerprints import smiles_to_fingerprint as mk
from morgan_fingerprint.morgan_fingerprints import smiles_to_fingerprint as mf
from topological_torsion_fingerprint.topological_torsion_fingerprints import smiles_to_fingerprint as tt
from one_hot_encoding.one_hot_encoding import one_hot_encode as oh
from RDKit_descriptors.RDKit_descriptors import get_descripors as gd
import numpy as np 
import sys
np.set_printoptions(threshold=sys.maxsize)

SMILES = "CCONNO"

atom_pair = ap(SMILES)
MACCS = mk(SMILES)
morgan = mf(SMILES)
topological = tt(SMILES)
Descriptors = gd(SMILES)
# ONEHOT = oh(SMILES)

print(
    atom_pair,
    "\n",
    "\n",
    MACCS,
    "\n",
    "\n",
    morgan,
    "\n",
    "\n",
    topological,
    "\n",
    "\n",
    Descriptors
    # ONEHOT
)