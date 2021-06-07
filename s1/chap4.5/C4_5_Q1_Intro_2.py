from manim import *

class C4_5_Q1_Intro_2(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]

      textAnimate.append(Text("当").shift(3*UP, 3*LEFT))
      self.play(Write(textAnimate[0]) ,run_time=1) 
      text.append(MathTex("\\sqrt{a+2\\sqrt{b}} ","  x > 0,","y > 0,"
          ).move_to(textAnimate[0]).shift(3.5*RIGHT))
      self.play(Write(text[0]) ,run_time=2) 
      self.wait()

      text.append(Text("使得").move_to(text[0]).shift(DOWN, 3*LEFT))
      self.play(Write(text[1]) , run_time=2) 
      text.append(MathTex(r"\left\{ \begin{array}{c} a=x+y, \\ b=xy, \end{array}").move_to(text[1]).shift(3*RIGHT))
      self.play(Write(text[2]),run_time=2)
      self.wait()

      text.append(Text("那么").move_to(text[1]).shift(DOWN))
      self.play(Write(text[3]) , run_time=2)
      text.append(MathTex("\\sqrt{a+2\\sqrt{b}} ","=","\\sqrt{x+y+2\\sqrt{xy}}"
          ).move_to(text[3]).shift(4*RIGHT))
      self.play(Write(text[4]) , run_time=2)
      self.wait()

      text.append(MathTex("=","\\sqrt{(\\sqrt{x} + \\sqrt{y})^2}"
          ).move_to(text[4]).shift(DOWN, 0.95*RIGHT))
      self.play(Write(text[5]) , run_time=2)
      self.wait()

      text.append(MathTex("=","\\sqrt{x} + \\sqrt{y}}"
          ).move_to(text[5]).shift(DOWN, 0.55*LEFT))
      self.play(Write(text[6]) , run_time=2)
      self.wait()

     
