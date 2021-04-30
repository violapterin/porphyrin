import organ
import stem
import leaflet
import error

class Leaflet(tissue.Stem):

   def parse(self):
      while not self.source:
         self.element, self.mark = self.snip()
         label = get_label_from_mark(mark)
         fragment_left = self.find_fragment_left()
         fragment_right = self.find_fragment_right()
         data = {
             "place" : self.place,
             "fragment_left" : fragment_left,
             "mark" : mark,
             "fragment_right" : fragment_right
         }
         if (be_leaf_label(label)):
             error.outer_scope_leaf(**data)
         if (label == "serif-roman"):
            leaf = Serif_roman()
         elif (label == "serif-italic"):
            label = Serif_italic
         elif (label == "serif-bold"):
            label = Serif_bold
         elif (label == "sans-normal"):
            label = Sans_normal
         elif (label == "sans-bold"):
            label = Sans_bold
         # ...

         self.push(leaf)

   def write(self):
      pass

   def write_tag(self, element, kind):
      result = ''
      result += "<span" + ' '
      result += "class=" + kind + ">"
      for leaf in self.sink:
         result += leaf.write()
      result += "<span" + "/>"
      return result

'''
   def write_comment(self, element):
      result = ''
      result += "<!-- "
      for leaf in self.sink:
         result += leaf.write()
      result += " -->"
      return result
'''

   def tune_text(source):
      result = ignore_mark_text(source)
      result = adjust_space(result)
      return result

   def tune_code(source):
      result = adjust_space(source)
      return result

   def adjust_space(source):
      spaces = {'\n', '\t'}
      result = erase_character(source, spaces)
      result = ' '.join(result.split())
      return result

   def ignore_mark_text(source):
      marks_ignored = {'<', '>', '@', '#', '$', '%', '&'}
      result = erase_character(source, marks_ignored)
      return result

   def remove_character(source, group):
      for symbol in group:
         source = source.translate(source.maketrans(symbol: ''))
      return source

   def erase_character(source, group):
      for symbol in group:
         source = source.translate(source.maketrans(symbol: ' '))
      return source

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Serif_roman(Leaflet):

   def __init__(self, **data):
      self.source = data.pop("source", ''),
      self.place = data.pop("place", Place())
      self.leftmost = data.pop("fragment_left", '')
      self.rightmost = data.pop("fragment_right", '')
      self.content = ''
      self.head = 0

   def parse(self):
      content = self.source
      self.content = self.tune_text(content)

   def write(self):
      return self.write_tag(self.content, "serif-roman"):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Serif_italic(Leaflet):

   def __init__(self, **data):
      self.source = data.pop("source", ''),
      self.place = data.pop("place", Place())
      self.leftmost = data.pop("fragment_left", '')
      self.rightmost = data.pop("fragment_right", '')
      self.content = ''
      self.head = 0

   def parse(self):
      content = self.source
      self.content = self.tune_text(content)

   def write(self):
      return self.write_tag(self.content, "serif-italic"):

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Serif_bold(Leaflet):

   def __init__(self, **data):
      self.source = data.pop("source", ''),
      self.place = data.pop("place", Place())
      self.leftmost = data.pop("fragment_left", '')
      self.rightmost = data.pop("fragment_right", '')
      self.content = ''
      self.head = 0

   def parse(self):
      content = self.source
      self.content = self.tune_text(content)

   def write(self):
      return self.write_tag(self.content, "serif-bold"):


