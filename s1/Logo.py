from manim import *

class Logo(Scene):
    def construct(self):
        #self.camera.background_color = "#e07a5f"
        
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"#"#343434"
        logo_black = WHITE      
        ds_e = MathTex(r"\mathbb{E}", fill_color=logo_black).scale(7)
        ds_e.shift(2.25 * LEFT + 1.5 * UP)
        ds_t = MathTex(r"\mathbb{T}", fill_color=logo_black).scale(7)
        #circle = Circle(color=logo_blue, fill_opacity=1).shift(UP,LEFT).scale(2)
        square = Square(color=RED, fill_opacity=1).shift(UP,LEFT).scale(3)
        logo = VGroup(square, ds_e,ds_t)  # order matters
        logo.move_to(ORIGIN)      
        self.play(Write(logo),run_time=4)
        self.wait()
        #self.add(logo)