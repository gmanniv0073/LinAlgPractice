# Animating a circle quickstart guide
# Manim Community v.0.17.2

# 3b1b Linear Algebra Review

#Using Manim Community edition https//github.com/ManimCommunity/manim for visualizations.
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