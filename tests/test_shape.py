from coding_katas.shape import Square, Triangle, Rectangle, Circle, ShapeAnalyzer
import math


def test_calculate_total_area_with_mutlipe_shapes_returns_correct_area_result():
    assert Square(length=8).getArea() == 64
    assert Rectangle(length=4, width=5).getArea() == 20
    assert Circle(radius=1).getArea() == math.pi
    assert Triangle(baselength=10, height=4).getArea() == 20


def test_largest_shape_with_mutlipe_shapes_returns_largest_shape():
    shapes = [
        Square(length=8),
        Rectangle(length=4, width=5),
        Circle(radius=1),
        Triangle(baselength=10, height=4),
    ]

    analyzer = ShapeAnalyzer()

    assert analyzer.getlargestShape(shapes) == shapes[0]


def test_correct_total_area_on_list_of_shapes():
    shapes = [
        Square(length=8),
        Rectangle(length=4, width=5),
    ]

    analyzer = ShapeAnalyzer()

    assert analyzer.totalArea(shapes=shapes) == 84
