from manim import *

class C4_5_Q6_1(Scene):
    def construct(self):

      text=[]
      textAnimate=[]
      text.append(MathTex("6.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{ 17", " - ","12\\sqrt{2}","}").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]),run_time=5)
      self.wait(2)
   
      text.append(MathTex(r"= \sqrt{  17 "," -  2",r" \times"," 6",r" \sqrt{2} ","}").move_to(
            text[1]).shift(1.3*DOWN, 0.4*RIGHT).set_color(RED))     
      self.play(Write(text[2]),run_time=6)
      self.wait()

      tex1=MathTex(r"= \sqrt{  17 "," -  2",r" \times",r" \sqrt{36}",r" \times"r" \sqrt{2} ","}").move_to(
            text[1]).shift(1.3*DOWN, 1*RIGHT).set_color(ORANGE)     
      self.play(Transform(text[2],tex1 ),run_time=5)
      self.wait() 

      tex2=MathTex(r"= \sqrt{  17 "," -  2",r" \sqrt{72} ","}").move_to(text[2]
            ).shift( 0.95*LEFT)
      self.play(Transform(text[2],tex2 ),run_time=5)
      self.wait()

      text.append(MathTex(r"= \sqrt{  9 + 8 "," -  2",r" \sqrt{ 9 \times 8} ","}"
            ).move_to(text[2]).shift(1.6*DOWN, 0.55*RIGHT))
      self.play(Write(text[3]),run_time=5)
      self.wait()

      text.append(MathTex(r"= \sqrt{ (", r" \sqrt{9} ", " - ",r" \sqrt{8}",r")^2"
            ,"}").move_to(text[3]).shift(1.6*DOWN, 0.5*LEFT))
      self.play(Write(text[4]),run_time=5)
      self.wait()

      text.append(MathTex(r"=  ", r" \sqrt{9} ", " - ",r" \sqrt{8}"
            ).move_to(text[4]).shift(1.6*DOWN, 0.6*LEFT))
      self.play(Write(text[5]),run_time=5)
      self.wait()

      self.remove(*[text[i] for i in range(2,len(text))])

      text.append(MathTex(r"=  ", r" 3 ", " - ",r" \sqrt{4 \times 2}"
            ).move_to(text[1]).shift(1.6*DOWN, 0.1*RIGHT))
      text[6][3].set_color(ORANGE);
      self.play(Write(text[6]),run_time=5)
      self.wait()

      tex3=MathTex(r" \sqrt{4} \times \sqrt{2}").move_to(text[6][3]
            ).shift( 0.3*RIGHT).set_color(ORANGE)
      self.play(Transform(text[6][3],tex3 ),run_time=4)
      self.wait()

      tex4=MathTex(r" 2  \sqrt{2}").move_to(text[6][3]
            ).shift( 0.5*LEFT)
      self.play(Transform(text[6][3],tex4 ),run_time=4)
      self.wait()

    

  