from manim import *

class C4_Q2_3(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("2.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{x^2-2x+1}","=","2").shift(3*UP,1*LEFT))
      self.add(text[0],text[1])

      text.append(Text("当").move_to(text[1]).shift(DOWN,1.5*LEFT))
      self.play(Write(text[2]),run_time=1)
      text.append(MathTex("x = -1").move_to(text[2]).shift(1.3*RIGHT))
      self.play(Write(text[3]),run_time=1)
      self.wait(1)

      text.append(MathTex("\\sqrt{(-1)^2-2(-1)+1}","=","2").move_to(text[2]).shift(DOWN,1.5*RIGHT))
      self.play(Write(text[4]),run_time=4)
      self.wait(1)

      text.append(MathTex("\\sqrt{1+2+1}","=","2").move_to(text[4]).shift(DOWN,1*RIGHT))     
      self.play(Write(text[5]),run_time=3)
      self.wait(1)

      text.append(MathTex("\\sqrt{4}","=","2").move_to(text[5]).shift(DOWN,0.85*RIGHT))     
      self.play(Write(text[6]),run_time=3)
      self.wait(1)

      text.append(MathTex("2","=","2").move_to(text[6]).shift(DOWN,0.2*RIGHT))
      self.play(Write(text[7]),run_time=2)
      self.wait(1)

      text.append(Text("左式 = 右式").move_to(text[7]).shift(DOWN))
      self.play(Write(text[8]))
      self.wait(2)
      self.remove(*[text[i] for i in range(2,len(text))])

      text.append(MathTex("\\sqrt{x^2-2x+1}","=","2").move_to(text[1]).shift(DOWN,3* LEFT))
      self.play(Write(text[9]),run_time=2)
      text.append(Text("的根是").move_to(text[9]).shift(3.6*RIGHT))
      self.play(Write(text[10]),run_time=2)
      text.append(MathTex("x = 3").move_to(text[10]).shift(1.8*RIGHT))
      self.play(Write(text[11]),run_time=1)
      text.append(Text("或").move_to(text[11]).shift(1.3*RIGHT))
      self.play(Write(text[12]),run_time=1)
      text.append(MathTex("x = -1").move_to(text[12]).shift(1.5*RIGHT))
      self.play(Write(text[13]),run_time=1)
      self.wait()