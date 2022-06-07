from dataclasses import dataclass


@dataclass
class Money:
    value: int
    currency: str = "USD"
