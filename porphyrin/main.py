#! /usr/bin/env python3

import os

import organ as ORGAN
import stem as STEM
import leaflet as LEAFLET
import caution as CAUTION

def make(relative_in, relative_out):
   EXTENSION = ".ppr"
   folder_this = os.path.dirname(__file__)
   folder_in = os.path.join(folder_this, relative_in)
   folder_out = os.path.join(folder_this, relative_out)
   things_in = os.scandir(folder_in)

   for thing in things_in:
      if not thing.is_file():
         print("Warning")
         continue
      name_in = thing.name
      if not name_in.endswith(EXTENSION):
         print("Warning")
         continue
      name_out = os.path.join(folder_out, name_in)
      if os.path.isfile(name_out):
         time_in = thing.stat().st_ctime
         time_out = thing.stat().st_ctime
         if time_in < time_out:
            continue
      convert(name_in, name_out) 


'''
   EXTENSION = ".ppr"
   folder_this = os.path.dirname(__file__)
   folder_in = os.path.join(folder_this, folder_relative_in)
   folder_out = os.path.join(folder_this, folder_relative_out)
   names_in = os.fsdecode(os.listdir(folder_in))
   names_out = os.fsdecode(os.listdir(folder_out))
   names_in = sort(names_in)
   names_out = sort(names_out)

   for name_in in names_in:
      if not name_in.endswith(EXTENSION):
         print ("Warning")
      if name_in in names_out:
         time_in = os.path.getmtime(name_in)
         time_out = os.path.getmtime(name_out)
         if time_in < time_out:
            continue
      name_out = os.path.join(folder_out, name_in)
      convert(name_in, name_out) 
'''

def convert(name_in, name_out):
   handle_in = open(name_in, mode = 'r')
   source = handle_in.read()
   handle_in.close()
   document = STEM.Document({"source": source})
   document.parse()
   sink = document.write()
   handle_out = open(name_out, mode = 'w')
   handle_out.write(sink)
   handle_out.close()
