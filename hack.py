#The code in the docstring is the hardware code
def R_SENSOR(): 
    '''  # raindrop sensor DO connected to GPIO18
        # HIGH = no rain, LOW = rain detected
        # Buzzer on GPIO13
        from time import sleep
        from gpiozero import Buzzer, InputDevice
         
        buzz    = Buzzer(13)
        no_rain = InputDevice(18)
         
        def buzz_now(iterations):
            for x in range(iterations):
                buzz.on()
                sleep(0.1)
                buzz.off()
                sleep(0.1)
         
        while True:
            if not no_rain.is_active:
                print("It's raining")
                buzz_now(5)
            else:
                print("It's not raining")
            sleep(1) '''                  
    import random
    import time
    intlist=range(0,100)#create a list of 100 numbers
    i=0
    while(i<12):
        val=random.choice(intlist)#randomly choose a number from the list
        if(val>50):#group the numbers into 2 categories.>50 for raining..<50 for not raining
            return(True)
        time.sleep(10) #run the code every 10 secs for a total time limit of 2 mins
        i=i+1
    return(False)    
        
        
def P_SENSOR():
    '''
    import time
def P_SENSOR():
    def hard_pressure():
        import smbus

        bus = smbus.SMBus(1)

        # CPS120 address, 0x28(40)
        #		0x80(128)	 Select Start mode
        bus.write_byte(0x28, 0x80)

        # CPS120 address, 0x28(40)
        # Read data back from 0x00(0), 2 bytes, Pressure MSB first
        data = bus.read_i2c_block_data(0x28, 0x00, 2)

        # Convert the data to kPa
        pressure = (((data[0] & 0x3F) * 256 + data[1]) / 16384.0) * 90 + 30

        return pressure
    def compare(a,b):
        if(b-a<0):
            indication=1 #Shows the decrease
        else:
            indication=0 #Shows doesn't decrease
        return indication
    temp_list=[]
    i=0
    activate=0
    a=hard_pressure()
    while(i<12):
        b=hard_pressure()
        temp_list.append(a)
        temp_list.append(b)
        indication=compare(temp_list[i],temp_list[i+1])
        if(indication==1):
            activate+=1
        else:
            activate=0
        i+=1
        if(activate==3):
            rain=True
            return rain,temp_list
        time.sleep(10)
    rain=False
    return rain,temp_list'''
    
    import time
    '''To sense the changes in air pressure'''
    import random
    data=[1,2,3]# a list of values of mV which is used as a input for sensing rain
    def compare(a,b):
        '''To check the next number is smaller or larger'''
        if(b-a<0):
            indication=1 #Shows the decrease
        else:
            indication=0 #Shows doesn't decrease
        return indication
    def pressure(x):
        '''Used to convert milli volts into kilo pascals'''
        x=((x* 256) / 16384.0) * 90 + 30
        return x
    temp_list=[]#Creating an empty list to note all the values of pressure and compare
    a=random.choice(data)
    a=pressure(a)
    temp_list.append(a)
    i=0
    activate=0
    while(i<12):
        b=random.choice(data)
        b=pressure(b)
        temp_list.append(b)
        indication=compare(temp_list[i],temp_list[i+1])#To compare every consecutive digit
        if(indication==1):
            activate+=1
        else:
            activate=0
        i+=1
        if(activate==2):#Continuous decrease in pressure indicates rainfall 
            rain=True
            return rain,temp_list
        time.sleep(10)
    rain=False
    return rain,temp_list
  


def H_SENSOR():
       ''' #include <dht.h>
    
    dht DHT;
    
    #define DHT11_PIN 4
    
    void setup(){
      Serial.begin(9600);
    }
        void loop()
    {
      int chk = DHT.read11(DHT11_PIN);
      Serial.print("Temperature = ");
      Serial.println(DHT.temperature);
      Serial.print("Humidity = ");
      Serial.println(DHT.humidity);
      delay(2000);'''
    import random
    import time
        
    rand= range(18,87)#assuming a range of values to select from later
    
    i=0
    while(i<30):
        pw = random.choice(rand)#choosing a dummy value for partial pressure and saturation vapor pressure
        ps = random.choice(rand)
        hum= (pw/ps*100)#calculating the humidity based on the chosen values of ps and pw

        #at 25c, ps= 23.8mmHg
        #RH=(pw/ps)*100%; pw =partial pressure, ps= saturation vapour pressure
        #baseline humidity is 100%
        if(hum>100):
            return (True,hum)#if humidity is greater than a certain threshold it means rain is probable
        time.sleep(2)
        i=i+1             #iteration
    return(False)#if humidity is not over ceratin threshold , rain is not probable
  
