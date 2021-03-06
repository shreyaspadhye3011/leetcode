/*
  WiFiAccessPoint.ino creates a WiFi access point and provides a web server on it.

  Steps:
  1. Connect to the access point "yourAp"
  2. Point your web browser to http://192.168.4.1/H to turn the LED on or http://192.168.4.1/L to turn it off
     OR
     Run raw TCP "GET /H" and "GET /L" on PuTTY terminal with 192.168.4.1 as IP address and 80 as port

  Created for arduino-esp32 on 04 July, 2018
  by Elochukwu Ifediora (fedy0)
*/

#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

#define LED_BUILTIN 2   // Set the GPIO pin where you connected your test LED or comment this line out if your dev board has a built-in LED

// Set these to your desired credentials.
const char *ssid = "shreyas";
const char *password = "";

WiFiServer server(80);


void setup() {
   pinMode(LED_BUILTIN, OUTPUT);
   pinMode(4, OUTPUT);
   pinMode(3, OUTPUT);
   digitalWrite(4, LOW);
   digitalWrite(3, LOW);

  Serial.begin(115200);
  Serial.println();
  Serial.println("Configuring access point...");

  // You can remove the password parameter if you want the AP to be open.
  WiFi.softAP(ssid, password);
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.begin();

  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();   // listen for incoming clients

  if (client) {                             // if you get a client,
    Serial.println("New Client.");           // print a message out the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected()) {            // loop while the client's connected
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out the serial monitor
        if (c == '\n') {                    // if the byte is a newline character

          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();

            // the content of the HTTP response follows the header:
//            client.print("Click <a href=\"/H\">here</a> to turn ON the LED.<br>");
//            client.print("Click <a href=\"/L\">here</a> to turn OFF the LED.<br>");

            // The HTTP response ends with another blank line:
            client.println();
            // break out of the while loop:

//            client.print("Click <a href=\"/on\">here</a> to turn ON the LED.<br>"); 
//            client.print("Click <a href=\"/off\">here</a> to turn OFF the LED<br><br>");
//
//            client.print("Click <a href=\"/on2\">here</a> to turn ON the LED - 2.<br>"); 
//            client.print("Click <a href=\"/off2\">here</a> to turn OFF the LED - 2<br><br>");
            client.print("<style> .button { color: #ffffff; } .red-button { background-color: #f44336; } .green-button { background-color: #4CAF50; } </style>");
            client.print("<body> <div style=\"margin-top: 150px; margin-left: 600px\">");
            client.print("<a href='/on'><button class=\"button green-button\">LED 1 On</button></a> <br>");
            client.print("<a href='/off'><button class=\"button red-button\">LED 1 Off</button></a> <br><br>");

            client.print("<a href='/on2'><button class=\"button green-button\">LED 2 On</button></a> <br>");
            client.print("<a href='/off2'><button class=\" button red-button\">LED 2 Off</button></a> <br><br>");
            client.print("</div> </body>");
            
            break;
          } else {    // if you got a newline, then clear currentLine:
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }

        if (currentLine.endsWith("GET /on")) {
          Serial.println("\ninside on\n");
          digitalWrite(4, HIGH);
        }

        else if (currentLine.endsWith("GET /off")) {
          Serial.println("\ninside off\n");
          digitalWrite(4, LOW);
        }

        else if (currentLine.endsWith("GET /on2")) {
          digitalWrite(3, HIGH);
        }
        else if (currentLine.endsWith("GET /off2")) {
          digitalWrite(3, LOW);
        }

        

        // Check to see if the client request was "GET /H" or "GET /L":
//        if (currentLine.endsWith("GET /H")) {
//          digitalWrite(LED_BUILTIN, HIGH);               // GET /H turns the LED on
//        }
//        if (currentLine.endsWith("GET /L")) {
//          digitalWrite(LED_BUILTIN, LOW);                // GET /L turns the LED off
//        }
      }
    }
    // close the connection:
    client.stop();
    Serial.println("Client Disconnected.");
  }
}