from typing import List, Iterator
import copy

class Vector:
    def _init_(self, coords: List[float]):
        self.coords = coords

    def get(self, i: int) -> float:
        return self.coords[i]

    def set(self, i: int, val: float):
        self.coords[i] = val

    def length(self) -> int:
        return len(self.coords)

    def add(self, other: 'Vector') -> 'Vector':
        if self.length() != other.length():
            raise ValueError("Vectors must be of same length")
        return Vector([a + b for a, b in zip(self.coords, other.coords)])

    def clone(self) -> 'Vector':
        return copy.deepcopy(self)

    def _str_(self) -> str:
        return f"Vector({self.coords})"

    def _eq_(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.coords == other.coords

    def _iter_(self) -> Iterator[float]:
        return iter(self.coords)

    def dot(self, other: 'Vector') -> float:
        if self.length() != other.length():
            raise ValueError("Vectors must be of same length")
        return sum(a * b for a, b in zip(self.coords, other.coords))

    def cross(self, other: 'Vector') -> 'Vector':
        if self.length() != 3 or other.length() != 3:
            raise ValueError("Cross product only defined for 3D vectors")
        a = self.coords
        b = other.coords
        return Vector([
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ])
