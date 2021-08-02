#! /usr/bin/env python3

import json

import porphyrin.organ as ORGAN
import porphyrin.stem as STEM
import porphyrin.leaf as LEAF
import porphyrin.aid as AID



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

sample_text = (
   "Pneumonoultramicroscopicsilicovolcanoconiosis"
   + ' ' + "is an artificial long word"
   + ' ' + "said to mean a lung disease"
   + ' ' + "caused by inhaling very fine ash and sand dust"
)

sample_code = (
   "char *s=\"char *s=%c%s%c;%cmain(){printf(s,34,s,34,10,10);}%c\";"
   + "main(){printf(s,34,s,34,10,10);}"
)

sample_text_chopped = AID.chop_word_text(sample_text)
sample_code_broken = AID.chop_word_code(sample_code)
print(sample_text_chopped)
print(sample_code_broken)
