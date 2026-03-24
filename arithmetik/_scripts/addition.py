from manim import *
config.background_color = GRAY_A

class Addition(Scene):
  def construct(self):
    s1 = MathTex(*r"7  \ 4  \ ,  2  \ 5".split("  "))
    s1[0].set_color(ORANGE)
    s1[1].set_color(BLUE)
    s1[2].set_color(GRAY_D)
    s1[3].set_color(GREEN)
    s1[4].set_color(PURE_GREEN)

    s2 = MathTex(*r"2  \ 6  \ ,  7  \ 6".split("  ")).next_to(s1, DOWN)
    s2[0].set_color(ORANGE)
    s2[1].set_color(BLUE)
    s2[2].set_color(GRAY_D)
    s2[3].set_color(GREEN)
    s2[4].set_color(PURE_GREEN)

    l = Line([-1.5, -1, 0], [1, -1, 0], color=RED)
    a = MathTex('+', color=RED).next_to([-1.9, -0.75, 0])

    r = MathTex(*r"1  \ 0  \ 1  \ ,  0  \ 1".split("  ")).next_to([-1.45, -1.4, 0])
    r[0].set_color(RED)
    r[1].set_color(ORANGE)
    r[2].set_color(BLUE)
    r[3].set_color(GRAY_D)
    r[4].set_color(GREEN)
    r[5].set_color(PURE_GREEN)

    self.add(s1, s2, l, a)

    frame = Rectangle(width=0.43, height=0.53, color=RED).move_to(s1[4], [0,0,0])
    self.play(FadeIn(frame))

    self.play(frame.animate.move_to(s2[4]))
    self.play(frame.animate.move_to(r[5]))
    self.play(FadeIn(r[5], MathTex('1', color=RED, font_size=30).next_to([0.15, -0.8, 0])))

    self.play(frame.animate.move_to(s1[3]))
    self.play(frame.animate.move_to(s2[3]))
    self.play(frame.animate.move_to(r[4]))
    self.play(FadeIn(r[4], r[3], MathTex('1', color=RED, font_size=30).next_to([-0.45, -0.8, 0])))

    self.play(frame.animate.move_to(s1[1]))
    self.play(frame.animate.move_to(s2[1]))
    self.play(frame.animate.move_to(r[2]))
    self.play(FadeIn(r[2], MathTex('1', color=RED, font_size=30).next_to([-0.85, -0.8, 0])))

    self.play(frame.animate.move_to(s1[0]))
    self.play(frame.animate.move_to(s2[0]))
    self.play(frame.animate.move_to(r[1]))
    self.play(FadeIn(r[1], MathTex('1', color=RED, font_size=30).next_to([-1.4, -0.8, 0])))

    self.play(frame.animate.move_to(r[0]))
    self.play(FadeIn(r[0]))
    self.play(FadeOut(frame))
    self.wait()
