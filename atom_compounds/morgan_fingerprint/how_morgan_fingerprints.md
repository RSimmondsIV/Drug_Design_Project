Obtain the fingerprint vector: The GetMorganFingerprint() function returns a binary fingerprint vector that represents the presence or absence of specific circular substructures in the molecule. Each bit in the vector corresponds to a particular substructure, and a value of 1 indicates the presence of that substructure, while a value of 0 indicates its absence.

In the fingerprint, in this case stored in a Numpy Array each index related to a certain substructure, where 1 means present and 0 means not present.

The exact structure at each index is standard and done through RDKit's library and functional operations. 