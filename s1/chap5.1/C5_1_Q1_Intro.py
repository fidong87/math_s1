from manim import *

class C5_1_Q1_Intro(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]

      textAnimate.append(Text("高一").shift(1*UP))
      self.play(Write(textAnimate[0]) ,run_time=1) 
      text.append(Text("5.1  角的定义及单位").move_to(textAnimate[0]).shift(DOWN))
      self.play(Write(text[0]) ,run_time=2) 
      self.wait()
      self.play(FadeOut(textAnimate[0]),FadeOut(text[0])) 

     
      text.append(
        Text("根据角的定义,").shift(3*UP))
      self.play(Write(text[1]),run_time=4)
      self.wait()

      text.append( Text("一个角的大小并不局限于一个周角之内,").move_to(text[1]).shift(DOWN))
      self.play(Write(text[2]),run_time=4)
      self.wait()

      text.append( Text(" 同样的始边与终边可形成无数个不同的角。").move_to(text[2]).shift(DOWN))
      self.play(Write(text[3]),run_time=4)
      self.wait()

      line = Line([-2, -2, 0], [2, 0.5, 0]).set_color(ORANGE)
      line2 = Line([-2, -2, 0], [2, -2, 0]).set_color(ORANGE) 
      self.wait(1)
      curvedArrow= CurvedArrow(0.1*DOWN, 1*LEFT,
        angle=1.2, radius= 1).move_to(line2).shift(0.34*UP,0.9*LEFT).rotate(-60 * DEGREES).scale(0.5)  
      self.add(line, line2,curvedArrow)
      tex = MathTex(r"\theta").move_to(curvedArrow).shift(0.1*UP,0.6*RIGHT).scale(1.2)
      self.play(Write(tex),run_time=0.02)
      curvedArrow2= CurvedArrow(2*UP, 2*RIGHT, 
        angle=3.6*TAU/4).shift(1*UP,0.4*RIGHT).rotate(-46* DEGREES).scale(0.3)  
      self.add(curvedArrow2)
      self.wait(3)

      text.append( Text("O \n 顶点").move_to(curvedArrow).shift(0.6*DOWN,1*LEFT))
      text.append( Text("Q").move_to(line).shift(1*UP,2.5*RIGHT))
      text.append( Text("P").move_to(curvedArrow).shift(0.3*DOWN,3.5*RIGHT))
      self.play(Write(text[4]),Write(text[5]),Write(text[6]),run_time=2)
      self.wait(2)
      text.append( Text("正角").move_to(curvedArrow).shift(0.5*UP,2*RIGHT))
      self.play(Write(text[7]),run_time=2)
      self.wait(1)
      text.append( Text("负角").move_to(line).shift(0*UP,2*LEFT))
      self.play(Write(text[8]),run_time=4)
      self.wait(1)
      text.append( Text("终边").move_to(curvedArrow).shift(1.7*UP,1*RIGHT))
      self.play(Write(text[9]),run_time=2)
      self.wait(1)
      text.append( Text("始边").move_to(curvedArrow).shift(0.8*DOWN,2*RIGHT))
      self.play(Write(text[10]),run_time=4)
      self.wait(1)


    
      # text.append(Text("那么").move_to(text[3]).shift(DOWN))
      # self.play(Write(text[5]) , run_time=2)
      # text.append(MathTex("\\sqrt{a+2\\sqrt{b}} ","=","\\sqrt{x} + \\sqrt{y}}"
      #     ).move_to(text[5]).shift(3.5*RIGHT))
      # self.play(Write(text[6]) , run_time=2)
      # self.wait()
      # text.append(MathTex("a+2\\sqrt{b}").move_to(text[5]).shift(DOWN, LEFT))
      # self.play(Write(text[7]) , run_time=2)
      # text.append(Text("的二次不尽根是" ).move_to(text[7]).shift(3.8*RIGHT))
      # self.play(Write(text[8]) , run_time=2)
      # text.append(MathTex("\\sqrt{x} + \\sqrt{y}}"
      #     ).move_to(text[8]).shift(3.8*RIGHT))
      # self.play(Write(text[9]) , run_time=2)
      # self.wait()
     
