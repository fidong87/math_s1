from manim import *


class C5_1_Q5_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("5.  ").shift(3*UP,6*LEFT).scale(1))  
      self.play(Write(text[0]))    
      self.wait(2)

      text.append(MathTex(r"\angle QOP ",r"= ",r" \frac{1.5}{5}",r" = 0.3").move_to(
            text[0]).shift(DOWN,4*RIGHT).scale(1))
      text.append( Text(" 弧度").move_to(text[1]).shift(3.5*RIGHT))
      self.play(Write(text[1]),Write(text[2]),run_time=3)
      self.wait()  

      text.append(MathTex(r"\angle POS ",r"= ",r" \frac{9}{5}",r" = 1.8").move_to(
            text[1]).shift(1.5*DOWN).scale(1))
      text.append( Text(" 弧度").move_to(text[3]).shift(3.5*RIGHT))
      self.play(Write(text[3]),Write(text[4]),run_time=3)
      self.wait()  

      text.append(MathTex(r"\angle SOR ",r"= ",r" \frac{17}{5}",r" = 3.4").move_to(
            text[3]).shift(1.5*DOWN).scale(1))
      text.append( Text(" 弧度").move_to(text[5]).shift(3.5*RIGHT))
      self.play(Write(text[5]),Write(text[6]),run_time=3)
      self.wait() 

      text.append(MathTex(r"\angle QOR ",r"= 6.284 -",r"  \angle QOP-\angle POS-\angle SOR"
            ).move_to(
            text[5]).shift(1.2*DOWN,2*RIGHT).scale(1))
      text.append( Text(" 弧度").move_to(text[7]).shift(5.5*RIGHT))
      self.play(Write(text[7]),Write(text[8]),run_time=3)
      self.wait()

     
      tex=  MathTex(r" 0.3 - 1.8 - 3.4" ).move_to(text[7][2]).shift(0.02*UP ,1.2*LEFT).scale(1)
      self.play( text[8].animate.shift(1.5*LEFT),Transform(text[7][2],tex ),run_time=2)
      self.wait() 

      text.append(MathTex(r"=0.784" ).move_to(
            text[7][2]).shift(1.2*DOWN,3.1*LEFT).scale(1))
      text.append( Text(" 弧度").move_to(text[9]).shift(2*RIGHT))
      self.play(Write(text[9]),Write(text[10]),run_time=3)
      self.wait()