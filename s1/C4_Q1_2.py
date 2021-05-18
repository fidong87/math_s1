from manim import *

class C4_Q1_2(Scene):
    def construct(self):

      text=[]
      textCopy=[]
      textAnimate=[]
      framebox=[]
      textEquation=[]
      text.append(MathTex("1.  ").shift(3*UP,6*LEFT))
      text.append(MathTex("\\sqrt{x-1}", " - \\sqrt{x-4}","=","3").shift(3*UP,0.8*LEFT))
      self.add(text[0],text[1])
      self.wait(2)

      text.append(MathTex("x","=", "5").move_to(text[1]).shift(DOWN))
      self.play(Write(text[2])) 
      self.wait(1)

      text.append(Text("检验").move_to(text[2]).shift(DOWN,3*LEFT))
      self.play(Write(text[3])) 
      self.wait()

      text.append(MathTex("\\sqrt{5-1}", " + \\sqrt{5-4}","=","3").move_to(text[3]).shift(4*RIGHT))
      self.play(Write(text[4]))
      self.wait()

      text.append(MathTex("\\sqrt{4}", " + \\sqrt{1}","=","3").move_to(text[4]).shift(DOWN))
      self.play(Write(text[5]))
      self.wait()

      text.append(MathTex("2 + 1","=","3").move_to(text[5]).shift(DOWN))
      self.play(Write(text[6]))
      self.wait()

      text.append(MathTex("3 = 3").move_to(text[6]).shift(DOWN))
      self.play(Write(text[7]))
      self.wait()

      text.append(Text("左式 = 右式").move_to(text[7]).shift(DOWN))
      self.play(Write(text[8]))
      self.wait()
      self.remove(*[text[i] for i in range(2,len(text))])

      text.append(MathTex("\\sqrt{x-1}", " - \\sqrt{x-4}","=","3").move_to(text[1]).shift(DOWN,2* LEFT))
      self.play(Write(text[9]))
      text.append(Text("的根是").move_to(text[9]).shift(3.8*RIGHT))
      self.play(Write(text[10]))
      text.append(MathTex("x = 5").move_to(text[10]).shift(1.8*RIGHT))
      self.play(Write(text[11]))
      self.wait()
   

           
      # text.append(MathTex("\\because \\sqrt{x+1}").move_to(text[0]).shift(DOWN,2*LEFT))
      # text.append(Text("不能是负值").move_to(text[6]).shift(4*RIGHT))
      # self.play(Write(text[6]),Write(text[7]))
      # self.wait(2)
          
      # text.append(MathTex("\\therefore \\sqrt{x-1} - \\sqrt{x+1} ").move_to(text[6]).shift(DOWN,RIGHT))
      # text.append(Text("无解").move_to(text[8]).shift( 3*RIGHT)) 
      # self.play(Write(text[8]),Write(text[9]))
      # self.wait(2)
      # text[6]=MathTex("\\sqrt{x-1} - \\sqrt{x+1} 无解" ).move_to(text[6]).shift(DOWN)
      # self.play(Write(text[6])) 
