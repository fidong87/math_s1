from manim import *

class C5_1_Q5_Intro2(Scene):
    def construct(self):

      text=[]
      text2=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]

     
      text.append( Text("角度制与弧度制的换算").shift(3*UP))
      self.play(Write(text[0]),run_time=4)
      self.wait()
      text.append( Text("一周角").move_to(text[0]).shift(DOWN,2.2*LEFT))
      text.append(MathTex(r"(360 ^ \circ)   "
            ,r"= \frac{2 \pi r}{r} "
            ,r"= 2 \pi  ").move_to(text[1]).shift( 3.1*RIGHT))
      text.append( Text("弧度").move_to(text[2]).shift(2.9*RIGHT))   
      self.play(Write(text[1]),Write(text[2]),Write(text[3]),run_time=4)
      self.wait()
      text.append(MathTex(r"(360 ^ \circ)   "
            ,r"= 2 \pi  ").move_to(text[1]).shift( DOWN,0*LEFT))
      text.append( Text("弧度").move_to(text[4]).shift(2.5*RIGHT)) 
      self.play(Write(text[4]),Write(text[5]),run_time=4)
      text.append(MathTex(r"(180 ^ \circ)   "
            ,r"=  \pi  ").move_to(text[4]).shift( DOWN,0.1*LEFT))
      text.append( Text("弧度").move_to(text[6]).shift(2.5*RIGHT)) 
      self.play(Write(text[6]),Write(text[7]),run_time=4)
      text.append( Text("1 弧度").move_to(text[6]).shift( DOWN, 0.1*LEFT)) 
      text.append(MathTex(
            r"=  \frac{ 180^ \circ }{\pi} "
            ,r"  \approx 57.30 ^ \circ ").move_to(text[8]).shift(3.5*RIGHT))
      self.play(Write(text[8]),Write(text[9]),run_time=4)

      text.append( MathTex(r"\alpha").move_to(text[8]).shift( 1.3* DOWN, 0.8*LEFT)) 
      text.append( Text("弧度").move_to(text[10]).shift(1.3*RIGHT)) 
      text.append(MathTex( r"= \alpha \bullet \left( \frac{ \pi }{ 180^ \circ } \right)").move_to(
            text[11]).shift(2.7*RIGHT))
      text.append( Text("弧度").move_to(text[12]).shift(2.4*RIGHT)) 
      self.play(Write(text[10]),Write(text[11]),Write(text[12]),Write(text[13]),run_time=4)
      self.wait(2)