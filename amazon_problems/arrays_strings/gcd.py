def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    lenarr = len(arr)
    
    if lenarr < 0:
        raise Exception("Array cannot be blank")
    
    if lenarr == 1:
        return arr[0]
    
    initx = arr[0]
    inity = arr[1]
    init_gcd = calcGCD(initx, inity)
    
    if lenarr == 2:
        return init_gcd

    for i in range(2, lenarr):
        final_gcd = calcGCD(init_gcd, arr[i])
    
    #print final_gcd
    
    return final_gcd

def calcGCD(valx, valy):
    if valy < 0 or valx < 0:
        raise Exception("Only positive integers allowed.")

    while valy:
        valx, valy = valy, valx % valy
        
    return valx