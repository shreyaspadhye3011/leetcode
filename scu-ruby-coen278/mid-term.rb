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

class Hash
    def select(&block)
        self.each do |key, val|
            if block_given? && key?(key)
                res = yield(key, self[key])
                # res = block.call(key, self[key], val)
                # puts res
                if(!res)
                    self.delete(key)
                end
            end
        end
    end
end
h = { "a" => 100, "b" => 200, "c" => 300 }
puts h.select{|k, v| v > 100}