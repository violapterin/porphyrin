#! /usr/bin/env python3

'''
import organ as ORGAN
import stem as STEM
import leaf as LEAF
import tissue as TISSUE
import caution as CAUTION
import aid as AID
'''

class Flower(object):
   def __init__(self, color):
      self.color = color
   
   class Leaf(object):
   

''
class Cat():
   KIND = "cat"
   def __init__(self, color):
      self.color = color
   def call(self):
      print("meow")
   def copy(self):
      return Cat(self.color)

class Dog():
   KIND = "dog"
   def __init__(self, color):
      self.color = color
   def call(self):
      print("bark")

class Bird():
   def __init__(self, **args):
      self.a = args.pop("a", 0)
      self.b = args.pop("b", 0)
'''

