#create a class 
class Stringattacker():
  def __init__(self,string1,string2,string3,string4):
    self.string1 = string1 
    self.string2 = string2
    self.string3 = string3
    self.string4 = string4
  def Mixer(Word):
    listone=[Word.string1,Word.string2,Word.string3,Word.string4]
    number=0
    for x in range(len(listone)):
      print(listone[0],end=listone[number]+"\n")
      print(listone[1],end=listone[number]+"\n")
      print(listone[2],end=listone[number]+"\n")
      print(listone[3],end=listone[number]+"\n")
      number+=1
str1=input("Please enter the 1.word:")
str2=input("Please enter the 2.word:")
str3=input("Please enter the 3.word:")
str4=input("please enter the 4.word:")
      
Start = Stringattacker(str1,str2,str3,str4)
Start.Mixer()
