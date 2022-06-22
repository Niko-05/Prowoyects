name = "Nick"
time = 19
salute = ""

if time < 12:
    salute = "Good morning"
elif time > 12 and time < 18:
    salute = "Good afternoon"
else:
    salute = "Good evening"
    
print(salute + " " + name)