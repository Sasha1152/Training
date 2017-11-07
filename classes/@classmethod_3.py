class Hero:

  @staticmethod
  def say_hello():
     print("Helllo...")

  @classmethod
  def say_class_hello(cls):
     if(cls.__name__=="HeroSon"):
        print("Hi Kido")
     elif(cls.__name__=="HeroDaughter"):
        print("Hi Princess")

class HeroSon(Hero):
  def say_son_hello(self):
     print("test  hello")

class HeroDaughter(Hero):
  def say_daughter_hello(self):
     print("test  hello daughter")

testson = HeroSon()
testson.say_class_hello() #Output: "Hi Kido"
testson.say_hello() #Outputs: "Helllo..."
testdaughter = HeroDaughter()
testdaughter.say_class_hello() #Outputs: "Hi Princess"
testdaughter.say_hello() #Outputs: "Helllo..."