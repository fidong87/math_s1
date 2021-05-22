from manim import *

class C4_5_Q1_1(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("1.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{x-1}", " - \\sqrt{x-4}","=","3").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(Write(text[1]))
      self.wait(2)

      textCopy.append(text[1].copy())
      framebox.append(SurroundingRectangle(text[1][1], buff = .1))     
      textAnimate.append(MathTex(" + \\sqrt{x-4}").move_to(text[1][1]).shift(3*RIGHT))
      self.play(Create(framebox[0]))
      self.play(FadeOut(framebox[0]),Transform(text[1][1], textAnimate[0]))
      self.wait(2)
      self.play(FadeOut(text[1]))
      self.add(textCopy[0])
      self.wait(1)

      text.append(MathTex("\\sqrt{x-1}","=","3"," + \\sqrt{x-4}").move_to(text[1]).shift(DOWN,0.9*LEFT))
      self.play(Write(text[2]))
      self.wait(2)  

      text.append(MathTex("(\\sqrt{x-1})^2","=","(3 + \\sqrt{x-4})^2").move_to(text[2]).shift(DOWN,0.1*RIGHT))
      self.play(Write(text[3]))
      self.wait(2)

      textEquation.append(MathTex("(a+ b)^2 = a^2 + 2ab + b^2").move_to(text[3]).shift(DOWN,1.5*RIGHT).set_color(ORANGE))
      self.play(Write(textEquation[0]))
      self.wait(2)
      self.play(FadeOut(textEquation[0]))     

      text.append(MathTex(
          "x","- 1"," = ","9" ,"+ 6\\sqrt{x-4} ","+ x","- 4"
      ).move_to(text[3]).shift(DOWN))
      textCopy.append(text[4].copy())     
      self.play(Write(text[4]))
      self.wait(2)
      framebox.append(SurroundingRectangle(text[4][0], buff = .1))
      framebox.append(SurroundingRectangle(text[4][5], buff = .1))
      self.play(
          Create(framebox[1]),Create(framebox[2])
      ) 
      self.wait(2)
      self.play(
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in text[4][5]]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in text[4][0]]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox[1]]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox[2]]),
      )
      framebox.append(SurroundingRectangle(text[4][1], buff = .1).set_color(ORANGE))
      framebox.append(SurroundingRectangle(text[4][3], buff = .1).set_color(ORANGE))
      framebox.append(SurroundingRectangle(text[4][6], buff = .1).set_color(ORANGE))    
      self.play(
          Create(framebox[3]),Create(framebox[4]),Create(framebox[5])
      )
      self.wait(2)
      self.play(
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox[3]]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox[4]]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox[5]]),
      )

      tex1=MathTex(" - 9").shift(5*LEFT)
      tex2=MathTex(" + 4").shift(4*LEFT)
      self.play(Transform(text[4][3],tex1 ),Transform(text[4][6],tex2 ))
      self.wait(2)

      text.append(MathTex( "6","\\sqrt{x-4}","=","6" ).move_to(textCopy[1]).shift(DOWN))    
      self.play(
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in text[4]]),
      )
      self.add(textCopy[1])
      self.play(Write(text[5]))

      textCopy.append(text[5].copy())
      tex4=MathTex("\\overline{6}").move_to(textCopy[2]).shift(1.2*RIGHT,0.5*DOWN)
      self.wait(2)
      self.play(Transform(text[5][0],tex4 ))  
      tex3=MathTex("\\frac{6}{6}").move_to(textCopy[2]).shift(1.5*RIGHT)
      self.play(    
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in  text[5][0]]),
        Transform(text[5][3],tex3 )
      )
      self.wait(2)
      self.remove(*[text[5][i] for i in range(0,len(text[5]))])
      self.wait()

      text.append(MathTex("\\sqrt{x-4}","=", "1").move_to(textCopy[2]).shift(DOWN))     
      self.add(textCopy[2])
      self.play(Write(text[6])) 
      self.wait(2)

      text.append(MathTex("x-4","=", "1^2").move_to(text[6]).shift(DOWN).set_color(ORANGE)) 
      self.play(Write(text[7])) 
      self.wait(1)
      tex4=MathTex("x-4","=", "1").move_to(text[7])
      self.play(   
        Transform(text[7],tex4 )
      )
      self.wait(1)

      # textCopy.append(text[7]);
      # self.remove(*[textCopy[i] for i in range(1,len(textCopy))])     
      # self.remove(*[text[i] for i in range(1,len(text))])
      # self.wait(1)
