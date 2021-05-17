from manim import *

class ShapeWithContent(VGroup):
    def __init__(self, content):
        super().__init__()
        self.shape = Rectangle(width=12.0, height=2.0).set_color(ORANGE)
        self.content = content
        self.add(self.shape, content)
        content.move_to(self.shape.get_center())

    def clear_content(self):
        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def _clear_content_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = Uncreate(self.content, **anim_args)
        self.clear_content()
        return anim

class C4_Q4_1(Scene):
    def construct(self):

       	text=MathTex("\\sqrt{x-1} - \\sqrt{x+1} = 2")
       	my_mobject = ShapeWithContent(text)
        self.play(Create(my_mobject))
        self.wait(3)
        self.play(my_mobject.animate.clear_content())
        self.wait()
