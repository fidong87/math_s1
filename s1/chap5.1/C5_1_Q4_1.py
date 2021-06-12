from manim import *


class C5_1_Q4_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("4.  ").shift(3*UP,6*LEFT).scale(1.2))
      text.append(Text("5602秒可记作多少度多少分多少秒",font='Open Sans Regular').shift(3*UP,0*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)

      text.append(MathTex(r"5602'' ",r"= ",r" 5580''",r" + 22''").move_to(text[1]).shift(DOWN,0.8*LEFT).scale(1.2))
      text[2][2].set_color(ORANGE)
      self.play(Write(text[2]),run_time=3)
      self.wait()  

      tex1 =  MathTex(r" 73'").move_to(text[2][2]).shift(0.2*LEFT).scale(1.2)  
      self.play(Transform(text[2][2],tex1 ),  text[2][3].animate.shift(0.5*LEFT),run_time=2)
      self.wait() 

      text.append(MathTex(r"= ",r" 60' +",r"  13'  ",r" 22''").move_to(text[2]).shift(DOWN,0.85*RIGHT).scale(1.2))
      text[3][3].shift(0.5*RIGHT)
      text[3][1].set_color(ORANGE)
      self.play(Write(text[3]),run_time=3)
      self.wait()  

      tex2 =  MathTex(r"1^ \circ").move_to(text[3][1]).scale(1.2)  
      self.play(Transform(text[3][1],tex2 ),run_time=2)
      self.wait() 
   