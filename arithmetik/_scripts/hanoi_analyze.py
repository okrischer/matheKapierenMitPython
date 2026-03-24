from manim import *
config.background_color = GRAY_A

class Hanoi(Scene):
    def construct(self):
        ground = Line([-6, -3, 0], [6.4, -3, 0], color=BLUE)
        A = Rectangle(width=0.1, height=2, color=GRAY_D).set_fill(GRAY_D, opacity=1.0).move_to([-4, -3, 0],aligned_edge=DOWN)
        B = Rectangle(width=0.1, height=2, color=GRAY_D).set_fill(GRAY_D, opacity=1.0).move_to([0, -3, 0],aligned_edge=DOWN)
        C = Rectangle(width=0.1, height=2, color=GRAY_D).set_fill(GRAY_D, opacity=1.0).move_to([4, -3, 0],aligned_edge=DOWN)
        at = Text('A', color=RED).next_to(A, UP)
        bt = Text('B', color=RED).next_to(B, UP)
        ct = Text('C', color=RED).next_to(C, UP)
        game = VGroup(ground, A, B, C, at, bt, ct)

        n3 = Rectangle(width=3*0.5, height=0.2, color=GREEN_C).set_opacity(1.0).move_to(A, aligned_edge=DOWN)
        n2 = Rectangle(width=2*0.5, height=0.2, color=TEAL_C).set_opacity(1.0).move_to(A,aligned_edge=DOWN, coor_mask=[1, 0.9, 1])
        n1 = Rectangle(width=1*0.5, height=0.2, color=BLUE_C).set_opacity(1.0).move_to(A, aligned_edge=DOWN, coor_mask=[1, 0.8, 1])
        n_min1 =VGroup(n1, n2)

        self.add(game, n3, n_min1)

        self.wait(2)
        self.play(n_min1.animate.move_to(B, aligned_edge=DOWN))
        self.wait(2)
        self.play(n3.animate.move_to(C, aligned_edge=DOWN))
        self.wait(2)
        self.play(n_min1.animate.move_to(C, coor_mask=[1, 0.4, 1]))
        self.wait(2)
