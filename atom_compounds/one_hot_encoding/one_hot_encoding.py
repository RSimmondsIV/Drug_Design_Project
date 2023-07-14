# From CHATGPT-4
import numpy as np
import sys

def one_hot_encode(labels):
    # Determine the unique labels in the dataset
    unique_labels = np.unique(labels)
    
    # Initialize an array of zeros with the appropriate shape
    encoding = np.zeros((len(labels), len(unique_labels)))
    
    # Assign 1 to the corresponding position for each label
    for i, label in enumerate(labels):
        index = np.where(unique_labels == label)[0][0]
        encoding[i, index] = 1
    
    return encoding

if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)

    file = open(file='atom_compounds/' +\
            'compound_list.txt')

    file2=open('atom_compounds/' +\
            'one_hot_encoding/' +\
            'one_hot_encoding_output.txt', 'w')

    file2.close()

    file2=open('atom_compounds/' +\
            'one_hot_encoding/' +\
            'one_hot_encoding_output.txt', 'a')

    for i in file:
        print(i)
        # a = Draw.MolToImage(Chem.MolFromSmiles(str(i)))
        # a.show()
        new = [*i]
        print(new)
        encoded = one_hot_encode(new)
        print(encoded, '\n', file=file2)

    file.close()
    file2.close()