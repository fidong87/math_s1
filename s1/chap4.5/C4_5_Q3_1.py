from manim import *

class C4_5_Q3_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("3.  ").shift(3*UP,6*LEFT))
      text.append(MathTex(r"\sqrt{ 4", " + ",r"\sqrt{15}","}").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)   


      text.append(MathTex(r"= \sqrt{  8 "," +  2",r" \sqrt{15} ",r"\over 2","}").move_to(
            text[1]).shift(1.3*DOWN, 0.5*RIGHT))
      # framebox1 = SurroundingRectangle(text[2][0][2:4], buff = .1)
      # self.play(Create(framebox1))
      self.play(Write(text[2]),run_time=3)
      self.wait()

      text.append(MathTex(r"= \sqrt{  3 ","+ 5 "," +  2",r" \sqrt{ 3 \times 5} "
            ,r"\over 2","}").move_to(text[2]).shift(1.6*DOWN, 0.7*RIGHT))
      self.play(Write(text[3]),run_time=3)
      self.wait()

      text.append(MathTex(r"= \sqrt{ (", r" \sqrt{3} ", " + ",r" \sqrt{5}",r")^2"
            ,r"\over 2","}").move_to(text[3]).shift(1.6*DOWN, 0.5*LEFT))
      self.play(Write(text[4]),run_time=3)
      self.wait()

      text.append(MathTex(r"=\frac{ \sqrt{ (  \sqrt{3} + \sqrt{5} )^2 }} { \sqrt{2}}").move_to(text[4]
            ).shift(1.6*DOWN, 0.05*LEFT).set_color(ORANGE))
      self.play(Write(text[5]),run_time=3)
      self.wait()

      tex1=MathTex(r"=\frac{ \sqrt{3} + \sqrt{5} } { \sqrt{2}}").move_to(text[5]
            ).shift( 0.55*LEFT)
      self.play(Transform(text[5],tex1 ),run_time=2)
      self.wait()      
          
      self.remove(*[text[i] for i in range(2,len(text))])


      text.append(MathTex(r"=\frac{ \sqrt{3}}{ \sqrt{2}}" , r" + \frac{\sqrt{5} } { \sqrt{2}}").move_to(text[2]
            ).shift( 0.4*LEFT).set_color(ORANGE))
      self.play(Write(text[6]),run_time=3)
      self.wait()

      tex2=MathTex(r"=\frac{ \sqrt{3}}{ \sqrt{2}}", r"\times \frac{ \sqrt{2}}{ \sqrt{2}}" 
            , r" + \frac{\sqrt{5} } { \sqrt{2}}"
            , r"\times \frac{ \sqrt{2}}{ \sqrt{2}}" ).move_to(text[2]).shift( 1*RIGHT)
      self.play(Transform(text[6],tex2 ),run_time=2)
      self.wait() 

      text.append(MathTex(r"=\frac{ \sqrt{6}}{ 2}" , r" + \frac{\sqrt{10} } { 2}").move_to(text[6]
            ).shift(1.5*DOWN, 1.34*LEFT).set_color(ORANGE))
      self.play(Write(text[7]),run_time=3)
      self.wait() 

      tex3=MathTex(r"=\frac{ \sqrt{6} + \sqrt{10} } { 2}").move_to(text[7]
            ).shift( 0.07*LEFT)
      self.play(Transform(text[7],tex3 ),run_time=2)
      self.wait(2) 


    
    

  