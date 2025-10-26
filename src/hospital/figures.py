from abc import ABC, abstractmethod
import math

class PlaneFigure(ABC):
    @abstractmethod
    def compute_perimeter(self):
        pass

    @abstractmethod
    def compute_surface(self):
        pass


class Triangle(PlaneFigure):
    def __init__(self, base: float, c1: float, c2: float, h: float):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self) -> float:
        return self.base + self.c1 + self.c2

    def compute_surface(self) -> float:
        return 0.5 * self.base * self.h


class Rectangle(PlaneFigure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def compute_perimeter(self) -> float:
        return 2 * (self.a + self.b)

    def compute_surface(self) -> float:
        return self.a * self.b


class Circle(PlaneFigure):
    def __init__(self, radius: float):
        self.radius = radius

    def compute_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def compute_surface(self) -> float:
        return math.pi * (self.radius ** 2)
