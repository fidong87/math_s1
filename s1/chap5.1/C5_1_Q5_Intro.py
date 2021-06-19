from manim import *

class C5_1_Q5_Intro(Scene):
    def construct(self):

      text=[]
      text2=[]
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
        Text("弧度制（Radian Measure)").shift(3*UP))
      self.play(Write(text[1]),run_time=4)
      self.wait()

      text.append( Text("1 弧度").move_to(text[1]).shift(1.5*DOWN,4*LEFT))
      self.play(Write(text[2]),run_time=4)
      self.wait()

      text.append(MathTex(r"= ",r"\frac{r}{r}").move_to(text[1]).shift(1.5*DOWN,2*LEFT).scale(1.2))
      self.play(Write(text[3]),run_time=3)
      self.wait()

      center=np.array([2, 0, 0])
      circle = Circle(radius=2, color=BLUE).move_to(center)
      self.add(circle)


      line = Line(center, circle.point_from_proportion(0)).set_color(ORANGE)
      line2 = Line(center ,circle.point_from_proportion(0.15)).set_color(ORANGE)         
      self.add(line,line2 )
      self.wait(3) 
      a = Angle(line, line2, radius=0.5, other_angle=False).set_color(ORANGE) 
      # tex = MathTex(r"\theta").move_to(
      #       Angle(
      #           line, line2, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
      #       ).point_from_proportion(0.5)
      #   )
      self.add(a
            #, tex 
             )

      text.append(  Text("1 弧度").arrange(
            buff=0.2).move_to(line).shift(0.5*UP, 0.3*RIGHT).scale(0.5))
      text.append(  MathTex(r"r").move_to(line).shift(0.3* DOWN, 0.1*RIGHT))
      text.append(  MathTex(r"r").move_to(line2).shift(0.1*UP, 1.5*RIGHT))
      self.play(Write(text[4]), Write(text[5]), Write(text[6]),run_time=3)
      self.wait()

  
      textAnimate.append( MathTex(r"\theta").move_to(text[2][0]))
      textAnimate.append(MathTex(r"\frac{l}{r}").move_to(text[3][1]))
      textAnimate.append( MathTex(r"\theta").move_to(text[4][0]).scale(0.7))
      self.play(Transform(text[2][0],textAnimate[1] ),
            Transform(text[3][1],textAnimate[2] ),
            Transform(text[4][0],textAnimate[3] )
                  ,run_time=4)
      self.wait(2)

      # tex5 = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex).scale(3)
      # self.add(tex5)
      text.append(  Text("半径为").arrange(
            buff=0.2).move_to(text[2]).shift(1*DOWN, 1*LEFT).scale(0.5))
      text2.append(  MathTex(r"r").arrange(
            buff=0.2).move_to(text[7]).shift( 0.8*RIGHT).scale(0.9))
      text2.append(Text("的圆的圆心角").arrange(
            buff=0.2).move_to(text2[0]).shift( 1.3*RIGHT).scale(0.5))

      text2.append(MathTex(r"\alpha").arrange(
            buff=0.2).move_to(text2[1]).shift( 1.4*RIGHT).scale(0.9))


      self.play(Write(text[7]),
            Write(text2[0]),Write(text2[1]),Write(text2[2]) ,run_time=3)

      text.append(  Text("所对的弧度长为").arrange(
            buff=0.2).move_to(text[7]).shift(0.5*DOWN, 0.8*RIGHT).scale(0.5))
      textAnimate.append(MathTex(r"l").move_to(text[8]).shift(1.6*RIGHT).scale(0.9))  
      text.append(  Text("那么角 ").arrange(
            buff=0.2).move_to(text[8]).shift(0.5*DOWN, 0.84*LEFT).scale(0.5))
      self.play(Write(text[8]),Write(textAnimate[4])
            ,run_time=3)
      text2.append(MathTex(r"\alpha").arrange(
            buff=0.2).move_to(text[9]).shift( 0.8*RIGHT).scale(0.9))
      text2.append(Text("的弧度数的绝对值是").arrange(
            buff=0.2).move_to(text2[3]).shift( 2.1*RIGHT).scale(0.5))
      self.play( Write(text[9]) ,Write(text2[3]),Write(text2[4]),run_time=3)
      text.append(MathTex(r"|\alpha| = \frac{l}{r}").move_to(text[9]).shift(0.9*DOWN, 0.3*RIGHT).scale(0.9)) 

      self.play(Write(text[10]),run_time=3)
      self.wait(2)