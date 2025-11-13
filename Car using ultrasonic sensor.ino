// // Define IR sensor pins
// #define IR_LEFT A0
// #define IR_RIGHT A1

// Define ultrasonic sensor pins
#define TRIG_PIN 2
#define ECHO_PIN 3

// Motor driver pins
int enA = 9;
int in1 = 7;
int in2 = 6;
int enB = 10;
int in3 = 5;
int in4 = 4;


// Variables to store sensor values
int left_ir, right_ir;
long duration;
int distance;

void setup() {
  // pinMode(IR_LEFT, INPUT);
  // pinMode(IR_RIGHT, INPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  
  // Initialize motor pins
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}

void loop() {
  // Read line sensors
  // left_ir = digitalRead(IR_LEFT);
  // right_ir = digitalRead(IR_RIGHT);
  
  // Read obstacle sensor
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2; // Distance in cm
  
  // Obstacle avoidance
  if (distance < 50) {
    stopMotors();
  }
  // Line following logic
  else if (left_ir == LOW && right_ir == LOW) {
    moveForward();
  }
  else if (left_ir == LOW && right_ir == HIGH) {
    turnLeft();
  }
  else if (left_ir == HIGH && right_ir == LOW) {
    turnRight();
  }
  else {
    stopMotors();
  }
}

void moveForward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 150); // Adjust speed as required
  analogWrite(enB, 150);
}
void turnLeft() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 100);
  analogWrite(enB, 150);
}
void turnRight() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(enA, 150);
  analogWrite(enB, 100);
}
void stopMotors() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}