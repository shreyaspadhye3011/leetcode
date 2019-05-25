require 'dm-core'
require 'dm-migrations'
# require 'sass'
require 'dm-timestamps'
require './main'

DataMapper.setup(:default, ENV['DATABASE_URL'] || "sqlite3://#{Dir.pwd}/main.db")

class Comment
  include DataMapper::Resource
  property :id, Serial
  property :name, String
  property :comment_txt, String
  property :created_at, DateTime
end

DataMapper.finalize
DataMapper.auto_upgrade!

# Fix DB inconsistency
# DataMapper.auto_migrate!

get '/comments' do
  @title = 'Student Information System - Comments'
  @comments = Comment.all
  erb :comments_home
end

get '/comments/new' do
  @title = 'Student Information System - Comments'
  redirect to('/login') unless session[:admin]
  @comment = Comment.new
  erb :new_comments
end

get '/comments/:id' do
  @title = 'Student Information System - Comments'
  redirect to('/login') unless session[:admin]
  @comment = Comment.get(params[:id])
  erb :show_comments
end

post '/comments' do
  if !validate_data_c
    halt(406, 'Incomplete Fields, Please go back and fill all the fields')
  end
  @comment = Comment.new
  @comment.id = params[:id]
  @comment.name = params[:name]
  @comment.comment_txt = params[:comment_txt]
  @comment.created_at = params[:created_at]
  @comment.save
  redirect to('/comments')
end

delete '/comments/:id' do
  Comment.get(params[:id]).destroy
  redirect to('/comments')
end

# Make sure request has all params needed
def validate_data_c
  if params[:name] == '' || params[:comment_txt] == ''
    false
  else
    true
  end
end
