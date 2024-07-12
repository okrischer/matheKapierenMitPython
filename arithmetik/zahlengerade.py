from manim import *
config.background_color = GRAY_A

class Gerade(Scene):
  def construct(self):
    line = NumberLine(
      x_range=[-4, 4],
      #length=12,
      unit_size=1.5,
      color=GRAY_D,
      include_numbers=True,
      numbers_with_elongated_ticks=[-3, -2, -1, 0, 1, 2, 3],
      include_ticks=True,
      include_tip=True,
    )

    for num in line.numbers:
      num.set_color(GRAY_D)
    
    t_sq = Line([1.41*1.5, 0, 0], [1.41*1.5, -1, 0], color=BLUE)
    sq2 = MathTex('\sqrt{2}', color=BLUE).next_to(t_sq, DOWN)
    sq = Group(t_sq, sq2)

    t_e = Line([2.72*1.5, 0, 0], [2.72*1.5, -1, 0], color=BLUE)
    e = MathTex('e', color=BLUE).next_to(t_e, DOWN)
    ez = Group(t_e, e)

    t_pi = Line([3.14*1.5, 0, 0], [3.14*1.5, -1, 0], color=BLUE)
    pi = MathTex('\pi', color=BLUE).next_to(t_pi, DOWN)
    kpi = Group(t_pi, pi)

    R = MathTex('\mathbb{R}', color=GRAY_D, font_size=60).next_to([-5, -1.5, 0])

    self.add(line, R, sq, ez, kpi)
