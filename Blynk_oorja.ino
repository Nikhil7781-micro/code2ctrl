#define BLYNK_TEMPLATE_ID "TMPL3bS_nj3of"
#define BLYNK_TEMPLATE_NAME "led toggle"
#define BLYNK_AUTH_TOKEN "J6KWg4LQkuChrD0o4Ry6PYfo6DF_xbrJ"



#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>

// WiFi details
char ssid[] = "LAVA LXX504";
char pass[] = "00778100";

// LED pin
#define LED_PIN 2

// Virtual pin V0 will control the LED
BLYNK_WRITE(V0)
{
  int value = param.asInt();  // Read value (0/1)

  if(value == 1) {
    digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_PIN, LOW);
  }
}

void setup()
{
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  Serial.begin(115200);

  // Connect to Blynk
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop()
{
  Blynk.run();
}
