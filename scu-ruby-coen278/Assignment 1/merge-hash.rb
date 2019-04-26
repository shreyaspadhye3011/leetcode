class Hash
    def merge(h2)
        res = dup
        h2.each do |key, val|
            if block_given? && key?(key)
                res[key] = yield(key, res[key], val)
            else
                res[key] = val
            end
        end
        return res
    end
  
    def merge!(h2)
        h2.each do |key, val|
            if block_given? && key?(key)
                self[key] = yield(key, self[key], val)
            else
                self[key] = val
            end
        end
        return self
    end
end

#Test
h1 = { 'a' => 100, 'b' => 200 }
h2 = { 'b' => 254, 'c' => 300 }
# p h1.merge(h2) { |_key, val1, val2| val2 - val1 }
# p h1.merge(h2) 
# p h1
p h1.merge!(h2)
p h1