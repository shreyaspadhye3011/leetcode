class SearchStudent
    def search_students(students, hash)
        @students = students
        found = false
        @students.each do |student|
        # do a lowercase check on both to facilitate case insensitive search
        # only single key-value combination search considered as no additional requirements given in question
            key = hash.keys[0]
            value = hash.values[0]
            hashVal = student[key]
            if key != :phonenumber
                result = student[key].downcase.eql?(value.downcase)
            else
                result = (hashVal === value)
            end
            if result
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
# students = [
# {:firstname => "John", :lastname => "LastnameJohn",  :phonenumber => 123456789},
# {:firstname => "Ken", :lastname => "Lastnameken",  :phonenumber => 456734244},
# {:firstname => "Marisa", :lastname => "lastnamemarisa",  :phonenumber => 443234567},
# {:firstname => "Ken", :lastname => "Kenlastname",  :phonenumber => 456734244}
# ]
# SearchStudent.new.search_students(students, firstname: "ken")
# SearchStudent.new.search_students(students, firstname: "KEn")
# SearchStudent.new.search_students(students, firstname: "KEny")
# SearchStudent.new.search_students(students, lastname: "lastnameken")
# SearchStudent.new.search_students(students, phonenumber: 456734244)
# SearchStudent.new.search_students(students, phonenumber: 456734254)
