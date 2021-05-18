from manim import *

class C4_Q3_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("3.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{x^2+6x+9}","=","x + 3").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)

      text.append(MathTex("x^2+6x+9","=","(x+3)^2").move_to(text[1]).shift(DOWN,0.5*RIGHT))
      self.play(Write(text[2]),run_time=3)
      self.wait(1)

      textEquation.append(MathTex("(a+ b)^2 = a^2 + 2ab + b^2").move_to(text[2]).shift(DOWN,1.8*RIGHT).set_color(ORANGE))
      self.play(Write(textEquation[0]))
      self.wait(2)
      self.play(FadeOut(textEquation[0])) 

      text.append(MathTex("x^2+6x+9","=","x^2+6x+9").move_to(text[2]).shift(DOWN,0.3*RIGHT))
      self.play(Write(text[3]),run_time=3)
      self.wait(1)

      text.append(MathTex("0x","=","0").move_to(text[3]).shift(DOWN,0.2*LEFT))
      self.play(Write(text[4]),run_time=3)
      self.wait(1)

      text.append(MathTex("x+3","\\geqslant","3").move_to(text[4]).shift(DOWN,2*LEFT))
      self.play(Write(text[5]),run_time=2)
      self.wait(1)

      text.append(Text("令根式有意义").move_to(text[5]).shift(3.3*RIGHT))
      self.play(Write(text[6]))
      self.wait(2)

      text.append(MathTex("\\therefore \\sqrt{x^2+6x+9}","=","x + 3").move_to(text[6]).shift(DOWN,2*LEFT))
      self.play(Write(text[7]),run_time=3)
    
      text.append(Text("的根是").move_to(text[7]).shift(3.8*RIGHT))
      self.play(Write(text[8]),run_time=1.5)

      text.append(MathTex(" x","\\geqslant","-3").move_to(text[8]).shift(2.2*RIGHT))
      self.play(Write(text[9]),run_time=1)
      self.wait(2)
