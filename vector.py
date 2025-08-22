import copy

class Vector:
    def _init_(self, coords):
        self.coords = coords

    def get(self, i):
        return self.coords[i]

    def set(self, i, val):
        self.coords[i] = val

    def length(self):
        return len(self.coords)

    def add(self, other):
        if self.length() != other.length():
            raise ValueError("Vectors must be of same length")
        return Vector([a + b for a, b in zip(self.coords, other.coords)])

    def clone(self):
        return copy.deepcopy(self)

    def _str_(self):
        return f"Vector({self.coords})"

    def _eq_(self, other):
        if not isinstance(other, Vector):
            return False
        return self.coords == other.coords

    def _iter_(self):
        return iter(self.coords)

    def dot(self, other):
        if self.length() != other.length():
            raise ValueError("Vectors must be of same length")
        return sum(a * b for a, b in zip(self.coords, other.coords))

    def cross(self, other):
        if self.length() != 3 or other.length() != 3:
            raise ValueError("Cross product only defined for 3D vectors")
        a = self.coords
        b = other.coords
        return Vector([
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ])
