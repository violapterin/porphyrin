#! /usr/bin/env python3

import sys

import organ
import stem
import leaf
import leaflet
import caution

# Document
# Section, Stanza, Table, Image, Break,
# Paragraph, Line, Row,
# Sentence, Verse, Cell
# Serif roman, Serif italic, Serif bold, Sans roman, Sans bold
# Math old, Math new, Monospace

def convert(filename_in, filename_out):
   file_in = open(filename_in, mode = 'r')
   source = file_in.read()
   file_in.close()
   document = stem.Document({"source": source})
   document.parse()
   sink = document.write()
   file_out = open(filename_out, mode = 'w')
   file_out.write(sink)
   file_out.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

filename_in = sys.argv[1]
filename_out = sys.argv[2]
convert(filename_in, filename_out)