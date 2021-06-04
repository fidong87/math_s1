from manim import *

class C4_5_Q4_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("4.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{ 11", " - ","2\\sqrt{18}","}").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]),run_time=5)
      self.wait(2)

      text.append(MathTex(r"\sqrt{ a", " - ",r"2 \sqrt{b}","}").move_to(text[1]).shift(DOWN))
      self.play(Write(text[2]),run_time=5)
      self.wait()        

      text.append(MathTex(r"\sqrt{ x+y", " - ",r"2 \sqrt{x \times y}","}").move_to(text[2]).shift(DOWN))
      self.play(Write(text[3]),run_time=5)
      textAnimate.append(Arrow(np.array([-1.3, 1.7, 0]), np.array([-1.7, 1.05, 0]), buff=0).set_color(RED))    
      self.add(textAnimate[0])
      textAnimate.append(Arrow(np.array([0.3, 1.7, 0]), np.array([0.6, 1.05, 0]), buff=0).set_color(RED) )   
      self.add(textAnimate[1])
      self.wait() 
      self.wait(2)
      self.play(FadeOut(text[2]),FadeOut(text[3])
        ,FadeOut(textAnimate[0]),FadeOut(textAnimate[1])) 

      text.append(MathTex(r"= \sqrt{ 9+2", " - ",r"2 \sqrt{9 \times 2}","}").move_to(text[1]).shift(DOWN, 1*RIGHT))
      self.play(Write(text[4]),run_time=6)
      self.wait()

      text.append(MathTex(r"= \sqrt{ (", r" \sqrt{9} ", " - ",r" \sqrt{2}",r")^2","}").move_to(text[4]).shift(DOWN, 0.51*LEFT))
      self.play(Write(text[5]),run_time=6)
      self.wait()

      text.append(MathTex(r"=",r"\sqrt{9}", " - ",r"\sqrt{2}").move_to(text[5]).shift(DOWN, 0.58*LEFT))
      text[6][1].set_color(ORANGE)
      self.play(Write(text[6]),run_time=5)
      self.wait()

      tex1=MathTex("3").move_to(text[6] ).shift( 0.4*LEFT)
      self.play(Transform(text[6][1],tex1 ),run_time=3)
      self.wait(2)

    

  