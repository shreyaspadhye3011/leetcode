/*
  Proxy Server: Assignment to demo that ESP32 can act both as a WifiClient and as an Access Point similar to the behaviour of a repeator. The code additionally checks for occurrence of the word "HTTP" and replaces it with "WHAT-IS-THIS"

  Testing steps:
  1. Add in your Wifi details (ssid & password) 
  2. Attach to the ESP32 board and upload this code
  3. Connect to the access point "shreyas" through Wifi (you won't require any password)
  4. Launch a browser and enter one of the following URLs to test. 

  The webpage should open with all instances of the word "HTTP" in the content replaced with "WHAT-IS-THIS"

  Test links:
  * 192.168.4.1/www.esqsoft.com/examples/troubleshooting-http-using-telnet.htm
  * http://192.168.4.1/http://esqsoft.com/examples/troubleshooting-http-using-telnet.htm
  * http://192.168.4.1/http://esqsoft.com/javascript/free-online-time-sheet.htm
*/
#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>
#include <HTTPClient.h>
#include <WebServer.h>

const char* WIFIID = "AL";
const char* WIFIPWD = "silverwinter"; 
const char* ACCESS_PT_SSID = "shreyas";

WebServer server(80);

void givePage() {
  Serial.println("rrrrr");
  HTTPClient http;
  String str = server.uri();
  str.remove(0,1);
  Serial.println(str);
  http.begin(str);
  int httpCode = http.GET();          
  String payload = http.getString();   
 
  Serial.println(httpCode);  
  Serial.println(payload);   

  http.end();
  String content = payload;
  content.replace("HTTP","WHAT-IS-THIS");
  server.send(200, "text/html", content);
  }

void setup()
{
    delay(10);
    Serial.begin(115200);
    
    Serial.println();
    Serial.println(ACCESS_PT_SSID);
    WiFi.softAP(ACCESS_PT_SSID);
    IPAddress myIP = WiFi.softAPIP();
    Serial.println(myIP);

    WiFi.begin(WIFIID, WIFIPWD);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.println(WiFi.localIP());
    server.onNotFound(givePage);
    server.begin();
}
void loop() {
  server.handleClient();
}