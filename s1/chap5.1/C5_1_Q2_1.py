from manim import *

class C5_1_Q2_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("2.  ").shift(3*UP,6*LEFT))
      text.append(Text("5度12分可记作多少分?",font='Open Sans Regular').shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)

      text.append(MathTex(r"5 ^ \circ ",r" 12' ",r"= "
            ,r" 300'+ 12'").arrange(buff=0.3).move_to(text[1]).shift(DOWN,0.8*LEFT).scale(1.2))
      text[2][3].set_color(ORANGE)
      self.play(Write(text[2]),run_time=3)
      self.wait()  

      tex1 =  MathTex(r" 312'").move_to(text[2][3]).shift(0.8*LEFT).scale(1.2)  
      self.play(Transform(text[2][3],tex1 ),run_time=2)
      self.wait() 

   