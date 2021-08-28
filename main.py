from os import write
from manim import *
from numpy import dot

class Abertura(Scene):
    def construct(self):
        ponto = Dot([0,0,0])
        circulo = Circle(color=RED)
        titulo = Text("Codando") 
        com = Tex("com")
        titulo.set_y(1)
        thalyson = Text("Thalyson")
        thalyson.set_y(-1)
        retangulo = Rectangle(height=3.5, width=6.0, color=RED)
        final = Dot([0,0,0])

        self.play(FadeIn(ponto))
        self.play(ReplacementTransform(ponto, circulo))
        self.wait(1)
        self.play(circulo.animate.shift(LEFT*4))
        self.play(ReplacementTransform(circulo, retangulo),  Write(titulo))
        self.play(Write(thalyson), Write(com))
        self.wait(2)
        grupo = Group(thalyson, titulo, retangulo, com)
        self.play(ReplacementTransform(grupo, final))
        self.play(FadeOut(final))
        self.wait(2)
        
        



