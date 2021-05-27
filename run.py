#! /usr/bin/env python3

import os

import porphyrin.stem as STEM
import porphyrin.aid as AID

def make(folder_in, folder_out):
   extension_in = ".ppr"
   extension_out = ".txt"
   things_in = os.scandir(folder_in)
   for thing_in in things_in:
      name_in = thing_in.name
      path_in = os.path.join(folder_in, name_in)
      if not thing_in.is_file():
         print(f"Warning: {name_in} is not a file.")
         continue
      if not path_in.endswith(extension_in):
         print(
            f"Warning: file {name_in}",
            f"does not end in \"{extension_in}\".",
         )
         continue
      name_out = name_in.replace(extension_in, extension_out)
      path_out = os.path.join(folder_out, name_out)
      if os.path.isfile(path_out):
         time_in = thing_in.stat().st_ctime
         time_out = os.path.getmtime(path_out)
         if time_in < time_out:
            continue
      print(f"Trying to convert {path_in} to {path_out}:")
      convert(path_in, path_out) 

def convert(path_in, path_out):
   handle_in = open(path_in, mode = 'r')
   source = handle_in.read()
   handle_in.close()
   document = STEM.Document(source = source)
   document.parse()
   sink = document.write()
   handle_out = open(path_out, mode = 'w')
   handle_out.write(sink)
   handle_out.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

subfolder_in = "test-input"
subfolder_out = "test-output"
folder_this = os.path.dirname(__file__)
folder_in = os.path.join(folder_this, subfolder_in)
folder_out = os.path.join(folder_this, subfolder_out)
make(folder_in, folder_out)
