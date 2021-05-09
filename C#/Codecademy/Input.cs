using System;

namespace GettingInput
{
  class Program
  {
    static void Main()
    {
        /* Sample input / ouput */
        // Console.WriteLine("How old are you?");
        // string input = Console.ReadLine();
        // Console.WriteLine($"You are {input} years old!");

        /* Sample string concat + date time */
        string sampleString = $"Beginning of time is {DateTime.Now} and time zone is {TimeZoneInfo.Local}";
        Console.WriteLine(sampleString);
    }
  }
}

// dotnet run (command to run)
