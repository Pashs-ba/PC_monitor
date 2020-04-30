#include <LiquidCrystal.h>

// if you use another monitor you need to config
LiquidCrystal lcd(11, 12, 5, 4, 3, 2); // screen init

#define USE_TIME 1 //if 1 - display time

void setup() {
  lcd.begin(16, 2);
  lcd.print("Waiting for");
  lcd.setCursor(0,1);
  lcd.print("connection");
  Serial.begin(9600);
  lcd.setCursor(0,0);
}
 
void loop() {
    if (Serial.available() >0){
      int cpu = Serial.parseInt();// Download form port
      int ram = Serial.parseInt();
      int hour = Serial.parseInt();
      int minute = Serial.parseInt();
      lcd.clear();
      lcd.print("CPU ");
      lcd.print(cpu);
      lcd.print("%");
      lcd.setCursor(0,1);
      lcd.print("RAM ");
      lcd.print(ram);
      lcd.print("%");
      lcd.setCursor(11,0);
      lcd.print("Now");
      lcd.setCursor(10,1);
      if (USE_TIME == 1){
        if (hour>9){
          lcd.print(hour);
          }
        else{
          lcd.print(0);
          lcd.print(hour);
          }
        lcd.print(":");
        if (minute>9){
          lcd.print(minute);
        }
        else{
          lcd.print(0);
          lcd.print(minute);
        }
      }
    }
};
