from manim import *

class C5_2_Q1_1(Scene):
    def construct(self):

      text=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("1.  ").shift(3*UP,6*LEFT))
      text.append(Text("将").arrange(
            buff=0.3).shift(3*UP,4.2*LEFT).scale(0.8))
      textEquation.append(MathTex(r"60 ^\circ").arrange(buff=0.3).move_to(
            text[1]).shift(0.8*RIGHT))
      textEquation.append(Text("化为弧度（答案以").arrange(
            buff=0.3).move_to(textEquation[0]).shift(3.1*RIGHT).scale(0.8))
      textEquation.append(MathTex(r"\pi").arrange(buff=0.3).move_to(
            textEquation[1]).shift(3.1*RIGHT))
      textEquation.append(Text("表示）。").arrange(
            buff=0.3).move_to(textEquation[2]).shift(1.4*RIGHT).scale(0.8))
      self.play(Write(text[0]))
      self.play(Write(text[1]),Write(textEquation[0])
            ,Write(textEquation[1]),Write(textEquation[2]),Write(textEquation[3]))
      self.wait(2)
      

      text.append( MathTex(r"60 ^\circ",r"="
            ,r"60 ^\circ \times \left( \frac{ \pi }{ 180^ \circ } \right)").move_to(
            text[1]).shift( 1.3* DOWN, 2*RIGHT)) 
      text.append( Text("弧度").move_to(text[2]).shift(3*RIGHT).scale(0.8)) 
      self.play(Write(text[2]),Write(text[3]),run_time=4)
      self.wait(2)

      text.append( MathTex(r" = \left( \frac{ \pi }{ 3 } \right)").move_to(
            text[3]).shift( 1.3* DOWN, 3.6*LEFT)) 
      text.append( Text("弧度").move_to(text[4]).shift(1.7*RIGHT).scale(0.8)) 
      self.play(Write(text[4]),Write(text[5]),run_time=4)
      self.wait(2)