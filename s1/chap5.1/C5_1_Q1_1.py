from manim import *

class C5_1_Q1_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("1.  ").shift(3*UP,6*LEFT))
      text.append(Text("2度21分35秒可记作多少秒?",font='Open Sans Regular').shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)



      text.append(MathTex(r"2 ^ \circ ",r" 21' ",r" 35''",r"= ",r" 120'+ 21'"
            ,r"  35''").arrange(buff=0.3).move_to(text[1]).shift(DOWN).scale(1.2))

      text[2][4].set_color(ORANGE)
      self.play(Write(text[2]),run_time=4)
      self.wait()  

      tex1 =  MathTex(r"141'").move_to(text[2][4]).shift(0.6*LEFT).scale(1.2)  
      self.play(Transform(text[2][4],tex1 ), text[2][5].animate.shift(1.3*LEFT),run_time=2)
      self.wait() 

      text.append(MathTex(r"= ",r" 8460'' +   35''").move_to(text[2]).shift(DOWN,1.8*RIGHT).scale(1.2))
      text[3][1].set_color(ORANGE)
      self.play(Write(text[3]),run_time=3)
      self.wait()  

      tex2 =  MathTex(r"8495''").move_to(text[3][1]).shift(0.5*LEFT).scale(1.2)  
      self.play(Transform(text[3][1],tex2 ),run_time=2)
      self.wait()  
