from math import factorial

n = 2048  

collision_probability_threshold = 0.75

for i in range(n):
    probability_no_collision = 1.0
    
    
    for j in range(i):
        probability_no_collision *= (n - j) / n
    
    probability_collision = 1 - probability_no_collision

    if probability_collision > collision_probability_threshold:
        print(i)
        break
