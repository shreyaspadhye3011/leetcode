class Advisor
    def show_advisor_lines
        flag = false
        File.open('conversation.txt', 'r') do |file|
            while line = file.gets
                flag = true if line.include?('ADVISOR:') || flag
                if flag
                    if line.include?('STUDENT:')
                        flag = false
                    else
                        puts line.to_s
                    end
                end
            end
        end
    end
end

Advisor.new.show_advisor_lines
  