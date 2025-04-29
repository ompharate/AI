
class DisJoinSet:
    def __init__(self,n):
        self.parent = list(range(n))

    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
                self.parent[root_v] = root_u


def kruskal(n,edges):
    ds = DisJoinSet(n)
    mst = []
    edges.sort()
    total = 0


    for weight,u,v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u,v)
            mst.append((u,v,weight))
            total += weight
    return mst,total



edges = []

nodes = int(input("Enter number of nodes:"))
n = int(input("Enter number of edges:"))
for _ in range(n):
        weight,u,v = map(int,input("weight u v:").split())
        edges.append((weight,u,v))


mst, total = kruskal(nodes, edges)
print("Edges in MST:", mst)
print("Total weight of MST:", total)




# Time Complexity: O(E log E) where E is the number of edges.