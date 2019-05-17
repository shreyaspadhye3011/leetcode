#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>
#include <HTTPClient.h>
#include <WebServer.h>

const char* wifiSsid     = "";
const char* wifiPassword = ""; 

const char * ssid = "sam";
const char * password = NULL;

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
    Serial.println(ssid);
    WiFi.softAP(ssid);
    IPAddress myIP = WiFi.softAPIP();
    Serial.println(myIP);

    WiFi.begin(wifiSsid, wifiPassword);

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