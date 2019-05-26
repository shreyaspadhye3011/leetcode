require 'dm-core'
require 'dm-migrations'
require './main'

DataMapper.setup(:default, ENV['DATABASE_URL'] || "sqlite3://#{Dir.pwd}/main.db")

class Student
  include DataMapper::Resource
  property :id, Serial
  property :firstname, String
  property :lastname, String
  property :address, String
  property :birthday, String
  property :scuid, String
end

DataMapper.finalize
DataMapper.auto_upgrade!

# All routes
get '/students' do
  @title = 'Student Information System - Students'
  @students = Student.all
  erb :students_page
end

get '/students/new' do
  @title = 'Student Information System - Students'
  redirect to('/login') unless session[:admin]
  @student = Student.new
  erb :new_students
end

get '/students/:id' do
  @title = 'Student Information System - Students'
  redirect to('/login') unless session[:admin]
  @student = Student.get(params[:id])
  erb :list_students
end

get '/students/:id/edit' do
  @title = 'Student Information System - Students'
  redirect to('/login') unless session[:admin]
  @student = Student.get(params[:id])
  erb :edit_students
end

post '/students' do
  @student = Student.new
  @student.id = params[:id]
  @student.firstname = params[:firstname]
  @student.lastname = params[:lastname]
  @student.address = params[:address]
  @student.birthday = params[:birthday]
  @student.scuid = params[:scuid]
  if !validate_data
    flash[:notice] = "Please fill all details"
    redirect to('/students/new')
    # halt(401, 'Incomplete Fields, Please go back and fill all the fields')
  end
  @student.save
  redirect to('/students')
end

put '/students/:id' do
  @student = Student.get(params[:id])
  @student.id = params[:id]
  @student.firstname = params[:firstname]
  @student.lastname = params[:lastname]
  @student.address = params[:address]
  @student.birthday = params[:birthday]
  @student.scuid = params[:scuid]
  if !validate_data
    # redirect to("/students/#{@student.id}")
    halt(401, 'Incomplete Fields, Please go back and fill all the fields')
  end
  @student.save
  redirect to("/students/#{@student.id}")
end

delete '/students/:id' do
  Student.get(params[:id]).destroy
  redirect to('/students')
end

def validate_data
  if params[:id] == '' || params[:firstname] == '' || params[:lastname] == '' || params[:address] == '' || params[:birthday] == '' || params[:scuid] == ''
    false
  else
    true
  end
end
