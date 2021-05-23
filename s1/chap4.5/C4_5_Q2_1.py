from manim import *

class C4_5_Q2_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]     

      text.append(MathTex("2.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{ 6", " + ","4\\sqrt{2}","}").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)

      framebox.append(SurroundingRectangle(text[1][2], buff = .1))     
      textAnimate.append(MathTex(r"2 \times ",r"2 ",r"\times",r" \sqrt{2}").move_to(text[1][2]
            ).shift(DOWN).set_color(ORANGE))
      self.play(Create(framebox[0]))     
      self.wait()
      self.play(Write(textAnimate[0]),run_time=3)
      self.wait() 
      textAnimate.append(MathTex(r"2 \times ",r"\sqrt{4} ",r"\times ",r"\sqrt{2}").move_to(
            textAnimate[0]).shift(DOWN,0.2*RIGHT).set_color(ORANGE))
      self.play(Write(textAnimate[1]),run_time=3)
      self.wait() 
      textAnimate.append(MathTex(r"2 \times ",r"\sqrt{8} ").move_to(
            textAnimate[1]).shift(DOWN).set_color(ORANGE))
      self.play(Write(textAnimate[2]),run_time=3)
      self.wait()
      self.play(FadeOut(framebox[0]),FadeOut(textAnimate[0])
            ,FadeOut(textAnimate[1]),FadeOut(textAnimate[2]))
       
      text.append(MathTex(r"= \sqrt{ 6", " + ",r"2 \sqrt{8}","}").move_to(text[1]).shift(DOWN, 0.1*RIGHT))
      self.play(Write(text[2]),run_time=3)
      self.wait()

      text.append(MathTex(r"= \sqrt{ 2+4", " + ",r"2 \sqrt{2 \times 4}","}").move_to(text[2]).shift(DOWN, 0.8*RIGHT))
      self.play(Write(text[3]),run_time=3)
      self.wait()

      text.append(MathTex(r"= \sqrt{ (", r" \sqrt{2} ", " + ",r" \sqrt{4}",r")^2","}").move_to(text[3]).shift(DOWN, 0.5*LEFT))
      self.play(Write(text[4]),run_time=3)
      self.wait()

      text.append(MathTex( r"= \sqrt{2} ", " + ",r" \sqrt{4}").move_to(text[4]).shift(DOWN, 0.58*LEFT))
      self.play(Write(text[5]),run_time=3)
      self.wait()

      text.append(MathTex( r"= \sqrt{2} ", " + ",r" 2").move_to(text[5]).shift(DOWN, 0.28*LEFT).set_color(ORANGE))
      self.play(Write(text[6]),run_time=3)
      self.wait()
      tex1=MathTex( r"= 2", " + ",r" \sqrt{2} ").move_to(text[6]).shift(0*RIGHT)
      self.play(Transform(text[6],tex1 ),run_time=2)
      self.wait()
      # text.append(MathTex(r"= \sqrt{2}", " + ",r"\sqrt{3}").move_to(text[5]).shift(DOWN, 0.7*LEFT))
      # self.play(Write(text[6]),run_time=3)
      # self.wait()

    

  