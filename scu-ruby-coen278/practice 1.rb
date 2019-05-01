# puts 11.even?
# puts 11.odd?
# puts 11.class
# puts 123456789012345678901234567890.class
# puts 11.next
# puts 11.succ

# puts 12.9.ceil
# puts (-12.9).ceil
# puts -12.9.abs
# puts 12.9.floor
# puts 12.9.to_i
# puts 12.9.to_int
# puts 10 ** 2
# puts 12.9.round
# puts 12.4.round
# puts 12.5.round
# puts 3.14159.round(2)
# puts 4.14159.round(4)
# puts 4.14152.round(3)

a = 10
# a.times { |x|  puts x}
# a.times { |x|  print x}

# a.upto(20) {|x| puts x}
# a.upto(1) {|x| puts x}

# b = 10...20
# puts b.first
# puts b.last
# b.each { |x| puts x}
# b.each do |x| puts x end

# puts 'it’s a wonderful year'
# puts "it’s a wonderful year"
# puts %q/it’s a wonderful year/
# puts %q/i spent #{a} years to get this degree/
# puts %Q/i spent #{a} years to get this degree/  # %Q -> ""
# puts 'i spent #{a}'  # %q -> ''
# puts 'i am ' + a.to_s + ' years old'
# puts 'i am ' << a.to_s << ' years old'
# puts "i am ""#{a}"" years old"

# p "car" <=> "car"

# "abcdefghijklmnopqrstuvwxyz".each_char {|x| puts x}
# puts 10 * "love"
# p "love " * 10 

# p ["apple", "banana", "orange"].include?("apple")
# p ["apple", "banana", "orange"].join
# p ["apple", "banana", "orange"].join(" ")

# str = "capital"
# p str.upcase
# p str
# p str.capitalize
# p str.capitalize!
# p str.upcase!
# p str
# p str.downcase
# p "aBcDeFg".swapcase
# p "Abc".swapcase

arr = %w{d b e f z h a l a b e a z m}
# arr = %w{d b e f}
# # p arr
# print arr.shuffle
# p arr.slice!(2)
# p arr
# p arr.uniq
# p arr.reverse
# [1,2,3,4,5].select { |num|  num.even?  }   #=> [2, 4]
# a = %w{ a b c d e f }
# a.select { |v| v =~ /[aeiou]/ }  #=> ["a", "e"]

# p "make".split("", 3)
# p "make".split("")
# p "hello ".gsub(" ", '$')
# p "hello".gsub(/[aeiou]/, '*')

# puts "love".reverse
# puts "love".respond_to?(:reverse)
mysymbol = :love
# puts mysymbol.reverse
puts mysymbol.respond_to?(:reverse)





