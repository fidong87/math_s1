from manim import *

class C5_2_Q4_1(Scene):
    def construct(self):

      text=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("4.  ").shift(3*UP,6*LEFT))  

      text.append(Text("将").arrange(buff=0.3).shift(3*UP,3.5*LEFT).scale(0.8))
      textEquation.append(MathTex(r"1.35").arrange(buff=0.3).move_to(
            text[1]).shift(1*RIGHT))
      textEquation.append(Text("弧度化为角度。").arrange(
            buff=0.3).move_to(textEquation[0]).shift(3*RIGHT).scale(0.8))
      self.play(Write(text[0]),Write(text[1])
            ,Write(textEquation[0]),Write(textEquation[1]),run_time=4)
      
      text.append( MathTex(r" 1.35 ").arrange(buff=0.3).move_to(text[1]).shift(1.3* DOWN, 0.1*RIGHT)) 
      textAnimate.append( Text("弧度").move_to(text[2]).shift(1.5*RIGHT).scale(0.8)) 
      text.append( MathTex(r"="
            ,r" 1.35 \times \left( \frac{ 180^ \circ}{  \pi } \right)").move_to(
            textAnimate[0]).shift(3*RIGHT))   
      self.play(Write(text[2]),Write(textAnimate[0]),Write(text[3]),run_time=4)
      self.wait(2)     

      text.append( MathTex(r"="
            ,r" 77.3493 ^ \circ").move_to(text[3][1]).shift(1.3* DOWN, 0.95*LEFT)) 
      self.play(Write(text[4]),run_time=2)    
      self.wait(2)

      text.append( MathTex(r"="
            ,r" 77^ \circ 21'").move_to(text[4]).shift(1.3* DOWN, 0.25*LEFT)) 
      self.play(Write(text[5]),run_time=2)    
      self.wait(2)