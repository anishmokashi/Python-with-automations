
Batches = {"PPA" : 18500, "Python" : 18700, "LB" : 19000, "Angular" : 19200, "LSP" : 18200, "C#" : 21000}

print(Batches)

print(type(Batches))

print(len(Batches))

print(Batches["Python"])

for value in Batches:
    print(value)

for value in Batches:
    print(Batches[value])

for value in Batches:
    print(value, Batches[value])