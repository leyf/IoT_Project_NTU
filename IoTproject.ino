#include <DHT.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include <SPI.h>


#define DHTPIN 2    
#define DHTTYPE DHT22   
#define BuzzerPin 7
#define ledPin 8


DHT dht(DHTPIN, DHTTYPE); // Initialize DHT sensor
int rainValue;
int h;
int t;
int p;

SoftwareSerial mySerial(10, 11); // RX, TX
boolean flag = false;
void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(BuzzerPin,OUTPUT);
  
  mySerial.begin(9600);
  
  
  
}


  


void loop() {
  rainValue = analogRead(A0);
  
  h = dht.readHumidity();
  t = dht.readTemperature();
  
  Serial.print("rainValue: ");
  Serial.println(rainValue);
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" C\t, ");
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.println(" %");

  if(rainValue<=900){
    digitalWrite(ledPin, HIGH);    
    digitalWrite(BuzzerPin, HIGH);
  }
  else{
    digitalWrite(ledPin, LOW);
    digitalWrite(BuzzerPin, LOW);
    }


   //Serial.print("---- GY BMP 280 ----------------\n");
   //Serial.print("Temperature = ");
   //Serial.print(bme.readTemperature());
   //Serial.println(" *C");
   //Serial.print("Pressure = ");
   //Serial.print(bme.readPressure()*pow(((288-(0.0065*28))/288),5.2561)); // 100 Pa = 1 millibar
   //Serial.println(" Pa");
   //msg[3] = bme.readPressure() / 100;
   
   
   mySerial.println(String(rainValue)+","+String(h)+","+String(t)+",");
   
   /*mySerial.println(String(h)+",");
   
   mySerial.println(String(t)+",");*/
  delay(5000);
}
