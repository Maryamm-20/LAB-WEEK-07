from Vector import Vector

# Create two vectors
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Test methods
print("v1:", v1)
print("v2:", v2)
print("Add:", v1.add(v2))
print("Dot product:", v1.dot(v2))
print("Cross product:", v1.cross(v2))
print("Clone v1:", v1.clone())
print("v1 == v2?", v1 == v2)

# Iterate through v1
print("Iterating v1:")
for val in v1:
    print(val)
