from typing import Iterator

class Range:
    def _init_(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        self._current = start

    def _iter_(self) -> Iterator[int]:
        self._current = self.start
        return self

    def _next_(self) -> int:
        if (self.step > 0 and self._current >= self.end) or (self.step < 0 and self._current <= self.end):
            raise StopIteration
        val = self._current
        self._current += self.step
        return val

    def _contains_(self, value: int) -> bool:
        if self.step > 0:
            return self.start <= value < self.end and (value - self.start) % self.step == 0
        else:
            return self.end < value <= self.start and (self.start - value) % abs(self.step) == 0

    def _str_(self) -> str:
        return f"Range({self.start}, {self.end}, {self.step})"
