import branch
import twig
import leaf
import main


def not_recognized_mark_branch(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   mark = arguments.pop(mark, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = "Token"
   message_right = "is not a branch opening mark."
   warn(
         place = place,
         fragment_left = fragment_left,
         fragment_right = fragment_right,
         message_left = message_left,
         message_right = message_right)


def warn_not_matched_mark_branch(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   mark = arguments.pop(mark, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = "Branch opening mark"
   message_right = "is not matched."
   warn(
         place = place,
         fragment_left = fragment_left,
         fragment_right = fragment_right,
         message_left = message_left,
         message_right = message_right)
   cease()


def warn_not_recognized_mark_leaf(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   mark = arguments.pop(mark, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = "Token"
   message_right = "is not an leaf opening mark."
   warn(
         place = place,
         fragment_left = fragment_left,
         fragment_right = fragment_right,
         message_left = message_left,
         message_right = message_right)
   cease()

def warn_not_matched_mark_leaf(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   mark = arguments.pop(mark, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = "Leaf opening mark"
   message_right = "is not matched."
   warn(
         place = place,
         fragment_left = fragment_left,
         fragment_right = fragment_right,
         message_left = message_left,
         message_right = message_right)

def warn_outer_scope_leaf(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   mark = arguments.pop(mark, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = "Leaf"
   message_right = "cannot occur in the outer scope."
   warn(
         place = place,
         fragment_left = fragment_left,
         fragment_right = fragment_right,
         message_left = message_left,
         message_right = message_right)

def warn_inner_scope_branch(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   mark = arguments.pop(mark, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = "Branch"
   message_right = "cannot occur in the outer scope."
   warn(
         place = place,
         fragment_left = fragment_left,
         fragment_right = fragment_right,
         message_left = message_left,
         message_right = message_right)

# def table_column_not_match

def warn(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   mark = arguments.pop(mark, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = arguments.pop(message_left, '')
   message_right = arguments.pop(message_right, '')
   STRESS = "\033[93m"
   NORMAL = "\033[0m"
   print("At ", place.emit(), ":\n")
   print(
         "      ", fragment_left, ' ',
         STRESS, mark, NORMAL, ' ',
         fragment_left, '\n')
   print(message_left, STRESS, mark, NORMAL, message_right)


def cease():
   raise SystemExit()



