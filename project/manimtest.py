# Animating a circle quickstart guide
# Manim Community v.0.17.2

# 3b1b Linear Algebra Review

# Using Manim Community edition https//github.com/ManimCommunity/manim for visualizations.
#    https://docs.manim.community/en/stable/tutorials/quickstart.html
#    Dependencies: Python >/= 3.7, ffmepeg, LaTeX.
#    Use chocolatey or scoop for Windows.
#    Use pip for Linux.
#    Use pipx for Mac.

from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

# manim -pql manimtest.py CreateCircle
# should show a pink circle on your default mp4 player.


# The general usage of Manim is as follows:

# The - p flag in the command above is for previewing, meaning the video file will automatically open when it is done rendering. The - ql flag is for a faster rendering at a lower quality.

# Some other useful flags include:

# -s to skip to the end and just show the final frame.
# -n < number > to skip ahead to the n'th animation of a scene.
# -f show the file in the file browser.

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)

class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)