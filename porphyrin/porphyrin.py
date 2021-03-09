import rendition-old


class PORPHYRIN:
   set_separation_word = {' ', '\t', '\n', '\r'}
   set_separation_line = {'\n', '\r'}

   # inline
   Tk_space_wide = '_'
   Dlmt_serif_normal = '@'
   Dlmt_serif_italic = '%'
   Dlmt_serif_bold = '#'
   Dlmt_sans_normal = '$'
   Dlmt_sans_bold = '&'
   Dlmt_Rdt_simple = '+'
   Dlmt_Rdt_old = '*'
   Dlmt_Rdt_new = '^'
   Dlmt_comment_left = '<'
   Dlmt_comment_right = '>'
   Dlmt_link = '|'

   # block
   Tk_paragraph = '~'
   Tk_separation = '/'
   Dlmt_image = '\\'
   Dlmt_table_outer = '\"'
   Dlmt_table_inner = '\''

   # block enum
   state_wait = 0
   state_table_1 = 1
   state_table_2 = 2
   state_table_3 = 3
   state_table_4 = 4
   state_paragraph = 5

   # block kind
   kind_paragraph = 0
   kind_separation = 0
   kind_image = 0
   kind_table = 0

   def _init_(S, Dcm_in):
      S.Dcm_in = Dcm_in
      S.Dcm_line = []
      S.Dcm_word = []
      S.slice_in = ""
      S.slice_out = ""
      S.Dcm_out = ""
      S.state = S.state_wait
      S.length = S.Dcm_in.size()
      S.head_left = 0
      S.head_right = 0
      S.sort = S.kind_paragraph

   def run(S):
      while true:
         S.read()
         S.convert()
         if (head_left == S.length): break
         head_left = head_right + 1



