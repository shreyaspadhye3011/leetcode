class CountWord
    def count_word_occurence(str, word)
        if (str.is_a?(String) && word.is_a?(String))
            str.count_word(word)
        else
            puts "Both parameters should be string"
        end
    end

class String
    def count_word(word)
        puts self + " ~ " + word
    end

# Test
CountWord.new.count_word_occurence("I am", "strong")