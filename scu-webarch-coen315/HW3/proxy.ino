/*
  Proxy Server: Assignment to demo that ESP32 can act both as a WifiClient and as an Access Point similar to the behaviour of a repeator. The code additionally checks for occurrence of the word "HTTP" and replaces it with "WHAT-IS-THIS"

  Testing steps:
  1. Add in your Wifi details (ssid & password) 
  2. Attach to the ESP32 board and upload this code
  3. Connect to the access point "shreyas" through Wifi (you won't require any password)
  4. Launch a browser and enter one of the following URLs to test. 

  The webpage should open with all instances of the word "HTTP" in the content replaced with "WHAT-IS-THIS"

  Test links:
  * http://192.168.4.1/http://esqsoft.com/examples/troubleshooting-http-using-telnet.htm
  * http://192.168.4.1/http://esqsoft.com/javascript/free-online-time-sheet.htm
*/
#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>
#include <WebServer.h>
#include <HTTPClient.h>

const char* ACCESS_PT_SSID = "shreyas";
const char* WIFIID = "";    // add your wifi ssid
const char* WIFIPWD = "";   // add your wifi password

WebServer server(80);

void renderWebContent() {
  // Get target URL & load it using HTTPClient
  String url = server.uri();
  url.remove(0,1);
  HTTPClient http;
  http.begin(url);    
  Serial.println("*****");  
  Serial.println(http.GET());  

  // Replace "HTTP" with "WHAT-IS-THIS"
  String content = http.getString();
  content.replace("HTTP","WHAT-IS-THIS");
  server.send(200, "text/html", content);
  http.end();
}

void setup() {
  delay(10);
  Serial.begin(115200);
  WiFi.softAP(ACCESS_PT_SSID);
  IPAddress accessPointIP = WiFi.softAPIP();
  Serial.print("Access Point IP: ");
  Serial.println(accessPointIP);

  WiFi.begin(WIFIID, WIFIPWD);
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
  }
  Serial.println("");
  Serial.println("### Wifi Connected Successfully!");
  server.onNotFound(renderWebContent);
  server.begin();
}
void loop() {
  server.handleClient();
}