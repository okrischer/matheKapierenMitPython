from manim import *
config.background_color = GRAY_A

class Euler(Scene):
  def construct(self):
    U = Square(side_length=4, color=BLACK)
    A = Circle(1.3, RED)
    AT = MathTex('A', color=RED).next_to([-1, 0.8, 0])
    xT = MathTex('x', color=RED).next_to([0, 0, 0])
    XinA = MathTex('x \in A', color=RED).next_to(U, UP)
    IN = VGroup(U, A, XinA, AT, xT)
    IN.move_to([-4.5, 0, 0])

    U2 = Square(side_length=4, color=BLACK)
    A2 = Circle(1.3, RED)
    AT2 = MathTex('A', color=RED).next_to([-1, 0.8, 0])
    xT2 = MathTex('x', color=RED).next_to([1.3, -1.4, 0])
    XnotinA = MathTex(r"x \notin A", color=RED).next_to(U2, UP)
    notIN = VGroup(U2, A2, XnotinA, AT2, xT2)
    notIN.move_to([0,0.1,0])

    U3 = Square(side_length=4, color=BLACK)
    A3 = Circle(1.3, RED)
    B = Circle(0.7, BLUE).shift([0.2, -0.1, 0])
    AT3 = MathTex('A', color=RED).next_to([-1, 0.8, 0])
    BT = MathTex('B', color=BLUE).next_to(ORIGIN)
    BsubA = MathTex(*r"B \subset A".split(" "), color=RED).next_to(U3, UP)
    BsubA[0].set_color(BLUE)
    sub = VGroup(U3, A3, B, AT3, BT, BsubA)
    sub.move_to([4.5,0.1,0])

    self.add(IN, notIN, sub)