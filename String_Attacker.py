#create a class 
class Stringattacker():
  def __init__(self):
    self.string1 = "xxxx" #change this
    self.string2 = "5871" #change this
    self.string3 = "1234" #change this
    self.string4 = "1111" #change this
  def Mixer(Word):
    listone=[Word.string1,Word.string2,Word.string3,Word.string4]
    number=0
    global number2
    number2 = 1
    for x in range(len(listone)):
      print(listone[0],end=listone[number]+"\n")
      print(listone[1],end=listone[number]+"\n")
      print(listone[2],end=listone[number]+"\n")
      print(listone[3],end=listone[number]+"\n")
      number+=1
      
Start = Stringattacker()
Start.Mixer()
