from manim import *

class C5_1_Q1_Intro_2(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
     
      text.append(
        Text("角度制 （Degree Measure)").shift(3*UP))
      self.play(Write(text[0]),run_time=4)
      self.wait()

      text.append( Text("一周角").move_to(text[0]).shift(DOWN,LEFT))
      text.append(MathTex(r"=  360 ^ \circ  ").move_to(text[1]).shift( 2.1*RIGHT).scale(1.2))   
      self.play(Write(text[1]),Write(text[2]),run_time=4)
      self.wait()

      text.append( MathTex(r"1 ^ \circ",r"= ",r"60' ").arrange(
            buff=0.3).move_to(text[1]).shift(DOWN, 1*RIGHT).scale(1.2))
      self.play(Write(text[3]),run_time=3)
      self.wait(2)

      text.append( MathTex(r" 1' ",r" =  ",r" 60 '' ").arrange(
            buff=0.3).move_to(text[3]).shift(DOWN).scale(1.2))
      self.play(Write(text[4]),run_time=3)
      self.wait()

    
