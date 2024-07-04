"""
## Description:
Design a system for calculating areas of different shapes using the SOLID principles.

## Task
* Create a Shape interface with a method getArea() (ISP)
* Implement Square and Rectangle that implements the Shape interface (OCP, LSP)
* Implement a shape analyzer class/function that can work with any Shape object (SRP)
* Add Circle and Triangle as Shapes which should not break existing code

## Instructions
1. Write a test for the smallest piece of functionality.
2. Write the minimum code necessary to pass the test.
3. Refactor the code to improve its quality.
4. Repeat!

"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def getArea(self) -> float:
        pass


class Square(Shape):
    def __init__(self, length: float):
        self.length = length

    def getArea(self) -> float:
        return self.length**2


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def getArea(self) -> float:
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def getArea(self) -> float:
        return math.pi * self.radius**2


class Pentagram(Shape):
    def getArea(self) -> float:
        return super().getArea()


class Triangle(Shape):
    def __init__(self, baselength: float, height: float):
        self.baselength = baselength
        self.height = height

    def getArea(self) -> float:
        return self.baselength * self.height / 2


class ShapeAnalyzer:
    def __init__(self) -> None:
        pass

    def getlargestShape(self, shapes: list[Shape]):
        largest_shape = None
        largest_area = 0
        for shape in shapes:
            if shape.getArea() > largest_area:
                largest_shape = shape
                largest_area = shape.getArea()
        return largest_shape

    def totalArea(self, shapes: list[Shape]):
        return sum(shape.getArea() for shape in shapes)
