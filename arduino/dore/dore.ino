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
#include <printf.h>

RF24 radio(9,10);                    // nRF24L01(+) radio attached using Getting Started board 

RF24Network network(radio);         // Network uses that radio

const uint16_t this_node = 011;        // Address of our node in Octal format
const uint16_t other_node = 00;       // Address of the other node in Octal format

const unsigned long interval = 2000; //ms  // How often to send 'hello world to the other unit

unsigned long last_sent;             // When did we last send?
unsigned long packets_sent;          // How many have we sent already

String testd = "am hub 011 door all ";
char string[32] = "";

void setup(void)
{
  Serial.begin(115200);
  SPI.begin();
  randomSeed(analogRead(0));
  printf_begin();
  radio.begin(); 
  network.begin(/*channel*/ 90, /*node address*/ this_node);
  radio.setDataRate( RF24_2MBPS );
  radio.setPALevel(RF24_PA_MIN);
  radio.printDetails();
  for(int i = 0; i < 2; i++){
    Serial.print("Sending...");
    RF24NetworkHeader header( other_node);
    testd += random(0, 10);
    testd.toCharArray(string, 32);
    bool ok = network.write(header,&string,sizeof(string));
    if (ok)
      Serial.println("ok.");
    else
      Serial.println("failed.");
  }
}

void loop() {
  network.update();                          // Check the network regularly
  while ( network.available() ) {     // Is there anything ready for us?
    RF24NetworkHeader header;        // If so, grab it and print it out
    network.read(header,&string,sizeof(string));
    Serial.println(string);
  }
    
}
