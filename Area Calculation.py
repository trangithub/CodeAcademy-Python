
# coding: utf-8

# In[1]:


print ("Let's calculate some area:")

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Starting the calculator ..."

print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle:")

option = option.upper()

if option == 'C':
  radius = float(raw_input("Enter radius:"))
  area = radius ** 2 * pi
  print "The pie is baking ..."
  sleep(1)  
  print ("Area: %.2f \n%s") % (area,hint)
elif option == 'T':
  base = float(raw_input("Enter base:"))
  height = float(raw_input("Enter height:"))  
  area = base * height * 0.5
  print "Uni Bi Tri..."
  sleep(1)
  print ("Area: %.2f \n%s") % (area,hint)
else: 
  print "Invalid shape. Please enter again:"

