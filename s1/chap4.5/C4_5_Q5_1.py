from manim import *

class C4_5_Q5_1(Scene):
    def construct(self):

      text=[]    
      text.append(MathTex("5.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{ 6", " - ","\\sqrt{11}","}").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]),run_time=4)
      self.wait(2)

      text.append(MathTex(r"= \sqrt{  12 "," -  2",r" \sqrt{11} ",r"\over 2","}").move_to(
            text[1]).shift(1.3*DOWN, 0.5*RIGHT))     
      self.play(Write(text[2]),run_time=5)
      self.wait()

      text.append(MathTex(r"= \sqrt{  11 ","+ 1 "," -  2",r" \sqrt{ 11 \times 1} "
            ,r"\over 2","}").move_to(text[2]).shift(1.6*DOWN, 0.8*RIGHT))
      self.play(Write(text[3]),run_time=6)
      self.wait()


      text.append(MathTex(r"= \sqrt{ (", r" \sqrt{11} ", " - ",r" \sqrt{1}",r")^2"
            ,r"\over 2","}").move_to(text[3]).shift(1.6*DOWN, 0.6*LEFT))
      self.play(Write(text[4]),run_time=6)
      self.wait()

      text.append(MathTex(r"=\frac{ \sqrt{ (  \sqrt{11} - \sqrt{1} )^2 }} { \sqrt{2}}").move_to(text[4]
            ).shift(1.6*DOWN, 0.07*LEFT).set_color(ORANGE))
      self.play(Write(text[5]),run_time=5)
      self.wait()

      tex1=MathTex(r"=\frac{  \sqrt{11} - \sqrt{1} } { \sqrt{2}}").move_to(text[5]
            ).shift( 0.55*LEFT)
      self.play(Transform(text[5],tex1 ),run_time=5)
      self.wait()      
          
      self.remove(*[text[i] for i in range(2,len(text))])
    
      text.append(MathTex(r"=\frac{ \sqrt{11}}{ \sqrt{2}}" , r" - \frac{\sqrt{1} } { \sqrt{2}}").move_to(text[2]
            ).shift( 0.4*LEFT).set_color(ORANGE))
      self.play(Write(text[6]),run_time=5)
      self.wait()

      tex2=MathTex(r"=\frac{ \sqrt{11}}{ \sqrt{2}}", r"\times \frac{ \sqrt{2}}{ \sqrt{2}}" 
            , r" + \frac{\sqrt{1} } { \sqrt{2}}"
            , r"\times \frac{ \sqrt{2}}{ \sqrt{2}}" ).move_to(text[2]).shift( 0.8*RIGHT)
      self.play(Transform(text[6],tex2 ),run_time=5)
      self.wait() 

      text.append(MathTex(r"=\frac{ \sqrt{22}}{ 2}" , r" + \frac{\sqrt{2} } { 2}").move_to(text[6]
            ).shift(1.5*DOWN, 1.4*LEFT).set_color(ORANGE))
      self.play(Write(text[7]),run_time=5)
      self.wait() 

      tex3=MathTex(r"=\frac{ \sqrt{22} + \sqrt{2} } { 2}").move_to(text[7]
            ).shift( 0.07*LEFT)
      self.play(Transform(text[7],tex3 ),run_time=2)
      self.wait(2) 

  