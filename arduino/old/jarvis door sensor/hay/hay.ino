#include <NewPing.h>
#include <Servo.h>

const int pingbound1 = 92;
const int pingbound2 = 82;

int ping1 = 0;
int ping2 = 0;

bool light_state = false;

int num_people = 0;


int num_people2 = 0;
uint32_t store = 0;

NewPing sonar(11, 10, 110);
NewPing sonar1(9, 8, 110);
Servo light_servo;


void setup() {
  Serial.begin(2000000);
  pinMode(7, OUTPUT);
  digitalWrite(7, HIGH);
}

void loop() {
  ping1 = sonar.ping_cm();
  delay(15);  
  Serial.print(ping1);
  Serial.print(" ");
  if(ping1 < (pingbound1 - 10)){
    if((millis() - store) >600){
      for(int d = 0; d < 40; d++){
        ping2 =sonar1.ping_cm();
        delay(15);
        Serial.println(ping2);
        if(ping2 < (pingbound2 - 10)){ 
          num_people++;
          store = millis();
          break;
        }
      }
    } else {
      store = millis();
    }
  }
  
  ping2 =sonar1.ping_cm();
  delay(15);
  Serial.print(ping2);
  if(ping2 < (pingbound2 - 10)){
    if((millis() - store) > 600){
      for(int d = 0; d < 40; d++){
        ping1 =sonar.ping_cm();
        delay(15);
        Serial.println(ping1);
        if(ping1 < (pingbound1 - 10)){  
          num_people--;
          store = millis();
          break;
        }
      }
    } else {
      store = millis();
    }
  }
  
  Serial.println("");
  if(num_people != num_people2){
    if(num_people != 0 && light_state == false){
      digitalWrite(7, LOW);
      delay(50);
      light_servo.attach(6);
      light_servo.write(114);
      delay(550);
      light_servo.detach();
      digitalWrite(7, HIGH);
      light_state = true;;
    }
    if(num_people == 0 && light_state == true){
      digitalWrite(7, LOW);
      delay(50);
      light_servo.attach(6);
      light_servo.write(80);
      delay(550);
      light_servo.detach();
      digitalWrite(7, HIGH);
      light_state = false;
    }
  }
  num_people2 = num_people;
}
