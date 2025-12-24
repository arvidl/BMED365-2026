#!/usr/bin/env python3
"""Generates figure with undirected and directed graph with adjacency matrices."""

import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

# Make sure we are in the correct folder
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# ============================================================================
# FIXED POSITIONS FOR THE NODES
# ============================================================================
# These positions ensure that the graphs are drawn the same way every time.
# Positions are (x, y) coordinates for each node.
pos = {
    'a': (-1.0, 0.0),   # Left, middle
    'b': (-0.5, 1.0),   # Top left
    'c': (0.0, 0.0),    # Center
    'd': (1.0, 1.0),    # Top right
    'e': (1.0, 0.0)     # Right, middle
}

fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1], hspace=0.3, wspace=0.3)

# Undirected graph
G_undirected = nx.Graph()
G_undirected.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('d', 'e')])

# Directed graph
G_directed = nx.DiGraph()
G_directed.add_edges_from([('a', 'b'), ('b', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('e', 'd'), ('e', 'c')])

# Draw undirected graph
ax1 = fig.add_subplot(gs[0, 0])
nx.draw(G_undirected, pos, ax=ax1, with_labels=True, node_color='lightblue', 
        node_size=800, font_size=14, font_weight='bold', edge_color='gray', width=2)
ax1.set_title('Undirected, binary graph', fontsize=14, fontweight='bold')
ax1.text(-1.15, -0.15, 'node', fontsize=13, style='italic', fontweight='bold')
ax1.text(-0.85, 0.55, 'edge', fontsize=13, style='italic', fontweight='bold')

# Draw directed graph
ax2 = fig.add_subplot(gs[0, 1])
nx.draw(G_directed, pos, ax=ax2, with_labels=True, node_color='lightblue', 
        node_size=800, font_size=14, font_weight='bold', edge_color='gray', 
        width=2, arrows=True, arrowsize=20, connectionstyle='arc3,rad=0.1')
ax2.set_title('Directed, binary graph', fontsize=14, fontweight='bold')

def create_adjacency_matrix(G):
    nodes = sorted(G.nodes())
    n = len(nodes)
    matrix = np.zeros((n, n))
    for i, n1 in enumerate(nodes):
        for j, n2 in enumerate(nodes):
            if G.has_edge(n1, n2):
                matrix[i, j] = 1
    return matrix, nodes

def draw_adjacency_matrix(ax, matrix, nodes):
    n = len(nodes)
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(n - 0.5, -0.5)
    for i in range(n + 1):
        ax.axhline(i - 0.5, color='black', linewidth=1)
        ax.axvline(i - 0.5, color='black', linewidth=1)
    for i in range(n):
        for j in range(n):
            if matrix[i, j] == 1:
                ax.text(j, i, '1', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(nodes, fontsize=12, fontweight='bold')
    ax.set_yticklabels(nodes, fontsize=12, fontweight='bold')
    ax.xaxis.tick_top()
    ax.set_aspect('equal')

# Draw adjacency matrices
ax3 = fig.add_subplot(gs[1, 0])
matrix_u, nodes = create_adjacency_matrix(G_undirected)
draw_adjacency_matrix(ax3, matrix_u, nodes)

ax4 = fig.add_subplot(gs[1, 1])
matrix_r, nodes = create_adjacency_matrix(G_directed)
draw_adjacency_matrix(ax4, matrix_r, nodes)

plt.tight_layout()
plt.savefig('binary_graphs_en.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print('✓ Figure saved to figures/binary_graphs_en.png')




