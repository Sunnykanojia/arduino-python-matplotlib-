int analog = A0;
int data = 0;
void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  data = analogRead(analog);
  Serial.println(data);
  delay(100);
  if(data <= 753 )
  {
   digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level) 
  }
  else
  {
     digitalWrite(LED_BUILTIN, LOW);
  }
}
