from manim import *

class C4_Q2_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("2.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{x^2-2x+1}","=","2").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)

      text.append(MathTex("x^2-2x+1","=","2^2").move_to(text[1]).shift(DOWN))
      text[2][2].set_color(ORANGE)
      self.play(Write(text[2]),run_time=3)
      self.wait(1)

      textAnimate.append( MathTex("4").move_to(text[2][2]))
      self.play(Transform(text[2][2], textAnimate[0]),run_time=1)
      self.wait(2)

      textCopy.append(text[2].copy())
      textAnimate.append(MathTex("- 4").move_to(text[2][2]).shift(1.5*LEFT))
      self.play(
            text[2][0].animate.shift(1.2*LEFT),
            Transform(text[2][2], textAnimate[1]),run_time=3
            ) 
      self.wait()
      self.play(FadeOut(text[2]))
      self.add(textCopy[0])

      text.append(MathTex("x^2+x-3","=","0").move_to(textCopy[0]).shift(DOWN))
      self.play(
        LaggedStart(*[ FadeInFrom(text[3], direction=UP)]),run_time=2
      )
      self.wait()

      text.append(MathTex("(x-3)","(x+1)","=","0").move_to(text[3]).shift(DOWN))
      self.play(Write(text[4]),run_time=5)
      self.wait()

      text.append(MathTex("(x-3)","=","0").move_to(text[4]).shift(DOWN,LEFT))
      self.play(Write(text[5]),run_time=2)
      self.wait()

      text.append(Text("或").move_to(text[4]).shift(DOWN,1.5*RIGHT))
      self.play(Write(text[6]),run_time=1.5)
      self.wait()

      text.append(MathTex("(x+1)","=","0").move_to(text[4]).shift(DOWN,3.8* RIGHT))
      self.play(Write(text[7]),run_time=2)
      self.wait()

      text.append(MathTex("x","=","3").move_to(text[5]).shift(DOWN))
      self.play(Write(text[8]),run_time=2)
      self.wait()

      text.append(MathTex("x","=","-1").move_to(text[7]).shift(DOWN))
      self.play(Write(text[9]),run_time=2)
      self.wait(2)
