class Compress
    attr_accessor :hash, :index_array
    def initialize(str = '')
        @str = str
        self.create_hash
    end
  
    def create_hash
      if @str != ''
        hash_str = {}
        index_array = []
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
          end
          index_array.push(hash_str[x])
          @hash = hash_str
          @index_array = index_array
        end
      else
        'The input string is empty!'
      end
    end

    def get_hash
        return @hash
    end

    def get_index_array
        return @index_array
    end
end

#Test
# str = 'i love you but do you love me'
# str = 'make me a me of a make'
# obj = Compress.new(str)
# puts obj.get_hash
# puts obj.get_index_array  