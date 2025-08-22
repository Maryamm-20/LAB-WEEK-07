from Range import Range

# Create a range
r = Range(1, 10, 2)

# Iterate through range
print("Range values:")
for i in r:
    print(i)

# Test membership
print("5 in range?", 5 in r)
print("6 in range?", 6 in r)

# Print range object
print(r)
