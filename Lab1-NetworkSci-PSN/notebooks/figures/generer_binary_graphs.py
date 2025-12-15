#!/usr/bin/env python3
"""Genererer figur med urettet og rettet graf med nabomatriser."""

import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Sett random seed for reproduserbarhet
np.random.seed(42)

# Sørg for at vi er i riktig mappe
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# ============================================================================
# FIKSERTE POSISJONER FOR NODENE
# ============================================================================
# Disse posisjonene sikrer at grafene tegnes likt hver gang.
# Posisjoner er (x, y) koordinater for hver node.
pos = {
    'a': (-1.0, 0.0),   # Venstre, midt
    'b': (-0.5, 1.0),   # Øverst venstre
    'c': (0.0, 0.0),    # Senter
    'd': (1.0, 1.0),    # Øverst høyre
    'e': (1.0, 0.0)     # Høyre, midt
}

fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1], hspace=0.3, wspace=0.3)

# Urettet graf
G_urettet = nx.Graph()
G_urettet.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('d', 'e')])

# Rettet graf
G_rettet = nx.DiGraph()
G_rettet.add_edges_from([('a', 'b'), ('b', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('e', 'd'), ('e', 'c')])

# Tegn urettet graf
ax1 = fig.add_subplot(gs[0, 0])
nx.draw(G_urettet, pos, ax=ax1, with_labels=True, node_color='lightblue', 
        node_size=800, font_size=14, font_weight='bold', edge_color='gray', width=2)
ax1.set_title('Urettet, binær graf', fontsize=14, fontweight='bold')
ax1.text(-1.15, -0.15, 'node', fontsize=13, style='italic', fontweight='bold')
ax1.text(-0.85, 0.55, 'kant', fontsize=13, style='italic', fontweight='bold')

# Tegn rettet graf
ax2 = fig.add_subplot(gs[0, 1])
nx.draw(G_rettet, pos, ax=ax2, with_labels=True, node_color='lightblue', 
        node_size=800, font_size=14, font_weight='bold', edge_color='gray', 
        width=2, arrows=True, arrowsize=20, connectionstyle='arc3,rad=0.1')
ax2.set_title('Rettet, binær graf', fontsize=14, fontweight='bold')

def lag_nabomatrise(G):
    noder = sorted(G.nodes())
    n = len(noder)
    matrise = np.zeros((n, n))
    for i, n1 in enumerate(noder):
        for j, n2 in enumerate(noder):
            if G.has_edge(n1, n2):
                matrise[i, j] = 1
    return matrise, noder

def tegn_nabomatrise(ax, matrise, noder):
    n = len(noder)
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(n - 0.5, -0.5)
    for i in range(n + 1):
        ax.axhline(i - 0.5, color='black', linewidth=1)
        ax.axvline(i - 0.5, color='black', linewidth=1)
    for i in range(n):
        for j in range(n):
            if matrise[i, j] == 1:
                ax.text(j, i, '1', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(noder, fontsize=12, fontweight='bold')
    ax.set_yticklabels(noder, fontsize=12, fontweight='bold')
    ax.xaxis.tick_top()
    ax.set_aspect('equal')

# Tegn nabomatriser
ax3 = fig.add_subplot(gs[1, 0])
matrise_u, noder = lag_nabomatrise(G_urettet)
tegn_nabomatrise(ax3, matrise_u, noder)

ax4 = fig.add_subplot(gs[1, 1])
matrise_r, noder = lag_nabomatrise(G_rettet)
tegn_nabomatrise(ax4, matrise_r, noder)

plt.tight_layout()
plt.savefig('binary_graphs_no.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print('✓ Figur lagret til figurer/binary_graphs_no.png')

