def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    if not states:
        raise Exception('Empty states')
    
    if days < 0:
        raise Exception('Days cannot be less than 0')
    
    # if days == 1:
    #     return states

    n = len(states)
    for day in range(days):
        houses = [0] + states + [0]
        states = [houses[i-1] ^ houses[i+1] for i in range(1, n+1)]
    return states
    # for j in range(0, days):
    #     states = updateState(states)
        
    # #print '---------------------------', states
    
    # return states


def updateState(states):
    states[0] = 0
    
    for i in range(1, len(states)-1):
        if states[i+1] == states[i-1]:
            res = 1
        else:
            res = 0
        states[i] = res
    
    if states[len(states)-2] == 0:
        states[len(states)-1] = 1
    else:
        states[len(states)-1] = 0
    
    print states, "\n\n"
    return states

print cellCompete([1,0,0,0,0,1,0,0], 1)
print cellCompete([1,1,1,0,1,1,1,1], 2)