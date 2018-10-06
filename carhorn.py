#testing git

import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)






try:
        while True:
                button_state23 = GPIO.input(23)
                if button_state23 == False:
                        print('Button 23 Pressed')
                        os.system('omxplayer /home/pi/sounds/Playful\ R2D2.mp3')
                        time.sleep(0.2)
                        
                button_state25 = GPIO.input(25)
                if button_state25 == False:
                        print('Button 25 Pressed')
                        os.system('omxplayer /home/pi/sounds/Cantina\ band.mp3')
                        time.sleep(0.2)
                        
                button_state12 = GPIO.input(12)
                if button_state12 == False:
                        print('button 12 pressed')
                        os.system('omxplayer /home/pi/sounds/Very\ Excited\ R2D2.mp3')
                        time.sleep(0.2)
                        
                    


except:
    GPIO.cleanup()
    
                    
