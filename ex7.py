import copy

original = [[1, 2], [3, 4]]
copied = copy.deepcopy(original)

print("Original:", original)
print("Copied:", copied)

print(id(original))
print(id(copied))