k=0
print("Hi guys, System is executing in the background. Please wait...")
#executing the three functions for each of the sensors
RAIN=R_SENSOR()
HUMIDITY,HUM_VAL=H_SENSOR()
PRESSURE,PRES_LIST=P_SENSOR()
print("rain=",RAIN,"pressure",PRESSURE,"Humidity",HUMIDITY)
 
'''#considering a Brushed DC Motor 2 (RM2)RB-Sbo-49
#rpm speed=1620
#rps speed=27
#since we want the motors to rotate 60 degrees in five secinds, we have to make the motor rotate 12 degrees in one second
#this implies we have to make the motor run at 0.123455%operation power for 5 seconds to get the desired rotation

from gpiozero import Motor#importing the motor class to operate the motor
from time import sleep#importing sleep function from the time module

motor1 = Motor(forward=15, backward=18)#first motor uses the gpio pins numbered 15 for forward motion and 18 for backward motion
motor2 = Motor(forward=17,backward= 27)#first motor uses the gpio pins numbered 17 for forward motion and 27 for backward motion

if rain==True:
    
    motor1.forward(0.00123455)
    motor2.backward(0.00123455)
    sleep(5)

else:
    motor1.backward(0.00123455)
    motor2.forward(0.00123455)
    sleep(5)'''
import pylab
#we r goin to show how the angle rotated by the motor varies based on the time of operation, using a grahical plot of angle vs time
if(RAIN==True):
    print("open butterfly")
    timevalues1=pylab.linspace(0,5,50)#timevalues becomes like a list of 50 x coordinate values from 0 to 5
    angle1=pylab.linspace(0,60,50)#angle values change from zero to 60 based on the time
    pylab.plot(timevalues1,angle1)#plotting angle rotated vs time
    stationarytime1=pylab.linspace(5,10,50)#stationary time to show that the motor stops after rotating for 60 degrees
    stationaryangle1=pylab.linspace(60,60,50)#in stationary time angle remains same to show motor stops
    pylab.plot(stationarytime1,stationaryangle1)#plotting
    pylab.xlabel("time in seconds")#adding labels
    pylab.ylabel("angle each motor rotates")
    pylab.title("angle rotated by motor w.r.t. time operated")#title of graph
    pylab.grid(True)#to plot on a grid
    k=1
elif(HUMIDITY==True and PRESSURE==True):
    print("open butterfly")#exact execution as in above condition
    timevalues1=pylab.linspace(0,5,50)
    angle1=pylab.linspace(0,60,50)
    pylab.plot(timevalues1,angle1)
    stationarytime1=pylab.linspace(5,10,50)
    stationaryangle1=pylab.linspace(60,60,50)
    pylab.plot(stationarytime1,stationaryangle1)
    pylab.xlabel("time in seconds")
    pylab.ylabel("angle each motor rotates")
    pylab.title("angle rotated by motor w.r.t. time operated")
    pylab.grid(True)
   
    k=1
else:
    if(k==1):
        print("close butterfly")#in case the flaps are initially open and then due to no rain it has to close
        timevalues2=pylab.linspace(0,5,50)
        angle2=pylab.linspace(60,0,50)#since the motor moves in the backward direction for closing function,the angle made by the flap with the vertical will be decreasing from 60 degrees to zero
        pylab.plot(timevalues2,angle2)
        stationarytime2=pylab.linspace(5,10,50)
        stationaryangle2=pylab.linspace(0,0,50)#stationary motors due to completion of close function
        pylab.plot(stationarytime2,stationaryangle2)
        pylab.xlabel("time in seconds")
        pylab.ylabel("angle each motor rotates")
        pylab.title("angle rotated by motor w.r.t. time operated")
        pylab.grid(True)
    else:#in case the flaps are already closed and the random values generated
        
        timevalues3=pylab.linspace(0,10,50)
        angle3=pylab.linspace(0,0,50)
        pylab.plot(timevalues3,angle3)
        pylab.xlabel("time in seconds")
        pylab.ylabel("angle each motor rotates")
        pylab.title("angle rotated by motor w.r.t. time operated")
        pylab.grid(True)
        