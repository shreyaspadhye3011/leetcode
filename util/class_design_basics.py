# https://docs.python.org/3/tutorial/classes.html

class WordObject:    
  # class variable to store all anagram objects
  words = [] 

  # default constructor - added for completeness. Not required until you want to initialize some instance parameter as default constructor is inherently defined for you. Comment this and test. it will work
  def __init__(self):
    # instance variables
    self.value = ""
    self.index = 0

  def create_objects_from_list(self, arr_list):
    for index,value in enumerate(arr_list):
      # deafault constructor usage
      obj = WordObject()
      obj.value = value
      obj.index = index
      self.words.append(obj)
    return self.words

obj = WordObject()
word_list = obj.create_objects_from_list(["ace", "cea", "ceca"])

for obj in word_list:
  print(obj.index, obj.value)



