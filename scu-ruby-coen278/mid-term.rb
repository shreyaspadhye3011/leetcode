# Q1
# module M          
#     module N
#         class C
#              class D                
#              end
#             CONT = 10          
#         end
#     end
# end
# puts M::N::C::CONT

# Q2
# puts /love/  =~ "love you"
# puts /^you/ =~ "love you"
# puts /[aeiou]/ =~ "love you"
# puts /./ =~ "love"

# Q3
# x = 1
# x *= 3 while x < 40
# x -= 6 until x < 60
# puts x

# Q4
# people = [
#   {:name => "bob", :age => 42},
#   {:name => "frank", :age => 13}
# ]
# arr = []
# people.each do |peo|
#     arr.push(peo[:name])
# end
# p arr