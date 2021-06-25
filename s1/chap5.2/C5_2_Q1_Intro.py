from manim import *

class C5_2_Q1_Intro(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]

      textAnimate.append(Text("高一").shift(1*UP))
      self.play(Write(textAnimate[0]) ,run_time=1) 
      text.append(Text("5.2  弧度与角度").move_to(textAnimate[0]).shift(DOWN))
      self.play(Write(text[0]) ,run_time=2) 
      self.wait()
      self.play(FadeOut(textAnimate[0]),FadeOut(text[0]))      
    
      text.append( Text("一周角").move_to(text[0]).shift(3*UP,2.5*LEFT))
      text.append(MathTex(r"= 2 \pi  ").move_to(text[1]).shift( 1.8*RIGHT))
      text.append( Text("弧度").move_to(text[2]).shift(1.3*RIGHT))   
      self.play(Write(text[1]),Write(text[2]),Write(text[3]),run_time=4)
      self.wait()
      text.append(MathTex(r"360 ^ \circ"
            ,r"= 2 \pi  ").move_to(text[1]).shift( DOWN,0*LEFT))
      text.append( Text("弧度").move_to(text[4]).shift(1.9*RIGHT)) 
      self.play(Write(text[4]),Write(text[5]),run_time=4)
      text.append(MathTex(r"180 ^ \circ "
            ,r"=  \pi  ").move_to(text[4]).shift( DOWN,0.1*LEFT))
      text.append( Text("弧度").move_to(text[6]).shift(1.9*RIGHT)) 
      self.play(Write(text[6]),Write(text[7]),run_time=4)
      text.append( Text("1 弧度").move_to(text[6]).shift( DOWN, 0.1*LEFT)) 
      text.append(MathTex(
            r"=  \frac{ 180^ \circ }{\pi} ").move_to(text[8]).shift(2.2*RIGHT))
      self.play(Write(text[8]),Write(text[9]),run_time=4)

      text.append( MathTex(r"\alpha").move_to(text[8]).shift( 1.3* DOWN, 0.8*LEFT)) 
      text.append( Text("弧度").move_to(text[10]).shift(1.3*RIGHT)) 
      text.append(MathTex( r"= \alpha \bullet \left( \frac{ \pi }{ 180^ \circ } \right)").move_to(
            text[11]).shift(2.5*RIGHT))
      text.append( Text("弧度").move_to(text[12]).shift(2.4*RIGHT)) 
      self.play(Write(text[10]),Write(text[11]),Write(text[12]),Write(text[13]),run_time=4)
      self.wait(2)
    
 
