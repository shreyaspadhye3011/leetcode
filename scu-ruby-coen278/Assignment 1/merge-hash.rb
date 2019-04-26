class Hash
    def merge(h2)
        res = dup
        h2.each do |key, val|
            res[key] = if block_given? && key?(key)
                            yield(key, res[key], val)
                        else
                            val
                        end
        end
        res
    end
  
    def merge!(h2)
        h2.each do |key, val|
        self[key] = if block_given? && key?(key)
                      yield(key, self[key], val)
                    else
                      val
                    end
        end
        self
    end
end

#Test
h1 = { 'a' => 100, 'b' => 200 }
h2 = { 'b' => 254, 'c' => 300 }
# p h1.merge(h2) { |_key, val1, val2| val2 - val1 }
p h1.merge(h2) 
  