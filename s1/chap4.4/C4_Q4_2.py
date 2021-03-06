from manim import *

class C4_Q4_2(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      text.append(MathTex("4.  ", "\\sqrt{x-1}", " - \\sqrt{x+1}","=","2").shift(3*UP,0.8*LEFT))
      self.play(Write(text[0]))
      self.play(text[0][0].animate.shift(2*LEFT))
      self.wait(2)

      textC=text[0].copy()
      framebox1 = SurroundingRectangle(text[0][2], buff = .1)      
      textS=MathTex(" + \\sqrt{x+1}").move_to(text[0]).shift(5*RIGHT)
      self.play(Create(framebox1))
      self.play(Transform(text[0][2], textS))
      self.wait(2)
      self.play(FadeOut(framebox1),FadeOut(text[0]))
      self.add(textC) 

      text.append(MathTex("\\sqrt{x-1}","=","2"," + \\sqrt{x+1}").move_to(text[0]).shift(DOWN))
      self.play(Write(text[1]))
      self.wait(2)  

      text.append(MathTex("(\\sqrt{x-1})^2","=","(2 + \\sqrt{x+1})^2").move_to(text[1]).shift(DOWN))
      self.play(Write(text[2]))
      self.wait(2)    

      text.append(MathTex(
          "x","- 1"," = ","4" ,"+ 4\\sqrt{x+1} ","+ x","+ 1"
      ).move_to(text[2]).shift(DOWN))
      textCopy.append(text[3].copy())     
      self.play(Write(text[3]))
      self.wait(2)
      framebox1 = SurroundingRectangle(text[3][0], buff = .1)
      framebox2 = SurroundingRectangle(text[3][5], buff = .1)
      self.play(
          Create(framebox1),Create(framebox2)
      ) 
      self.wait(2)
      
      #self.remove(text[3][0])
      self.play(
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in text[3][5]]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in text[3][0]]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox1]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox2]),
      )
      framebox3 = SurroundingRectangle(text[3][1], buff = .1).set_color(ORANGE)
      framebox4 = SurroundingRectangle(text[3][3], buff = .1).set_color(ORANGE)
      framebox5 = SurroundingRectangle(text[3][6], buff = .1).set_color(ORANGE)
      #framebox5 = SurroundRect_Color(text[3][6],ORANGE)
      self.play(
          Create(framebox3),Create(framebox4),Create(framebox5)
      )
      self.wait(2)
      self.play(
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox5]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox3]),
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in framebox4]),
      )

      tex1=MathTex(" - 4").shift(5*LEFT)
      tex2=MathTex(" - 1").shift(4*LEFT)
      self.play(Transform(text[3][3],tex1 ),Transform(text[3][6],tex2 ))
      self.wait(2)

      text.append(MathTex("-6","=",  "4","\\sqrt{x+1}").move_to(textCopy[0]).shift(DOWN))    
      self.play(
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in text[3]]),
      )
      self.add(textCopy[0])
      self.play(Write(text[4]))

      textCopy.append(text[4].copy())
      tex4=MathTex("\\overline{4}").move_to(textCopy[1]).shift(1.2*LEFT,0.5*DOWN)
      self.wait(2)
      self.play(Transform(text[4][2],tex4 ))  
      tex3=MathTex("\\frac{-6}{4}").move_to(textCopy[1]).shift(2*LEFT)
      self.play(    
        LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in  text[4][2]]),
        Transform(text[4][0],tex3 )
      )
      self.wait(2)
      self.remove(*[text[4][i] for i in range(0,len(text[4]))])
      self.wait()

      text.append(MathTex("\\sqrt{x+1}","=", "-\\frac{3}{2}").move_to(textCopy[1]).shift(DOWN))     
      self.add(textCopy[1])
      self.play(Write(text[5])) 
      self.wait(2)

      tex5 =text[5];#a * (self.remove(*diffHooks))
      self.remove(*[textCopy[i] for i in range(0,len(textCopy))])     
      self.remove(*[text[i] for i in range(0,len(text))])

           
      text.append(MathTex("\\because \\sqrt{x+1}").move_to(text[0]).shift(DOWN,2*LEFT))
      text.append(Text("???????????????").move_to(text[6]).shift(4*RIGHT))
      self.play(Write(text[6]),Write(text[7]))
      self.wait(2)
          
      text.append(MathTex("\\therefore \\sqrt{x-1} - \\sqrt{x+1} ").move_to(text[6]).shift(DOWN,RIGHT))
      text.append(Text("??????").move_to(text[8]).shift( 3*RIGHT)) 
      self.play(Write(text[8]),Write(text[9]))
      self.wait(2)
      # text[6]=MathTex("\\sqrt{x-1} - \\sqrt{x+1} ??????" ).move_to(text[6]).shift(DOWN)
      # self.play(Write(text[6])) 
