class Solution(object):
    def criticalConnections(self, n, connections):
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        
        pre = [-1 for i in range(n)]
        low = [-1 for i in range(n)]
        order = 0    
        ans = []
        
        def dfs(par, cur, order):
            order += 1
            pre[cur] = order
            low[cur] = pre[cur]
            for w in graph[cur]:
                if (pre[w] == -1):
                    dfs(cur, w, order)
                    low[cur] = min(low[cur], low[w])
                    if (low[w] == pre[w]):
                        ans.append((cur, w))
                
                elif (w != par):
                    low[cur] = min(low[cur], pre[w])
        
        dfs(0, 0, 0) # this can be any random node, since from one node can reach any other node, dfs(1, 1, 0) will also work

        return ans
#     def criticalConnections(self, n, connections):
#         """
#         :type n: int
#         :type connections: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         node_dict = {}
        
#         for connection in connections:
#             if connection[0] in node_dict:
#                 node_dict[connection[0]] += 1
#             else:
#                 node_dict[connection[0]] = 1
                
#             if connection[1] in node_dict:
#                 node_dict[connection[1]] += 1
#             else:
#                 node_dict[connection[1]] = 1
        
#         print node_dict
#         result = []
#         for connection in connections:
#             if node_dict[connection[0]] == 1 or node_dict[connection[1]] == 1:
#                 result.append(connection)
        
#         return result