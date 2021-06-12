from manim import *

class C5_1_Q3_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("3.  ").shift(3*UP,6*LEFT).scale(1.2))
      text.append(Text("432秒可记作多少分多少秒?",font='Open Sans Regular').shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)

      text.append(MathTex(r"432'' ",r"= ",r" 420''",r" +  12''").move_to(text[1]).shift(DOWN,0.8*LEFT).scale(1.2))
      text[2][2].set_color(ORANGE)
      self.play(Write(text[2]),run_time=3)
      self.wait()  

      tex1 =  MathTex(r" 7'").move_to(text[2][2]).shift(0.21*LEFT).scale(1.2)  
      self.play(Transform(text[2][2],tex1 ),  text[2][3].animate.shift(0.5*LEFT),run_time=2)
      self.wait() 
