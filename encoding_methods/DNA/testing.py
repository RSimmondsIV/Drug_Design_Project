DNA_SEQUENCE = "aactggttagagtccgtataacagtatgcgtcacgaccataatccgagga" # RANDOM

new_sequnce = []
final_sequence = []
for i in DNA_SEQUENCE:
    if i == 'a':
        new_sequnce.append(1001)
    if i == 'c':
        new_sequnce.append(1011)
    if i == 't':
        new_sequnce.append(1101)
    if i =='g':
        new_sequnce.append(1111)

for i in new_sequnce:
    final_sequence.append(str(i))

seq = "".join(final_sequence)

print(int(seq))