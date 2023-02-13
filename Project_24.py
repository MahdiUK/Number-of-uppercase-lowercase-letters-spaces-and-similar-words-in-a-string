A = tuple(input(" Please enter a string: "))
c = 0
d = 0
e = 0
for char in A:
    if char.isupper() == True:
     c += 1
    if char.islower() == True:
     d += 1
    if char.isspace() == True:
     e += 1
print(f'The Number of Uppered Characters= {c}')
print(f'The Number of Lowered Charachters= {d}')
print(f'The Number of Spaced Charachters= {e}')

def count_characters(A):
    frequency = {}
    for char in A:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
frequency = count_characters(A)
print(frequency)

       