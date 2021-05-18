from manim import *

class C4_Q2_2(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("1.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{x^2-2x+1}","=","2").shift(3*UP,1*LEFT))
      self.add(text[0],text[1])

      text.append(Text("当").move_to(text[1]).shift(DOWN,1.5*LEFT))
      self.play(Write(text[2]),run_time=1)
      text.append(MathTex("x = 3").move_to(text[2]).shift(1.3*RIGHT))
      self.play(Write(text[3]),run_time=1)
      self.wait(1)

      text.append(MathTex("\\sqrt{(3)^2-2(3)+1}","=","2").move_to(text[2]).shift(DOWN,1.5*RIGHT))
      self.play(Write(text[4]),run_time=4)
      self.wait(1)

      text.append(MathTex("\\sqrt{9-6+1}","=","2").move_to(text[4]).shift(DOWN,0.65*RIGHT))     
      self.play(Write(text[5]),run_time=3)
      self.wait(1)

      text.append(MathTex("2","=","2").move_to(text[5]).shift(DOWN,1.05*RIGHT))
      self.play(Write(text[6]),run_time=2)
      self.wait(1)

      text.append(Text("左式 = 右式").move_to(text[6]).shift(DOWN))
      self.play(Write(text[7]))
      self.wait()

       