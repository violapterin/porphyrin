#! /usr/bin/env python3

import sys

import organ as OG
import stem as S
import leaf as L
import caution as CT

# Stem: Document
# Stem (bough): Section, Stanza, Table, Image, Break,
# Stem (twig): Paragraph, Line, Row,
# Stem (frond): Sentence, Verse, Cell
# Stem (Leaf): Math old, Math new, Monospace
# Leaflet: Serif roman, Serif italic, Serif bold, Sans roman, Sans bold

def convert(filename_in, filename_out):
   file_in = open(filename_in, mode = 'r')
   source = file_in.read()
   file_in.close()
   document = STEM.Document({"source": source})
   document.parse()
   sink = document.write()
   file_out = open(filename_out, mode = 'w')
   file_out.write(sink)
   file_out.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

filename_in = sys.argv[1]
filename_out = sys.argv[2]
convert(filename_in, filename_out)
