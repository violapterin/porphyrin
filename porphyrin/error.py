import branch
import twig
import leaf
import main

def warn(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   token = arguments.pop(token, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = arguments.pop(message_left, '')
   message_right = arguments.pop(message_right, '')
   STRESS = "\033[93m"
   NORMAL = "\033[0m"
   print("At ", place.emit(), ":\n")
   print(
         "      ", fragment_left, ' ',
         STRESS, token, NORMAL, ' ',
         fragment_left, '\n')
   print(message_left, STRESS, token, NORMAL, message_right)


def not_recognized_mark_branch(**arguments):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   token = arguments.pop(token, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = "Token"
   message_right = "is not a branch opening mark."
   warn(
         place = place,
         fragment_left = fragment_left,
         fragment_right = fragment_right,
         message_left = message_left,
         message_right = message_right)
   cease()


def not_matched_mark_branch(Error):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   token = arguments.pop(token, '')
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


def not_recognized_mark_leaf(Error):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   token = arguments.pop(token, '')
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

def not_matched_mark_leaf(Error):
   place = arguments.pop(place, Place())
   fragment_left = arguments.pop(fragment_left, '')
   token = arguments.pop(token, '')
   fragment_right = arguments.pop(fragment_right, '')
   message_left = "Leaf opening mark"
   message_right = "is not matched."
   warn(
         place = place,
         fragment_left = fragment_left,
         fragment_right = fragment_right,
         message_left = message_left,
         message_right = message_right)
   cease()

def cease():
   raise SystemExit()



