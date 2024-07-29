import networkx as nx
import matplotlib.pyplot as plt

def colorearGrafo(Vertices, adyacencias):
    colores = {v: 0 for v in vertices}
    colores[vertices[0]] = 1
    print(f"Asignar color 1 al vertice {vertices[0]}")
    
    for v in vertices [1:]:
        coloresVecinos = {colores[u] for u in adyacencias[v] if colores [u] != 0}
        color = 1
        while color in coloresVecinos:
            color += 1
        colores[v] = color 
        print(f"Asignar color {color} al vértice {v} (vecinos: {adyacencias[v]})")
        
    return colores

vertices = ['v1', 'v2', 'v3', 'v4', 'v5']
adyacencias = {
    'v1': ['v2', 'v3'],
    'v2': ['v1', 'v3', 'v4'],
    'v3': ['v1', 'v2'],
    'v4': ['v2', 'v5'],
    'v5': ['v2', 'v4'],
    }

colores = colorearGrafo(vertices, adyacencias)
print("\nResultado final de colores:", colores)
G = nx.Graph()
for vertice in vertices:
    G.add_node(vertice)
for vertice, vecinos in adyacencias.items():
    for vecino in vecinos:
        G.add_edge(vertice, vecino)
color_map = []
for vertice in G:
    color_map.append(colores[vertice])
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=500, cmap=plt.cm.jet)
plt.show()
