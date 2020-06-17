print "Hello"


'''
# Your last C/C++ code is saved below:

# 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by over-population.
# 4. Any dead cell with exactly three live neighbors becomes a live cell,
# as if by reproduction.

# Example:
[
	[0,1,0],
	[0,0,1],
	[1,1,1],
	[0,0,0]
]
[
	[0,0,0],
	[1,0,1],
	[0,1,1],
	[0,1,0]
]
'''
def generate_state(input_arr):
  
  result = [[]]
  deltas = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

  for ind_parent, input in enumerate(input_arr):
    for ind, val in enumerate(input):
      neighbors = []
      
      count_alive = 0
      for delta in deltas:
        new_ind_parent = ind_parent + delta[0]
        new_ind = ind + delta[1]
    
        if new_ind_parent < 0 or new_ind_parent>len(input) :
          continue
        
        value_neighbor = input_arr[new_ind_parent][new_ind]
        neighbors.append(value_neighbor)
        count_alive = count_alive+1 if value_neighbor == 1 else count_alive
        # neighbors.append(input[ind+1])
        # neighbors.append(input_arr[ind_parent][ind_parent+1])
        # neighbors.append(input_arr[ind_parent+1][ind_parent+1])
      
      if count_alive <= 1:
        # 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        result[ind_parent[ind]] = 0
      elif count_alive in [2,3]:
        # 2. Any live cell with two or three live neighbors lives on to the next generation.
        # 4. Any dead cell with exactly three live neighbors becomes a live cell,
        result[ind_parent[ind]] = 1
      elif count_alive > 3:
        # 3. Any live cell with more than three live neighbors dies, as if by over-population.
        result[ind_parent[ind]] = 0

      
    return result
    

input_arr = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print generate_state(input_arr)