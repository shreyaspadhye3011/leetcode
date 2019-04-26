require 'erb'

def get_items() 
    ['bread', 'milk', 'eggs', 'spam'] 
end

class TemplateRenderer
    include ERB::Util 
    attr_accessor :items, :template, :date
    
    def initialize(items, template, date=Time.now) 
        @date = date 
        @items = items 
        @template = template 
    end

    def filter_template()
        puts ERB.new(@template).result(binding)
    end
end

#Test
template = %{ <!DOCTYPE html> 
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
contents = TemplateRenderer.new(get_items, template)
contents.filter_template