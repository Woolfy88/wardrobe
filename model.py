from dataclasses import dataclass, field
from typing import List

@dataclass
class Shelf:
    y: int  # height from floor (mm)

@dataclass
class Hanging:
    top: int
    bottom: int

@dataclass
class Drawer:
    y: int
    height: int = 180

@dataclass
class Bay:
    width: int
    shelves: List[Shelf] = field(default_factory=list)
    hangings: List[Hanging] = field(default_factory=list)
    drawers: List[Drawer] = field(default_factory=list)

@dataclass
class Wardrobe:
    total_width: int
    height: int
    depth: int
    bays: List[Bay]
