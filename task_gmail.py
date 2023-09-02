
from pyautogui import *
from time import*

def function():
    sleep(4)
    print(position())

# function()



# oint(x=19, y=96) for chrome icon
sleep(1)
click(41,143)
sleep(1)
cord=None
while cord is None:
    cord=locateOnScreen("/home/ahmed/work/python_workspace/session3_task/gmail.png",confidence=0.7)
if cord is not None:
    x=cord[0]
    y=cord[1] 

sleep(3)
click(x,y) 
# ***********************************************************************************      
# # Point(x=1473, y=174) for search bar
sleep(1)
move(1473,174)  
sleep(1)
click(1473,174)
sleep(1)
write("is:unread")
sleep(1)
press("Enter")
# *************************************************************************
sleep(4)
# Point(x=1815, y=300) for select all button
click(1815,300)
sleep(2)
# Point(x=1326, y=294) for tripple colum
click(1326,294)
sleep(2)
# then click
# click
# Point(x=1286, y=334) for read 
click(1286,334)
