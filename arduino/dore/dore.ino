/*
 Copyright (C) 2012 James Coliz, Jr. <maniacbug@ymail.com>

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 version 2 as published by the Free Software Foundation.
 
 Update 2014 - TMRh20
 */

/**
 * Simplest possible example of using RF24Network 
 *
 * TRANSMITTER NODE
 * Every 2 seconds, send a payload to the receiver node.
 */

#include <RF24Network.h>
#include <RF24.h>
#include <SPI.h>
#include <Servo.h>

Servo light_servo;
RF24 radio(9,10);                    // nRF24L01(+) radio attached using Getting Started board 

RF24Network network(radio);         // Network uses that radio

const uint16_t this_node = 011;        // Address of our node in Octal format
const uint16_t other_node = 00;       // Address of the other node in Octal format

char string[32] = "";

String testd = "am hub 011 door all ";
void dynamic_wait(int wait){
  uint64_t st = millis();
  while(millis()-st < wait){
    network.update();
    if(network.available()){
      RF24NetworkHeader header;        // If so, grab it and print it out
      network.read(header,&string,sizeof(string));
    }
  }
}

void move_servo(int angle){
  light_servo.attach(5);
  light_servo.write(angle);
  dynamic_wait(200);
  light_servo.detach();
}

void setup(void)
{ 
  Serial.begin(2000000);
  SPI.begin();
  light_servo.attach(5);
  pinMode(A5, OUTPUT);
  analogWrite(A5, 0);
  radio.begin(); 
  network.begin(/*channel*/ 90, /*node address*/ this_node);
  radio.setDataRate(RF24_2MBPS);
  radio.setPALevel(RF24_PA_LOW);
  radio.printDetails();
  move_servo(130);
  delay(1000);
  move_servo(60);
  while(1){
    Serial.print("Sending...");
    RF24NetworkHeader header( other_node);
    testd += random(0, 10);
    testd.toCharArray(string, 32);
    bool ok = network.write(header,&string,sizeof(string));
    if(ok){
      Serial.println("ok.");
      break;
    } else {
      Serial.println("failed.");
    }
  }
  
}

void loop() {
  network.update();                          // Check the network regularly
  Serial.println(network.available());
  while(network.available()){ 
    char string[32] = "";
    RF24NetworkHeader header;        // If so, grab it and print it out
    network.read(header,&string,sizeof(string));
    Serial.println(string);
    Serial.println(millis());
    if(string[0] == 'a'){
      move_servo(130);
    }
    if(string[0] == 'b'){    
      move_servo(60);

    }
  } 
}
