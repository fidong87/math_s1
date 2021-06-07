from manim import *

class C4_5_Q1_Intro(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]

      textAnimate.append(Text("高一").shift(1*UP))
      self.play(Write(textAnimate[0]) ,run_time=1) 
      text.append(Text("4.5  二次不尽根").move_to(textAnimate[0]).shift(DOWN))
      self.play(Write(text[0]) ,run_time=2) 
      self.wait()
      self.play(FadeOut(textAnimate[0]),FadeOut(text[0])) 

     
      text.append(MathTex("(\\sqrt{x} + \\sqrt{y})^2","=","x+y+2\\sqrt{xy}"
            ,",x > 0, y > 0").shift(3*UP))
      self.play(Write(text[1]),run_time=4)
      self.wait()

      text.append(MathTex("\\sqrt{x} + \\sqrt{y}","=","\\sqrt{x+y+2\\sqrt{xy}}"
          ).move_to(text[1]).shift(DOWN))
      self.play(Write(text[2]),run_time=4)
      self.wait()

      text.append(Text("使得").move_to(text[2]).shift(DOWN, 3*LEFT))
      self.play(Write(text[3]) , run_time=2) 
      text.append(MathTex(r"\left\{ \begin{array}{c} a=x+y, \\ b=xy, \end{array}").move_to(text[3]).shift(3*RIGHT))
      self.play(Write(text[4]),run_time=2)
      self.wait()

      text.append(Text("那么").move_to(text[3]).shift(DOWN))
      self.play(Write(text[5]) , run_time=2)
      text.append(MathTex("\\sqrt{a+2\\sqrt{b}} ","=","\\sqrt{x} + \\sqrt{y}}"
          ).move_to(text[5]).shift(3.5*RIGHT))
      self.play(Write(text[6]) , run_time=2)
      self.wait()
      text.append(MathTex("a+2\\sqrt{b}").move_to(text[5]).shift(DOWN, LEFT))
      self.play(Write(text[7]) , run_time=2)
      text.append(Text("的二次不尽根是" ).move_to(text[7]).shift(3.8*RIGHT))
      self.play(Write(text[8]) , run_time=2)
      text.append(MathTex("\\sqrt{x} + \\sqrt{y}}"
          ).move_to(text[8]).shift(3.8*RIGHT))
      self.play(Write(text[9]) , run_time=2)
      self.wait()
     
