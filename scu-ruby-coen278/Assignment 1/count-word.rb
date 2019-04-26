class String
    def count_word(word = "")
        if word != ""
            if (word.is_a?(String))
                count = 0
                # get all words and check for passed word match
                self.scan(/\w+/).each do |paraword|
                    if paraword === word
                        count += 1
                    end
                end
                return count
            else
                return "parameter should be string"
            end
        else
            hash = {}
            self.scan(/\w+/).each do |paraword|
                if hash.key?(paraword)
                    hash[paraword] += 1
                else
                    hash[paraword] = 1
                end
            end
            return hash
        end
    end
end

# Test
# CountWord.new.count_word_occurence("I am a stranger to this world but this world does not decide what I believe in and create", "a")
# CountWord.new.count_word_occurence(2, "a")
# str = "I am a stranger to this world but this world does not decide what I believe in and create"
# str = "three three three"
# puts str.count_word("I")