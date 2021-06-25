from manim import *

class C5_2_Q2_1(Scene):
    def construct(self):

      text=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("2.  ").shift(3*UP,6*LEFT))
      text.append(Text("将").arrange(
            buff=0.3).shift(3*UP,4.2*LEFT).scale(0.8))
      textEquation.append(MathTex(r"\frac{ 3\pi }{ 5} ").arrange(buff=0.3).move_to(
            text[1]).shift(0.8*RIGHT))
      textEquation.append(Text("化为角度。").arrange(
            buff=0.3).move_to(textEquation[0]).shift(2.2*RIGHT).scale(0.8))      
      self.play(Write(text[0]))
      self.play(Write(text[1]),Write(textEquation[0])
            ,Write(textEquation[1]))
      self.wait(2)
      

      text.append( MathTex(r"\frac{ 2\pi }{ 5} ",r"="
            ,r"\frac{ 2\pi }{ 5} \times \left( \frac{ 180^ \circ }{ \pi } \right)").move_to(
            text[1]).shift( 1.3* DOWN, 2*RIGHT)) 
      self.play(Write(text[2]),run_time=4)
      self.wait(2)

      textEquation.append(text[2][2].copy())
      tex= MathTex(r"\frac{ \pi }{ 1} \times \left( \frac{ 36^ \circ }{ \pi } \right)").move_to(
            text[2][2]).set_color(ORANGE)
      self.play(Transform(text[2][2],tex ),run_time=2)

      tex2= MathTex(r"\frac{ 1 }{ 1} \times \left( \frac{ 36^ \circ }{ 1 } \right)").move_to(
            text[2][2]).set_color(ORANGE)
      self.play(Transform(text[2][2],tex2 ),run_time=2)

      self.play(FadeOut(text[2][2])) 
      self.play(Write(textEquation[2])) 

      text.append( MathTex(r" = 72^ \circ").move_to(
            text[2][1]).shift( 1.3* DOWN, 0.4*RIGHT)) 
      self.play(Write(text[3]),run_time=4)
      self.wait(2)