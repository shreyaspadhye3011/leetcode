# https://docs.python.org/3/tutorial/classes.html

class Anagram:    
  # class variable to store all anagram objects
  anagrams = [] 

  def create_objects_from_list(self, arr_list):
    for index,value in enumerate(arr_list):
      # deafault constructor
      obj = Anagram()
      obj.value = value
      obj.index = index
      self.anagrams.append(obj)
    return self.anagrams

obj = Anagram()
anagram_list = obj.create_objects_from_list(["ace", "cea", "eca"])

for obj in anagram_list:
  print(obj.index, obj.value)

