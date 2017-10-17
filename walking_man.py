# Created by : Sidney Kang
# Created on : 16 Oct. 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-06
# This program displays a man walking when a button is pressed

import ui
import time

@ui.in_background
def walking_man_touch_up_inside(sender):
    # This makes man walk
   
    #variables 
    number_generated = 0
    counter = 10
    
    #process
    while number_generated < counter:
          if number_generated == 0:
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_1.bmp')
             number_generated = number_generated + 1                             
          elif number_generated == 1:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_2.bmp')                                                                                              
             number_generated = number_generated + 1                              
          elif number_generated == 2:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_3.bmp')
             number_generated = number_generated + 1                             
          elif number_generated == 3:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_4.bmp')
             number_generated = number_generated + 1                             
          elif number_generated == 4:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_5.bmp')
             number_generated = number_generated + 1                              
          elif number_generated == 5:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_6.bmp')
             number_generated = number_generated + 1                            
          elif number_generated == 6:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_7.bmp')
             number_generated = number_generated + 1                              
          elif number_generated == 7:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_8.bmp')
             number_generated = number_generated + 1                              
          elif number_generated == 8:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_9.bmp')
             number_generated = number_generated + 1                             
          elif number_generated == 9:
             time.sleep(0.15)
             #output
             view['man_walking_image'].image = ui.Image.named('./assets/sprites/walking_man_10.bmp')
             number_generated = 0                            
     
view = ui.load_view()
view.present('sheet')
