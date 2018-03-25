# Mario Benavides
# Status - Completed
# This program will calculate the distance in meters based on the object’s falling time.

Gravity = 9.8 
from distance import falling_distance # put in same folder


# main – will call the falling_distance function in a loop, passing it the values 1 – 10 as arguments
# (seconds the object has been falling).   
# It will display the returned distance.

def main():
    print("Time (seconds) \tDistance (meters)") # Header
    print("----------------------------------") # Line
    print() # Empty line

    for time in range (1,11): # 1 - 10
        distance = falling_distance(time)
        print(time, '\t\t', format(distance, ',.2f'))
       
#def falling_distance(time): 
#    g = Gravity
#    return (1/2*g*(time**2)) works if not pulled from file.
# ------------------------------------------------------------
#   print(distance.falling_distance(time))
		
main()
