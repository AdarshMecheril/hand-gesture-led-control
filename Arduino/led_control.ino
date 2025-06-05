#define LED1 2  // Change these pins as per your circuit
#define LED2 3
#define LED3 4
#define LED4 5
#define LED5 6

void setup() {
    Serial.begin(9600);  // Start serial communication
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);
    pinMode(LED5, OUTPUT);
}
void loop() {
    if (Serial.available()) {
        int fingers = Serial.read() - '0';  // Convert received character to integer

        // Turn off all LEDs
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        digitalWrite(LED4, LOW);
        digitalWrite(LED5, LOW);

        // Turn on LEDs based on fingers detected
        if (fingers >= 1) digitalWrite(LED1, HIGH);
        if (fingers >= 2) digitalWrite(LED2, HIGH);
        if (fingers >= 3) digitalWrite(LED3, HIGH);
        if (fingers >= 4) digitalWrite(LED4, HIGH);
        if (fingers == 5) digitalWrite(LED5, HIGH);
    }
}
