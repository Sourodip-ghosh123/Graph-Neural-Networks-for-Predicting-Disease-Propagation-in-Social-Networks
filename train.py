import torch
from torch_geometric.data import Data
from torch_geometric.utils import from_networkx
import networkx as nx
from models import GNN

G = nx.read_gpickle('data/graphs/social_network_graph.gpickle')
data = from_networkx(G)

model = GNN(in_channels=data.num_node_features, hidden_channels=16, out_channels=2)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

def train():
    model.train()
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)
    loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()
    return loss

for epoch in range(200):
    loss = train()
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')

torch.save(model.state_dict(), "src/model.pth")

