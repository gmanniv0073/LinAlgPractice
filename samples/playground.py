# Just messing around with manim

from manim import *


class Helloworld(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))


class grid(Scene):
    def construct(self):
        dot = Dot()
        grid = VGroup(*[dot.copy().shift(x * RIGHT + y * UP)
                      for x in range(-10, 10) for y in range(-10, 10)])
        self.add(grid)

        title = Text("Grid")
        title.scale(2)
        self.play(Write(title))


class grid2(Scene):
    def construct(self):
        dot = Dot()
        grid = VGroup(*[dot.copy().shift(x * RIGHT + y * UP)
                      for x in range(-10, 10) for y in range(-10, 10)])
        self.add(grid)

        title = Text("Grid")
        title.scale(2)
        self.play(Write(title))

        self.play(grid.animate.shift(UP * 2))

        self.play(grid.animate.shift(LEFT * 2))

        self.play(grid.animate.shift(DOWN * 2))

        self.play(grid.animate.shift(RIGHT * 2))

        self.play(grid.animate.shift(UP * 2))

        self.play(grid.animate.shift(LEFT * 2))

        self.play(grid.animate.shift(DOWN * 2))

        self.play(grid.animate.shift(RIGHT * 2))

        self.wait(1)


class gridandarrow(Scene):
    def construct(self):
        dot = Dot()
        grid = VGroup(*[dot.copy().shift(x * RIGHT + y * UP)
                      for x in range(-10, 10) for y in range(-10, 10)])
        self.add(grid)

        title = Text("Grid")
        title.scale(2)

        arrow = Arrow(LEFT, RIGHT)
        arrow.scale(2)
        
        self.play(Write(title))

        self.play(grid.animate.shift(UP * 2))
        
        self.play(grid.animate.shift(LEFT * 2))

        self.play(grid.animate.shift(DOWN * 2))

        self.play(grid.animate.shift(RIGHT * 2))

        self.play(arrow.animate.rotate(PI/2))

        self.play(arrow.animate.rotate(PI/2))

        transform = Transform(title, arrow)
        self.play(transform)
        
        self.wait(1)