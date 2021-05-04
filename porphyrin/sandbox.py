#! /usr/bin/env python3

import organ as OG
import stem as S
import leaf as L
import caution as CT

class Cat():
   kind = "cat"
   def __init__(self, color):
      self.color = color
   def call(self):
      print("meow")
   def copy(self):
      return Cat(self.color)

class Dog():
   kind = "dog"
   def __init__(self, color):
      self.color = color
   def call(self):
      print("bark")

class Bird():
   def __init__(self, **args):
      self.a = args.pop("a", 0)
      self.b = args.pop("b", 0)

c = Cat("black")
d = c.copy()
print (d.color)

'''
c1 = Bird(a=3,b=5)
kw = {"a":3, "b":5}
c2 = Bird(**kw)
print(c1.a)
print(c2.a)
'''


'''
str = "Cat"
c = (eval(str))("red")
c.call()
'''

'''
s1 = "apple , banana , cake"
s2 = ", banana , cake"
s3 = ","
s4 = "apple ,, banana , cake"

t1 = "@@ apple @ banana @@ cake"
t2 = "@@ apple @ banana @@ cake"
t3 = "apple @@ banana , cake"

print (s1.split(','))
print (s2.split(','))
print (s3.split(','))
print (s4.split(','))
print (t1.split('@'))
print (t2.split('@@'))
print (t3.split('@@'))
'''

