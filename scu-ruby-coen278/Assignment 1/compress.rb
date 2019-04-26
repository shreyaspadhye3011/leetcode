class Compress
    attr_accessor :word_set, :index_array
    def initialize(str = '')
        @str = str
        @word_set = []
        @index_array = []
        self.create_word_set
    end
  
    def create_word_set
      if @str != ''
        hash_str = {}
        curr_index = 0
        arr = @str.split(' ')
        arr.each do |x|
          new_x = ''
          if x[x.length - 1] == ',' || x[x.length - 1] == '.'
            for i in 0..x.length - 2
              new_x += x[i]
            end
            x = new_x
          end
          if hash_str.key?(x)
            # do nothing as the key already exists
          else
            hash_str[x] = curr_index
            curr_index += 1
            @word_set.push(x)
          end
          @index_array.push(hash_str[x])
        end
      else
        'The input string is empty!'
      end
    end

    def get_word_set
        return @word_set
    end

    def get_index_array
        return @index_array
    end
end

#Test
# str = 'i love you but do you love me'
# str = 'make me a me of a make'
# obj = Compress.new(str)
# p obj.get_word_set
# p obj.get_index_array  