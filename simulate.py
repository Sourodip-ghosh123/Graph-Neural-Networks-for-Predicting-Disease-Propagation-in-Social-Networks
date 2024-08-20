import matplotlib.pyplot as plt
import networkx as nx

def simulate_spread(G, infected_nodes, steps=10):
    spread = [len(infected_nodes)]
    for _ in range(steps):
        new_infected = set()
        for node in infected_nodes:
            neighbors = list(G.neighbors(node))
            new_infected.update(neighbors)
        infected_nodes.update(new_infected)
        spread.append(len(infected_nodes))
    return spread

G = nx.read_gpickle('data/graphs/social_network_graph.gpickle')

# Initial infected nodes
infected_nodes = set([0])
spread = simulate_spread(G, infected_nodes)

plt.plot(spread)
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected Nodes')
plt.title('Disease Spread Over Time')
plt.show()

