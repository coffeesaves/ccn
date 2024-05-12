from gpio import *
from time import *

switchValue = 0
togglePushButtonValue = 0
potentiometerValue = 0
flexSensorValue = 0

def readFromSensors():
    global switchValue
    global togglePushButtonValue
    global potentiometerValue
    global flexSensorValue
    
    switchValue = digitalRead(0)
    togglePushButtonValue = digitalRead(1)
    potentiometerValue = analogRead(A0)
    flexSensorValue = analogRead(A1)

def writeToActuators():
    if switchValue == HIGH:
        customWrite(2, "2")
    else:
        customWrite(2, "0")

    if togglePushButtonValue == HIGH:
        digitalWrite(3, HIGH)
    else:
        digitalWrite(3, LOW)

    if potentiometerValue > 512:
        customWrite(4, HIGH)
    else:
        customWrite(4, LOW)

    if flexSensorValue > 0:
        analogWrite(5, flexSensorValue)
    else:
        analogWrite(5, 0)

def main():
    pinMode(0, IN)
    pinMode(1, IN)
    pinMode(2, OUT)
    pinMode(3, OUT)
    pinMode(4, OUT)
    
    while True:
        readFromSensors()
        writeToActuators()
        delay(1000)

if __name__ == "__main__":
    main()
