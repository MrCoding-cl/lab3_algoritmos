from itertools import permutations
l = list("bazooka")
print(l)
perm = set(permutations(l))
c = 0
for x in perm:
    c2 = 0
    while c2 < len(x):
        if x[c2] == 'o':
            if x[c2 + 1] != 'o':
                print(''.join(x))
                c += 1
            break
        c2 += 1
print(f'Cantidad de palabras isn que se repita la O: {c}')