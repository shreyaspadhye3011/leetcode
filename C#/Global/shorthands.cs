/* create a new dotnet project */
// dotnet new console

/* run a dotnet project */
// dotnet run

/* Timezones */
// https://docs.microsoft.com/en-us/dotnet/api/system.timezone.currenttimezone?view=net-5.0
// DateTime.Now -- current time (english date time)
// TimeZoneInfo.Local -- local time zone

/* Data Types */
int myNum = 5;               // Integer (whole number)
double myDoubleNum = 5.99D;  // Floating point number
char myLetter = 'D';         // Character
bool myBool = true;          // Boolean
string myText = "Hello";     // String

// It is also possible to convert data types explicitly by using built-in methods, such as 
// Convert.ToBoolean, Convert.ToDouble, Convert.ToString, Convert.ToInt32 (int) and Convert.ToInt64 (long)

/* Boolean */
bool isCSharpFun = true;
bool isFishTasty = false;
Console.WriteLine(isCSharpFun);             // Outputs True
Console.WriteLine(isFishTasty);             // Outputs False
Console.WriteLine(isCSharpFun == true);     // Outputs True
Console.WriteLine(true.ToString());         // Outputs True
// Notice that all lowercase true & false is used in code but the output is capitalized

// declaring constants
const int myNum = 15;
myNum = 20; // error

/* --------------------------------- */
/* Loops */
for (int i = 0; i < 5; i++) 
{
  Console.WriteLine(i);
}

// Array & foreach
string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
foreach (string i in cars) 
{
  Console.WriteLine(i);
}

// do while
int i = 0;
do
{
    Console.WriteLine("i = {0}", i);
    i++;

} while (i < 5);

/* --------------------------------- */

/* Methods optional params & named params */
// Definition: public void ExampleMethod(int required, string optionalstr = "default string", int optionalint = 10)
// Call: anExample.ExampleMethod(3, optionalint: 4);
// https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/named-and-optional-arguments

// optional param Example #2
static void MyMethod(string country = "Norway") 
{
  Console.WriteLine(country);
}

/* Arrays */
// Sort a string array
string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
Array.Sort(cars);

/* Dictionary */
// https://www.tutorialsteacher.com/csharp/csharp-dictionary
IDictionary<int, string> numberNames = new Dictionary<int, string>();
numberNames.Add(1,"One"); //adding a key/value using the Add() method
numberNames.Add(2,"Two");
numberNames.Add(3,"Three");

//The following throws run-time exception: key already added.
//numberNames.Add(3, "Three"); 

foreach(KeyValuePair<int, string> kvp in numberNames)
    Console.WriteLine("Key: {0}, Value: {1}", kvp.Key, kvp.Value);
		
//creating a dictionary using collection-initializer syntax
var cities = new Dictionary<string, string>(){
	{"UK", "London, Manchester, Birmingham"},
	{"USA", "Chicago, New York, Washington"},
	{"India", "Mumbai, New Delhi, Pune"}
};
		
foreach(var kvp in cities)
    Console.WriteLine("Key: {0}, Value: {1}", kvp.Key, kvp.Value);


/* --------------------------------- */

/* Classes & Inheritance */
 class Car : Vehicle  // derived class (child)
{
  public string modelName = "Mustang";  // Car field
}

// sealed class Vehicle -- "sealed" to ensure that no other class can inherit from this.


// Naming Conventions
// https://github.com/ktaranov/naming-convention/blob/master/C%23%20Coding%20Standards%20and%20Naming%20Conventions.md

/* Learn */
// https://www.tutorialsteacher.com/csharp/csharp-partial-class
// https://www.w3schools.com/cs/cs_variables.asp
// https://www.w3schools.com/cs/exercise.asp?filename=exercise_data_types4