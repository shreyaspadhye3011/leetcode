class SearchStudent
    def search_students2(students, name)
        @students = students
        found = false
        @students.each do |student|
          if student[:firstname].downcase.eql?(name.downcase)
            if (!found)
                puts "First Name\tLast Name\t\tPhone#"
            end
            found = true
            puts "#{student[:firstname]}\t\t#{student[:lastname]}\t\t#{student[:phonenumber]}"
          end
        end
        if !(found)
            puts "No record found"
        end
    end

    def search_students(students, hash)
        @students = students
        found = false
        @students.each do |student|
          if student[hash.keys[0]].downcase.eql?(hash.values[0].downcase)
            if (!found)
                puts "First Name\tLast Name\t\tPhone#"
            end
            found = true
            puts "#{student[:firstname]}\t\t#{student[:lastname]}\t\t#{student[:phonenumber]}"
          end
        end
        if !(found)
            puts "No record found"
        end
    end
end

#Test
students = [
{:firstname => "John", :lastname => "LastnameJohn",  :phonenumber => 123456789},
{:firstname => "Ken", :lastname => "Lastnameken",  :phonenumber => 456734244},
{:firstname => "Marisa", :lastname => "lastnamemarisa",  :phonenumber => 443234567},
{:firstname => "Ken", :lastname => "Kenlastname",  :phonenumber => 456734244}
]
# SearchStudent.new.search_students(students, firstname: "ken")
# SearchStudent.new.search_students(students, firstname: "KEn")
SearchStudent.new.search_students(students, firstname: "KEny")

