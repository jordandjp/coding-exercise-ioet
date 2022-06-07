from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Money:
    value: int
    currency: str = "USD"

    def __add__(self, other: Money) -> Money:
        if self.currency != other.currency:
            ValueError("Money objects must be of the same currency")

        return Money(self.value + other.value, self.currency)

    def __mul__(self, other: int) -> Money:
        return Money(self.value * other, self.currency)

    def __rmul__(self, other: int) -> Money:
        return self * other
