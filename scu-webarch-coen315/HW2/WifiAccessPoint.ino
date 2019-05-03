/*
  This file creates an open WiFi access point "shreyas" and provides a web server on it from where you can handle 2 LEDs on the ESP32 chip 

  Steps:
  1. Connect to the access point "shreyas"
  2. Point your web browser to http://192.168.4.1/ and select appropriate buttons to handle the LEDs
*/

#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>
#include "SPIFFS.h"
#include <ESPAsyncWebServer.h>

// Access point config
const char *ssid = "shreyas";
const char *password = "";

AsyncWebServer servers(90);
WiFiServer server(80);


void setup() {
   pinMode(4, OUTPUT);
   pinMode(14, OUTPUT);
   digitalWrite(4, LOW);
   digitalWrite(14, LOW);

  Serial.begin(115200);
  if(!SPIFFS.begin()){
    Serial.println("SPIFFS Error");
    return;
  }
  Serial.println();
  Serial.println("Configuring access point...");

  WiFi.softAP(ssid, password);
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  
  servers.on("/img", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/bg.jpg", "image/jpeg");
  });
  server.begin();
  servers.begin();

  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();  

  if (client) {                             
    Serial.println("New Client.");          
    String currentLine = "";                
    while (client.connected()) {            
      if (client.available()) {             
        char c = client.read();             
        Serial.write(c);                    
        if (c == '\n') {                    
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();

            client.println();
            client.print("<style> .button { border-radius: 8px; color: #ffffff; width: 165; height: 40; margin: 5px } .red-button { background-color: #f44336; margin-bottom: 70px} .green-button { background-color: #4CAF50; } </style>");
            client.print("<body background = \"http://192.168.4.1:90/img\"> <div style=\"margin-top: 200px; margin-left: 600px\">");
            client.print("<a href='/on'><button class=\"button green-button\">LED 1 On</button></a> <br>");
            client.print("<a href='/off'><button class=\"button red-button\">LED 1 Off</button></a> <br><br>");

            client.print("<a href='/led2on'><button class=\"button green-button\">LED 2 On</button></a> <br>");
            client.print("<a href='/led2off'><button class=\" button red-button\">LED 2 Off</button></a> <br><br>");
            client.print("</div> </body>");
            
            break;
          } else {    
            currentLine = "";
          }
        } else if (c != '\r') {  
          currentLine += c;      
        }

        if (currentLine.endsWith("GET /on")) {
          Serial.println("\ninside on\n");
          digitalWrite(4, HIGH);
        }

        else if (currentLine.endsWith("GET /off")) {
          Serial.println("\ninside off\n");
          digitalWrite(4, LOW);
        }

        else if (currentLine.endsWith("GET /led2on")) {
          digitalWrite(14, HIGH);
        }
        else if (currentLine.endsWith("GET /led2off")) {
          digitalWrite(14, LOW);
        }
      }
    }
    client.stop();
    Serial.println("Client Disconnected.");
  }
}