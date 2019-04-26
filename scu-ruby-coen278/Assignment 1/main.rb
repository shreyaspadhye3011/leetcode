#!/usr/bin/ruby

puts
puts '***************** Question 1 *****************'
require_relative 'count-word.rb'
str = <<EOS
Facebook and its founder must release documents and electronic correspondence
to a defense lawyer whose client has fled from criminal charges that he falsely
 claimed a majority ownership in the social media giant,
 a federal judge said Friday.
EOS
puts "Word count: #{str.count_word('and')}"
puts
str = "three three, three"
puts "All Word count hash: \n#{str.count_word()}"
puts

puts '***************** Question 2 *****************'
require_relative 'search-student.rb'
students = [
{:firstname => "John", :lastname => "LastnameJohn",  :phonenumber => 123456789},
{:firstname => "Ken", :lastname => "Lastnameken",  :phonenumber => 456734244},
{:firstname => "Marisa", :lastname => "lastnamemarisa",  :phonenumber => 443234567},
{:firstname => "Ken", :lastname => "Kenlastname",  :phonenumber => 456734244}
]
SearchStudent.new.search_students(students, firstname: "ken")
puts


puts '***************** Question 3 *****************'
require_relative 'compress.rb'
str = 'i love you but do you love me'
obj = Compress.new(str)
puts 'String: ' + str
puts 'Set of words:'
p obj.word_set
puts 'Array index:'
p obj.index_array
puts

puts '***************** Question 4 *****************'
require_relative 'merge-hash.rb'
h1 = { 'a' => 100, 'b' => 200 }
h2 = { 'b' => 254, 'c' => 300 }
puts 'Merge with code block'
p h1.merge(h2) { |_key, val1, val2| val2 - val1 }
puts 'merge :'
puts h1.merge(h2)
puts h1
puts 'merge! :'
puts h1.merge!(h2)
puts h1
puts

puts '***************** Question 5 *****************'
require_relative 'template-render.rb'
template = %{ <!DOCTYPE html> 
    <html> 
    <head> 
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> 
    <title>Reminders</title> 
    </head>

    <body>
    <h1>Reminders for <%= @date.strftime('%d %m %Y') %></h1>
    <p>Items in <%=@listTitle%>:</p>
    <ul>
    <% for item in @items %> 
    <li> <%= h(item) %> </li>
    <% end %>
    </ul>
    </body>
    </html>
}  
reminderList = {:title => 'Todo List', :items => ['Ruby Assignment', 'Resume Corrections', 'Grocery Shopping']}
contents = TemplateRenderer.new(reminderList, template)
contents.filter_template
puts

puts '***************** Question 6 *****************'
require_relative 'advisor.rb'
puts Advisor.new.show_advisor_lines

