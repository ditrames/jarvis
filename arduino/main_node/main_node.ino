/*
 Copyright (C) 2012 James Coliz, Jr. <maniacbug@ymail.com>

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 version 2 as published by the Free Software Foundation.
 
 Update 2014 - TMRh20
 */

/**
 * Simplest possible example of using RF24Network,
 *
 * RECEIVER NODE
 * Listens for messages from the transmitter and prints them out.
 */

#include <RF24Network.h>
#include <RF24.h>
#include <SPI.h>


RF24 radio(9,10);                // nRF24L01(+) radio attached using Getting Started board 

RF24Network network(radio);      // Network uses that radio
const uint16_t this_node = 00;    // Address of our node in Octal format ( 04,031, etc)

char string[32] = "";


void setup(void)
{
  Serial.begin(2000000);
 
  SPI.begin();
  radio.begin();
  network.begin(/*channel*/ 90, /*node address*/ this_node);
  radio.setDataRate( RF24_2MBPS );
  radio.setPALevel(RF24_PA_MIN);
  radio.setAutoAck(true);
  
}

void loop(void){
  
  network.update();                  // Check the network regularly

  
  while ( network.available() ) {     // Is there anything ready for us?
    
    RF24NetworkHeader header;        // If so, grab it and print it out
    network.read(header,&string,sizeof(string));
    Serial.println(string);
  }
  if(Serial.available()>0){
    String command = "";
    while(Serial.available()>0){
      command += char(Serial.read());
    }
    Serial.println(command);
    if(command == "sendto"){
      char string[32];
      String command = "";
      while(!Serial.available()){}
      while(Serial.available()>0){
        command += char(Serial.read());
      }
      Serial.println(command);
      int address = command.toInt();
      Serial.println(address);
      command = "";
      while(!Serial.available()){}
      while(Serial.available()>0){
        command += char(Serial.read());
      }
      RF24NetworkHeader header(address); // If so, grab it and print it out
      command.toCharArray(string, 32);
      network.write(header,&string,sizeof(string));
      
    }
    
  }
}
