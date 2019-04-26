require 'erb'

class TemplateRenderer
    include ERB::Util 
    attr_accessor :items, :template, :date
    
    def initialize(itemsHash, template, date=Time.now) 
        @date = date 
        @items = itemsHash[:items] 
        @listTitle = itemsHash[:title]
        @template = template 
    end

    def filter_template()
        puts ERB.new(@template).result(binding)
    end
end

#Test
# given template is used to list reminders for a day
template = %{ <!DOCTYPE html> 
    <html> 
    <head> 
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> 
    <title>Reminders</title> 
    </head>

    <body>
    <h1>Reminders for <%= @date.strftime('%d %m %Y') %></h1>
    <p>Items in <%=@listTitle%>:</p>
    <ul>
    <% for item in @items %> 
    <li> <%= h(item) %> </li>
    <% end %>
    </ul>
    </body>
    </html>
}  
reminderList = {:title => 'Todo List', :items => ['Ruby Assignment', 'Resume Corrections', 'Grocery Shopping']}
contents = TemplateRenderer.new(reminderList, template)
contents.filter_template