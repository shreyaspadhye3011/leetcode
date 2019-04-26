class CountWord
    def count_word_occurence(str, word)
        if (str.is_a?(String) && word.is_a?(String))
            puts str.count_word(word)
        else
            puts "Both parameters should be string"
        end
    end
end

class String
    def count_word(word)
        count = 0
        # get all words and check for passed word match
        self.scan(/\w+/).each do |paraword|
            if paraword === word
                count += 1
            end
        end
        return count
    end
end

# Test
# CountWord.new.count_word_occurence("I am a stranger to this world but this world does not decide what I believe in and create", "a")
# CountWord.new.count_word_occurence(2, "a")