from manim import *
config.background_color = GRAY_A

class Venn(Scene):
  def construct(self):
    A = Circle(1, BLACK)
    B = Circle(1, BLACK).shift(RIGHT)
    V = Union(A, B, color=RED, fill_opacity=1)
    AoderB = MathTex('A \cup B', color=RED).next_to(A, UP).shift([0.5,0,0])
    VM = VGroup(V, A, B, AoderB)
    VM.move_to([-4, 2, 0])

    A1 = Circle(1, BLACK)
    B1 = Circle(1, BLACK).shift(RIGHT)
    S = Intersection(A1, B1, color=RED, fill_opacity=1)
    AundB = MathTex('A \cap B', color=RED).next_to(A1, UP).shift([0.5,0,0])
    SM = VGroup(S, A1, B1, AundB)
    SM.move_to([2, 2, 0])

    A2 = Circle(1, BLACK)
    B2 = Circle(1, BLACK).shift(RIGHT)
    D = Difference(A2, B2, color=RED, fill_opacity=1)
    AdiffB = MathTex(r"A \backslash B", color=RED).next_to(A2, UP).shift([0.5,0,0])
    DM = VGroup(D, A2, B2, AdiffB)
    DM.move_to([-4, -2, 0])

    A3 = Circle(1, BLACK)
    B3 = Circle(1, BLACK).shift(RIGHT)
    Delta = Exclusion(A3, B3, color=RED, fill_opacity=1)
    AsymB = MathTex('A \Delta B', color=RED).next_to(A3, UP).shift([0.5,0,0])
    SDM = VGroup(Delta, A3, B3, AsymB)
    SDM.move_to([2, -2, 0])

    self.add(VM, SM, DM, SDM)