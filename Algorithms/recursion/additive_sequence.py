

def additive_sequence(n, b1, b2):
    if n == 0:
        return b1
    else:
        return additive_sequence(n - 1, b2, b1 + b2)

print(additive_sequence(8, 0,1))
print(additive_sequence(8, 4,6))