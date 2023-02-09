# Just messing around with manim

from manim import *


class Helloworld(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))


class grid(Scene):
    def construct(self):
        dot = Dot()
        grid = VGroup(*[dot.copy().shift(x * RIGHT + y * UP) for x in range(-10, 10) for y in range(-10, 10)])
        self.add(grid)

        title = Text("Grid")
        title.scale(2)
        self.play(Write(title))
        



