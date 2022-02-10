def distance():
    #distance=speed*time 
    speed=1100 #ft/sec
    mile=5280 #ft
    t=eval(input("Please write the how long it took for the flash of lightning to occur versus when you heard the thunder, in seconds:"))
    distance=t*speed
    print("The distance from the lightning strike is:",round(distance/mile),"miles away")
distance()


