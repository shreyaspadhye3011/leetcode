require 'erb'

def get_items() 
    ['bread', 'milk', 'eggs', 'spam'] 
end

def get_template()
    %{ <!DOCTYPE html> 
    <html> 
    <head> 
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> 
    <title>Shopping List for <%= @date.strftime('%A, %d %B %Y') %></title> 
    </head>

    <body>
    <h1>Shopping List for <%= @date.strftime('%A, %d %B %Y') %></h1>
    <p>You need to buy:</p>
    <ul>
    <% for item in @items %> 
    <li> <%= h(item) %> </li>
    <% end %>
    </ul>
    </body>
    </html>
    } 
end

class ShoppingList
    include ERB::Util 
    attr_accessor :items, :template, :date
    
    def initialize(items, template, date=Time.now) 
        @date = date 
        @items = items 
        @template = template 
    end

    def render() 
        ERB.new(@template).result(binding) 
    end

    def save(file) 
        File.open(file, "w+") do |f| 
            f.write(render) 
        end 
    end

    def show_result()
        puts ERB.new(@template).result(binding)
    end
end

list = ShoppingList.new(get_items, get_template)
# list.save(File.join(ENV['PWD'], 'list.html'))     #save result in a separate file
list.show_result