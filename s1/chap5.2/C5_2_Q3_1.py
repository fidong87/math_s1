from manim import *

class C5_2_Q3_1(Scene):
    def construct(self):

      text=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("3.  ").shift(3*UP,6*LEFT))
      text.append(Text("将").arrange(
            buff=0.3).shift(3*UP,5*LEFT).scale(0.8))
      textEquation.append(MathTex(r"45 ^\circ 50' ").arrange(buff=0.3).move_to(
            text[1]).shift(1.1*RIGHT))
      textEquation.append(Text("化为弧度（答案准确至四位小数)").arrange(
            buff=0.3).move_to(textEquation[0]).shift(5.8*RIGHT).scale(0.8))    
      self.play(Write(text[0]))
      self.play(Write(text[1]),Write(textEquation[0])
            ,Write(textEquation[1]))
      self.wait(2)
      

      text.append( MathTex(r"45 ^\circ 50' ",r"="
            ,r"45 ^\circ \frac{ 50 }{ 60} \times \left( \frac{ \pi }{ 180^ \circ } \right)").move_to(
            text[1]).shift( 1.3* DOWN, 3.5*RIGHT)) 
      text.append( Text("弧度").move_to(text[2]).shift(3.5*RIGHT).scale(0.8)) 
      self.play(Write(text[2]),Write(text[3]),run_time=4)
      self.wait(2)

      text.append( MathTex(r"="
            ,r" \frac{ 45 ^\circ \times 60 + 50 }{ 60} \times \left( \frac{ \pi }{ 180^ \circ } \right)").move_to(
            text[2][2]).shift( 1.3* DOWN, 0.6*RIGHT)) 
      text.append( Text("弧度").move_to(text[4]).shift(3.8*RIGHT).scale(0.8)) 
      text[4][1].set_color(ORANGE)
      self.play(Write(text[4]),Write(text[5]),run_time=4)
      self.wait(2)
     
      tex= MathTex(r" 0.7999").move_to(text[4][1]).shift(2*LEFT) 
      self.play(Transform(text[4][1],tex ),text[5].animate.shift(3.8*LEFT),run_time=2)    
      self.wait(2)