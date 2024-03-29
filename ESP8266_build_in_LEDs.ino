// Built-in LED Blinking

int LED1 = 2;      // Assign LED1 to pin GPIO2
int LED2 = 16;     // Assign LED2 to pin GPIO16

void setup() {

  // initialize GPIO2 and GPIO16 as an output
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {

  digitalWrite(LED1, LOW);
  digitalWrite(LED2, HIGH);

  delay(1000);

  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, LOW);

  delay(1000);
}
