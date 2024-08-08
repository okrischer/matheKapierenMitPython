from manim import *
config.background_color = GRAY_A

class Hanoi(Scene):
    def construct(self):
        ground = Line([-6, -3, 0], [6.4, -3, 0], color=BLUE)
        self.A = Rectangle(width=0.1, height=2, color=GRAY_D).set_fill(GRAY_D, opacity=1.0).move_to([-4, -3, 0],aligned_edge=DOWN)
        self.B = Rectangle(width=0.1, height=2, color=GRAY_D).set_fill(GRAY_D, opacity=1.0).move_to([0, -3, 0],aligned_edge=DOWN)
        self.C = Rectangle(width=0.1, height=2, color=GRAY_D).set_fill(GRAY_D, opacity=1.0).move_to([4, -3, 0],aligned_edge=DOWN)
        at = Text('A', color=RED).next_to(self.A, UP)
        bt = Text('B', color=RED).next_to(self.B, UP)
        ct = Text('C', color=RED).next_to(self.C, UP)
        game = VGroup(ground, self.A, self.B, self.C, at, bt, ct)
        self.add(game)

        colors = [WHITE, BLUE_C, TEAL_C, GREEN_C, YELLOW_C]
        self.disks = VGroup()

        for i in range(4, 0, -1):
            self.disks.add(Rectangle(width=i*0.5, height=0.2, color=colors[i])
                     .set_opacity(1.0)
                     .move_to(self.A, aligned_edge=DOWN, coor_mask=[1, 0.6+i*0.1, 1]))

        self.add(self.disks)

        n = 4
        self.moves = []
        self.ast = []
        self.bst = []
        self.cst = []
        for i in range(n, 0, -1):
            self.ast.append(i)

        self.hanoi('A', 'C', 'B', n)
        self.wait()
        for m in self.moves:
            self.move(m, n)
        self.wait()


    def move(self, m, n):
        (f, t) = m
        a = -4
        b = 0
        c = 4
        g = -2.9
        h = 0.3
        if f == 'A':
            i = n - self.ast[-1]
            if t == 'B':
                o = len(self.bst)*h
                self.play(self.disks[i].animate.move_to([b, g+o, 0]))
                self.bst.append(self.ast.pop())
            elif t == 'C':
                o = len(self.cst)*h
                self.play(self.disks[i].animate.move_to([c, g+o, 0]))
                self.cst.append(self.ast.pop())
        elif f == 'B':
            i = n - self.bst[-1]
            if t == 'A':
                o = len(self.ast)*h
                self.play(self.disks[i].animate.move_to([a, g+o, 0]))
                self.ast.append(self.bst.pop())
            elif t == 'C':
                o = len(self.cst)*h
                self.play(self.disks[i].animate.move_to([c, g+o, 0]))
                self.cst.append(self.bst.pop())
        elif f == 'C':
            i = n - self.cst[-1]
            if t == 'A':
                o = len(self.ast)*h
                self.play(self.disks[i].animate.move_to([a, g+o, 0]))
                self.ast.append(self.cst.pop())
            elif t == 'B':
                o = len(self.bst)*h
                self.play(self.disks[i].animate.move_to([b, g+o, 0]))
                self.bst.append(self.cst.pop())


    def hanoi(self, start, ziel, temp, n):
        if n == 0: return
        self.hanoi(start, temp, ziel, n-1)
        self.moves.append((start, ziel))
        self.hanoi(temp, ziel, start, n-1)
