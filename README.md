# **Graph Neural Networks for Predicting Disease Propagation**

Welcome to the **Graph Neural Networks for Predicting Disease Propagation** project! This repository contains code and resources for modeling and predicting the spread of diseases within social networks using Graph Neural Networks (GNNs). The project aims to identify key influencers in disease propagation and test various intervention strategies to minimize the spread.

## **Project Overview**

Disease propagation in social networks is a critical area of study, particularly for understanding and controlling the spread of infectious diseases. In this project, we use Graph Neural Networks to model the interactions between individuals (nodes) and their relationships (edges) to predict the spread of diseases and identify key influencers (super-spreaders) within the network.

### **Objectives**
- **Model Disease Propagation:** Predict the likelihood of disease transmission between individuals based on social interactions.
- **Identify Super-Spreaders:** Use graph analysis to find key nodes that play significant roles in spreading the disease.
- **Simulate Intervention Strategies:** Test various strategies, such as targeted vaccinations, to minimize disease spread.

## **Features**

- **Graph Construction:** Build a social network graph from interaction data.
- **GNN Model:** Train a Graph Neural Network to predict disease spread.
- **Simulation:** Visualize disease propagation and evaluate the impact of different intervention strategies.
- **Analysis:** Identify super-spreaders and analyze the effectiveness of interventions.

## **Installation**

To get started, clone this repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/graph-disease-propagation.git
cd graph-disease-propagation
pip install -r requirements.txt
