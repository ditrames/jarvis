#include <Keypad.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// starts the keypad up
const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns

char hexaKeys[ROWS][COLS] = {
  {'1','2','3','c'},
  {'4','5','6','a'},
  {'7','8','9','e'},
  {'.','0','t','s'}
};
byte rowPins[ROWS] = {5, 6, 7, 8}; //row pins
byte colPins[COLS] = {9, 10, 11, 12}; //collom pins

Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 


LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

void write_byte(int DEVICEADDRESS ,uint32_t theMemoryAddress, uint8_t u8Byte) {

    Wire.beginTransmission(DEVICEADDRESS);
    Wire.write( (theMemoryAddress >> 8) & 0xFF );
    Wire.write( (theMemoryAddress >> 0) & 0xFF );
    Wire.write(u8Byte);
    Wire.endTransmission();
    delay(5);

}

uint8_t read_byte(int DEVICEADDRESS ,uint32_t theMemoryAddress) {
  uint8_t u8retVal = 10;
  Wire.beginTransmission(DEVICEADDRESS);
  Wire.write( (theMemoryAddress >> 8) & 0xFF );
  Wire.write( (theMemoryAddress >> 0) & 0xFF );
  Wire.endTransmission();
  delay(5);
  Wire.requestFrom(DEVICEADDRESS, 1);
  u8retVal = Wire.read();
  return u8retVal ;
}

int render_screen_acounts(int acount_id_at_top_of_screen, int selecter_pos_on_screen, int num_acounts, int fpsb){
  int fps = 1000/fpsb;
  delay(fps);
  int selected_id;
  int count;
  selected_id = acount_id_at_top_of_screen + selecter_pos_on_screen;//gets whitch acount the selcector arrow is on
  count = acount_id_at_top_of_screen;//starts with acount id at the top of the screen then loops through the outher acount ids to desplay on screen
  int pre_count = count;//acount id at the top of the screen
  lcd.clear();//resets screen
  
  while(count <= num_acounts){ //loops through all acounts ready to be displayed on screen
    lcd.setCursor(0, count-pre_count);//sets the Cursor to first char and the line num is dependent on how many times the loop has looped through
    if(selecter_pos_on_screen == count-pre_count){//displays the sellector on the right line
      lcd.setCursor(17, count-pre_count);// displays the selectore at the end of the lcd 
      lcd.print(" <-");
      lcd.setCursor(0, count-pre_count);// puts the cursor back to where it was befor the selector was desplayed
    }
    
    if(((count)-2) >= 0)
    {
      
      Serial.println((uint32_t(count-2)*uint32_t(10000))+1);
    }
    if((count - pre_count) == 3){
      break;
    }
    count ++;  
  }    
  return selected_id;
}

int select_acount(int fps){
  
  bool selecting = true;// loop var  loops throu all acounts
  write_byte(0x50, 0, 0);// testing will be romeved later
  int num_acounts = (int(read_byte(0x50, 0)));// gets num of acounts on eeprom
  //Serial.println(num_acounts);
  int selecter = 0; // selected pos on screen
  int ud = 2;//buffer if key held down it will wait till button is let go
  int scroll = 1;// acount at the top of the screen
  int selected = 1;//selected acount
  
  while(selecting){ // loops throu all acounts and renders them
    selected = render_screen_acounts(scroll, selecter, num_acounts, fps);
    char customKey1 = customKeypad.getKey();//gets kepad key press
   
    if (customKey1 == '2'){// sets buffer to up
      ud = 1;
    }
    if (customKey1 == '8'){//sets buffer to down
      ud = 3;
    }
    if (customKey1 == 'e'){//exits the loop and selects  acount
      selecting = false;
      lcd.clear();
    }
    if (customKeypad.getState() == IDLE){
      if(ud == 1 && selecter == 0){// 2 key is pressed
        scroll--;
        ud = 2;
        if(scroll < 1){
          scroll = 1;
        }
      } else {
        if(ud==1){
          selecter--;
          ud = 2;
        }
      }
      if(ud == 3 && selecter == 3){ // 8 key is pressed
        scroll++;
        ud = 2;
        if(scroll > num_acounts-3){
          scroll = num_acounts-3;
        }
      } else {
        if(ud==3){
          selecter++;
          ud = 2;
          if(selecter > num_acounts-1){
            selecter = num_acounts-1;
          }
        }
      }
    }
  } 
  return selected;
}

void setup(){
  Wire.begin();
  Serial.begin(2000000);
  lcd.begin(20,4);
  lcd.setCursor(0, 0);
  lcd.print("conecting");
  bool connecting = true;
  String comp = "";
  
  while(connecting){
    Serial.println("norec");
    while(Serial.available()>0){
       comp = comp + (char)Serial.read();
    }
    if(comp == "276894"){
      connecting = false;
      lcd.setCursor(0, 0);
      lcd.print("pluged in");
      delay(1000);
      Serial.println("req ard func");
    }
  }
}

void loop(){
  
}
