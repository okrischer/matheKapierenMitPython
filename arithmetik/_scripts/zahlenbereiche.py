from manim import *
config.background_color = GRAY_A

class Zahlenbereiche(Scene):
  def construct(self):
    N = Ellipse(width=2, height=1, color=GREEN)
    Z = Ellipse(width=4, height=2, color=BLUE)
    Q = Ellipse(width=6, height=3, color=ORANGE)
    R = Ellipse(width=8, height=4, color=RED)
    ZB = VGroup(N,Z,Q,R)

    NN = MathTex('\mathbb{N}', color=GREEN).next_to([-1, 0, 0])
    eins = MathTex('1', color=GREEN, font_size=30).next_to([-0.3, 0.3, 0])
    vier = MathTex('4', color=GREEN, font_size=30).next_to([0.2, -0.2, 0])
    NZ = VGroup(NN, eins, vier)

    ZZ = MathTex('\mathbb{Z}', color=BLUE).next_to([-2, 0, 0])
    null = MathTex('0', color=BLUE, font_size=30).next_to([-1.5, 0.4, 0])
    drei = MathTex('-3', color=BLUE, font_size=30).next_to([-1.3, -0.6, 0])
    GZ = VGroup(ZZ, null, drei)

    QQ = MathTex('\mathbb{Q}', color=ORANGE).next_to([-3, 0, 0])
    einhalb = MathTex(r'\frac{1}{2}', color=ORANGE, font_size=25).next_to([-2.6, 0.5, 0])
    dreiviertel = MathTex(r'-\frac{3}{4}', color=ORANGE, font_size=25).next_to([-2.6, -0.6, 0])
    einszwof = MathTex('1,25', color=ORANGE, font_size=30).next_to([-1.8, 1, 0])
    mindrei = MathTex('-3,33', color=ORANGE, font_size=30).next_to([-2, -1.1, 0])
    QZ = VGroup(QQ, einhalb, dreiviertel, einszwof, mindrei)

    RR = MathTex('\mathbb{R}', color=RED).next_to([-4, 0, 0])
    wurzel = MathTex(r'\sqrt{2}', color=RED, font_size=30).next_to([-3.6, 0.7, 0])
    wurf = MathTex(r'\sqrt{5}', color=RED, font_size=30).next_to([-3, 1.2, 0])
    e = MathTex('e', color=RED, font_size=35).next_to([-3.6, -0.7, 0])
    pi = MathTex(r'\pi', color=RED, font_size=35).next_to([-3, -1.1, 0])
    RZ = VGroup(RR, wurzel, wurf, e, pi)

    self.add(ZB, NZ, GZ, QZ, RZ)