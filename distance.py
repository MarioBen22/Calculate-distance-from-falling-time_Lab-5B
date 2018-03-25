# import distance.py
# falling_distance – will be passed one parameter which is the time in seconds the object has been falling 
# and will calculate and return the distance in meters.    
# falling_distance should be stored in a separate file (module) called distance.py   
# You will import distance before your main function in your original program file.

Gravity = 9.8 # otherwise gravity was not defined

def falling_distance(time): 
    g = Gravity
    return (1/2*g*(time**2))
