from time import sleep
import RPi.GPIO as GPIO
#step_count=0.0
#float(step_count)
#x=0.0
#float(x)
#range=0.0
#float(range)
DIR = 38
STEP =40
CW = 1
CCW = 0
#LOOP=1000 SPR =200
EN=37
M0=35
M1=33
M2=31
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN,GPIO.OUT)
GPIO.setup(M0,GPIO.OUT)
GPIO.setup(M1,GPIO.OUT)
GPIO.setup(M2,GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(EN, GPIO.LOW)
GPIO.output(DIR, GPIO.HIGH)
#step_count = SPR
#lp=LOOP
delay=0.0005
GPIO.output(M0,GPIO.LOW)
GPIO.output(M1,GPIO.LOW)
GPIO.output(M2,GPIO.LOW)
GPIO.output(EN, GPIO.LOW)
while(1):
 angle=input(' enter angle ')
 print(angle)
 step_count=float((angle)/(1.8))
 #step_count=input(' enter no of steps ')
 print(round(step_count))
 step_count=round(step_count)
 step_count=int(step_count)
 print(step_count)

# print(int(step_count))
 if step_count > 0:
  for x in range(step_count):
   GPIO.output(EN, GPIO.LOW)
   GPIO.output(DIR, GPIO.HIGH)
   print('seedha ghumo')
   GPIO.output(STEP, GPIO.HIGH)
   print('mai high hu')
   sleep(delay)
   GPIO.output(STEP, GPIO.LOW)
   print('mai low hu')
   sleep(delay)
  sleep(0.5)
 else:
  step_count=(step_count)*(-1)
    #GPIO.output(DIR, GPIO.LOW)
    # print('ulta ghumo')
  for x in range(step_count):
   GPIO.output(DIR, GPIO.LOW)
   print('ulta ghumo')
   GPIO.output(EN, GPIO.LOW)
   GPIO.output(DIR, GPIO.LOW)
   GPIO.output(STEP, GPIO.HIGH)
   print('mai ulta high hu')
   sleep(delay)
   GPIO.output(STEP, GPIO.LOW)
   print('mai ulta low hu')
   sleep(delay)
  sleep(0.5)
GPIO.output(EN,GPIO.HIGH)
GPIO.cleanup()

