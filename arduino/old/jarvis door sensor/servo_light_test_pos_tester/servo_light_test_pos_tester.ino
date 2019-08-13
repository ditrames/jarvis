#include <Servo.h>

Servo servo1[4];


int hay[][2] = {{180,0},{0,180},{0,180},{0,180}};

String comp = "";
void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < 4 ; i++){
    servo1[i].attach(i+6);
  }
  Serial.begin(115200);
}

int degree(int i, int x){
  return map(0, 180, hay[i][0], hay[i][1], x);
}

void loop(){
  for(int i = 0; i < 4 ; i++){
    Serial.println(degree(i, 180));
  }
  
  for(int i = 0; i < 4 ; i++){
    servo1[i].write(degree(i, 180));  
  }
  
  delay(5000);
  for(int i = 0; i < 4 ; i++){
    Serial.println(degree(i, 90));
  }
  for(int i = 0; i < 4 ; i++){
    servo1[i].write(degree(i, 90));  
  }
  delay(5000);
  for(int i = 0; i < 4 ; i++){
    Serial.println(degree(i, 0));
  }
  for(int i = 0; i < 4 ; i++){
    servo1[i].write(degree(i, 0));  
  }
  delay(5000);
}

