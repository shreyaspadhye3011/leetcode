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

        bool isCSharpFun = true;
        bool isFishTasty = false;
        Console.WriteLine(isCSharpFun);             // Outputs True
        Console.WriteLine(isFishTasty);             // Outputs False
        Console.WriteLine(isCSharpFun == true);     // Outputs True
        Console.WriteLine(true.ToString());         // Outputs True
    }
  }
}

// dotnet run (command to run)
