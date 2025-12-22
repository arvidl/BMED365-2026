# ============================================================================
# 🎓 INTERACTIVE LEARNING MODULE: GRAPH THEORY IN MEDICINE
# ============================================================================
# This module contains:
# - Interactive slides with quizzes
# - Graph builder where you can create your own networks
# - Centrality calculator with visualization
# - Parameter sliders for network experimentation
# ============================================================================

from IPython.display import display, Markdown, HTML, clear_output
import ipywidgets as widgets
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import random

# ============================================================================
# MAIN CLASS: Interactive Learning Module
# ============================================================================

class InteractiveLearningModule:
    """An interactive learning module about graph theory in medicine."""
    
    def __init__(self):
        self.current_section = 0
        self.quiz_points = 0
        self.total_quizzes = 0
        self.completed_sections = set()
        
        # The graph used in the graph builder
        self.user_graph = nx.Graph()
        self.user_graph.add_nodes_from(['Patient A', 'Patient B', 'Patient C'])
        
        # Create sections
        self.sections = self._create_sections()
        
        # CSS for better formatting
        display(HTML("""
        <style>
            .quiz-correct { background-color: #d4edda !important; border: 2px solid #28a745 !important; }
            .quiz-wrong { background-color: #f8d7da !important; border: 2px solid #dc3545 !important; }
            .section-complete { color: #28a745; }
            .progress-bar { 
                background: linear-gradient(90deg, #4CAF50 var(--progress), #e0e0e0 var(--progress));
                height: 10px; border-radius: 5px; margin: 10px 0;
            }
        </style>
        """))
        
        self._show_main_menu()
    
    # =========================================================================
    # MAIN MENU AND NAVIGATION
    # =========================================================================
    
    def _show_main_menu(self):
        """Show the main menu with section selection."""
        clear_output(wait=True)
        
        # Header
        display(HTML("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; border-radius: 10px; margin-bottom: 20px;">
            <h1 style="margin: 0;">🎓 Graph Theory in Medicine</h1>
            <p style="margin: 10px 0 0 0; font-size: 1.1em;">Interactive Learning Module</p>
        </div>
        """))
        
        # Progress indicator
        completed = len(self.completed_sections)
        total = len(self.sections)
        percent = int(100 * completed / total) if total > 0 else 0
        
        display(HTML(f"""
        <div style="margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 8px;">
            <strong>📊 Your Progress:</strong> {completed}/{total} sections completed ({percent}%)
            <div style="background: #e0e0e0; height: 10px; border-radius: 5px; margin-top: 10px;">
                <div style="background: linear-gradient(90deg, #4CAF50, #8BC34A); height: 100%; 
                           width: {percent}%; border-radius: 5px; transition: width 0.5s;"></div>
            </div>
            <p style="margin-top: 10px;">🏆 <strong>Quiz Points:</strong> {self.quiz_points} correct answers</p>
        </div>
        """))
        
        # Section buttons
        display(HTML("<h3>📚 Choose a section:</h3>"))
        
        for i, section in enumerate(self.sections):
            completed_mark = "✅ " if i in self.completed_sections else ""
            button = widgets.Button(
                description=f"{completed_mark}{section['title']}",
                layout=widgets.Layout(width='100%', height='50px'),
                style={'button_color': '#e8f5e9' if i in self.completed_sections else '#e3f2fd'}
            )
            button.on_click(lambda _, idx=i: self._show_section(idx))
            display(button)
    
    def _show_section(self, idx):
        """Show a specific section."""
        self.current_section = idx
        section = self.sections[idx]
        
        clear_output(wait=True)
        
        # Navigation buttons
        nav_buttons = widgets.HBox([
            widgets.Button(description='🏠 Main Menu', layout=widgets.Layout(width='120px')),
            widgets.Button(description='← Previous', layout=widgets.Layout(width='100px')),
            widgets.HTML(value=f'<h4 style="margin: 0 20px;">Section {idx + 1}/{len(self.sections)}</h4>'),
            widgets.Button(description='Next →', layout=widgets.Layout(width='100px'))
        ], layout=widgets.Layout(justify_content='center', margin='10px 0'))
        
        nav_buttons.children[0].on_click(lambda _: self._show_main_menu())
        nav_buttons.children[1].on_click(lambda _: self._show_section(max(0, idx - 1)))
        nav_buttons.children[3].on_click(lambda _: self._show_section(min(len(self.sections) - 1, idx + 1)))
        
        display(nav_buttons)
        
        # Section title
        display(HTML(f"""
        <div style="text-align: center; padding: 15px; background: #f0f4f8; border-radius: 8px; margin: 10px 0;">
            <h2 style="margin: 0; color: #2c3e50;">{section['title']}</h2>
        </div>
        """))
        
        # Show section content
        section['content']()
        
        # Mark as completed
        self.completed_sections.add(idx)
    
    # =========================================================================
    # QUIZ SYSTEM
    # =========================================================================
    
    def _create_quiz(self, question, options, correct_index, explanation):
        """Create an interactive quiz question."""
        quiz_output = widgets.Output()
        
        display(HTML(f"""
        <div style="background: #fff3e0; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800; margin: 15px 0;">
            <strong>❓ Quiz:</strong> {question}
        </div>
        """))
        
        buttons = []
        for i, opt in enumerate(options):
            button = widgets.Button(
                description=opt,
                layout=widgets.Layout(width='100%', height='40px', margin='5px 0'),
                style={'button_color': '#e3f2fd'}
            )
            
            def check_answer(_, idx=i):
                with quiz_output:
                    clear_output()
                    if idx == correct_index:
                        self.quiz_points += 1
                        display(HTML(f"""
                        <div style="background: #d4edda; padding: 15px; border-radius: 8px; 
                                    border-left: 4px solid #28a745; margin: 10px 0;">
                            <strong>✅ Correct!</strong><br>{explanation}
                        </div>
                        """))
                    else:
                        display(HTML(f"""
                        <div style="background: #f8d7da; padding: 15px; border-radius: 8px; 
                                    border-left: 4px solid #dc3545; margin: 10px 0;">
                            <strong>❌ Not quite.</strong> Correct answer: <em>{options[correct_index]}</em><br>{explanation}
                        </div>
                        """))
                    self.total_quizzes += 1
            
            button.on_click(check_answer)
            buttons.append(button)
            display(button)
        
        display(quiz_output)
    
    # =========================================================================
    # INTERACTIVE GRAPH BUILDER
    # =========================================================================
    
    def _show_graph_builder(self):
        """Show an interactive graph builder."""
        display(HTML("""
        <div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <h3 style="margin-top: 0;">🔨 Build Your Own Patient Similarity Network</h3>
            <p>Use the tools below to add patients and connections between them.</p>
        </div>
        """))
        
        graph_output = widgets.Output()
        
        # Add node
        new_node_input = widgets.Text(placeholder='Patient name (e.g., "Patient D")', layout=widgets.Layout(width='200px'))
        add_node_button = widgets.Button(description='➕ Add Patient', style={'button_color': '#4CAF50'})
        
        # Add edge
        node1_dropdown = widgets.Dropdown(options=list(self.user_graph.nodes()), description='From:')
        node2_dropdown = widgets.Dropdown(options=list(self.user_graph.nodes()), description='To:')
        add_edge_button = widgets.Button(description='🔗 Connect Patients', style={'button_color': '#2196F3'})
        
        # Remove edge
        remove_edge_button = widgets.Button(description='✂️ Remove Connection', style={'button_color': '#f44336'})
        
        # Reset
        reset_button = widgets.Button(description='🔄 Reset', style={'button_color': '#9e9e9e'})
        
        def update_dropdowns():
            nodes = list(self.user_graph.nodes())
            node1_dropdown.options = nodes
            node2_dropdown.options = nodes
        
        def draw_graph():
            with graph_output:
                clear_output(wait=True)
                fig, ax = plt.subplots(figsize=(8, 6))
                
                if len(self.user_graph.nodes()) > 0:
                    pos = nx.spring_layout(self.user_graph, seed=42)
                    nx.draw(self.user_graph, pos, ax=ax, with_labels=True,
                           node_color='lightblue', node_size=2000, font_size=10,
                           font_weight='bold', edge_color='gray', width=2)
                    
                    # Show statistics
                    ax.set_title(f'Nodes: {self.user_graph.number_of_nodes()} | '
                                f'Edges: {self.user_graph.number_of_edges()}', fontsize=12)
                else:
                    ax.text(0.5, 0.5, 'No nodes yet.\nAdd patients!', 
                           ha='center', va='center', fontsize=14)
                    ax.axis('off')
                
                plt.tight_layout()
                plt.show()
        
        def add_node(_):
            name = new_node_input.value.strip()
            if name and name not in self.user_graph.nodes():
                self.user_graph.add_node(name)
                new_node_input.value = ''
                update_dropdowns()
                draw_graph()
        
        def add_edge(_):
            if node1_dropdown.value and node2_dropdown.value:
                if node1_dropdown.value != node2_dropdown.value:
                    self.user_graph.add_edge(node1_dropdown.value, node2_dropdown.value)
                    draw_graph()
        
        def remove_edge(_):
            if node1_dropdown.value and node2_dropdown.value:
                if self.user_graph.has_edge(node1_dropdown.value, node2_dropdown.value):
                    self.user_graph.remove_edge(node1_dropdown.value, node2_dropdown.value)
                    draw_graph()
        
        def reset(_):
            self.user_graph.clear()
            self.user_graph.add_nodes_from(['Patient A', 'Patient B', 'Patient C'])
            update_dropdowns()
            draw_graph()
        
        add_node_button.on_click(add_node)
        add_edge_button.on_click(add_edge)
        remove_edge_button.on_click(remove_edge)
        reset_button.on_click(reset)
        
        # Layout
        display(widgets.HBox([new_node_input, add_node_button]))
        display(widgets.HBox([node1_dropdown, node2_dropdown, add_edge_button, remove_edge_button]))
        display(reset_button)
        display(graph_output)
        
        draw_graph()
    
    # =========================================================================
    # CENTRALITY CALCULATOR
    # =========================================================================
    
    def _show_centrality_calculator(self):
        """Show an interactive centrality calculator."""
        display(HTML("""
        <div style="background: #fff3e0; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <h3 style="margin-top: 0;">📊 Centrality Calculator</h3>
            <p>See how different centrality measures identify "important" nodes in a network.</p>
        </div>
        """))
        
        # Create example network
        G = nx.karate_club_graph()
        
        centrality_dropdown = widgets.Dropdown(
            options=[
                ('Degree Centrality (number of connections)', 'degree'),
                ('Betweenness Centrality (bridge nodes)', 'betweenness'),
                ('Closeness Centrality (distance to others)', 'closeness'),
                ('Eigenvector Centrality (important neighbors)', 'eigenvector')
            ],
            value='degree',
            description='Choose measure:'
        )
        
        output = widgets.Output()
        
        def update_visualization(change):
            with output:
                clear_output(wait=True)
                
                # Calculate centrality
                if change['new'] == 'degree':
                    centrality = nx.degree_centrality(G)
                    title = "Degree Centrality"
                    explanation = "Nodes with many connections are large/dark."
                elif change['new'] == 'betweenness':
                    centrality = nx.betweenness_centrality(G)
                    title = "Betweenness Centrality"
                    explanation = "Nodes that lie on many shortest paths are important 'bridges'."
                elif change['new'] == 'closeness':
                    centrality = nx.closeness_centrality(G)
                    title = "Closeness Centrality"
                    explanation = "Nodes with short distance to all others can spread information quickly."
                else:
                    centrality = nx.eigenvector_centrality(G, max_iter=1000)
                    title = "Eigenvector Centrality"
                    explanation = "Nodes connected to other important nodes are themselves important."
                
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
                
                # Graph visualization
                pos = nx.spring_layout(G, seed=42)
                values = list(centrality.values())
                
                nx.draw(G, pos, ax=ax1, with_labels=True,
                       node_color=values, cmap=plt.cm.YlOrRd,
                       node_size=[v * 3000 + 300 for v in values],
                       font_size=8, edge_color='lightgray')
                ax1.set_title(f'{title}\n{explanation}', fontsize=11)
                
                # Bar chart
                sorted_data = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]
                nodes, values = zip(*sorted_data)
                colors = plt.cm.YlOrRd([v/max(values) for v in values])
                ax2.barh(range(len(nodes)), values, color=colors)
                ax2.set_yticks(range(len(nodes)))
                ax2.set_yticklabels([f'Node {n}' for n in nodes])
                ax2.set_xlabel('Centrality Value')
                ax2.set_title('Top 10 Most Central Nodes')
                ax2.invert_yaxis()
                
                plt.tight_layout()
                plt.show()
                
                # Explanation
                display(HTML(f"""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 5px; margin-top: 10px;">
                    <strong>💡 Interpretation:</strong> Node {sorted_data[0][0]} has the highest {title.lower()} 
                    ({sorted_data[0][1]:.3f}), while node {sorted_data[-1][0]} has the lowest among the top 10 ({sorted_data[-1][1]:.3f}).
                </div>
                """))
        
        centrality_dropdown.observe(update_visualization, names='value')
        display(centrality_dropdown)
        display(output)
        
        # Trigger initial visualization
        update_visualization({'new': 'degree'})
    
    # =========================================================================
    # NETWORK PARAMETER EXPERIMENT
    # =========================================================================
    
    def _show_network_experiment(self):
        """Let the user experiment with network parameters."""
        display(HTML("""
        <div style="background: #f3e5f5; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <h3 style="margin-top: 0;">🧪 Experiment with Networks</h3>
            <p>Adjust the sliders to see how different parameters affect network structure.</p>
        </div>
        """))
        
        # Sliders
        num_nodes = widgets.IntSlider(value=20, min=5, max=50, description='Number of patients:',
                                       style={'description_width': '140px'})
        connections = widgets.FloatSlider(value=0.2, min=0.05, max=0.5, step=0.05, 
                                          description='Connection probability:',
                                          style={'description_width': '140px'})
        network_type = widgets.Dropdown(
            options=[
                ('Random network', 'random'),
                ('Scale-free (hubs)', 'scalefree'),
                ('Small-world', 'smallworld')
            ],
            value='random',
            description='Network type:',
            style={'description_width': '140px'}
        )
        
        output = widgets.Output()
        
        def update(change=None):
            with output:
                clear_output(wait=True)
                
                n = num_nodes.value
                p = connections.value
                
                # Generate network
                if network_type.value == 'random':
                    G = nx.erdos_renyi_graph(n, p)
                    description = f"Random network: {n} nodes, {p:.0%} connection probability"
                elif network_type.value == 'scalefree':
                    G = nx.barabasi_albert_graph(n, max(1, int(n * p / 2)))
                    description = f"Scale-free: {n} nodes with preferential attachment"
                else:
                    G = nx.watts_strogatz_graph(n, max(2, int(n * p)), 0.3)
                    description = f"Small-world: {n} nodes with local clustering"
                
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
                
                # Network visualization
                pos = nx.spring_layout(G, seed=42)
                degrees = dict(G.degree())
                node_sizes = [degrees[n] * 50 + 100 for n in G.nodes()]
                node_colors = [degrees[n] for n in G.nodes()]
                
                nx.draw(G, pos, ax=ax1, with_labels=False,
                       node_color=node_colors, cmap=plt.cm.YlOrRd,
                       node_size=node_sizes, edge_color='lightgray', alpha=0.8)
                ax1.set_title(description)
                
                # Degree distribution
                degree_list = [d for n, d in G.degree()]
                ax2.hist(degree_list, bins=range(max(degree_list) + 2), 
                        edgecolor='white', color='steelblue', alpha=0.7)
                ax2.set_xlabel('Number of connections (degree)')
                ax2.set_ylabel('Number of patients')
                ax2.set_title('Degree Distribution: How many connections does each patient have?')
                
                plt.tight_layout()
                plt.show()
                
                # Network statistics
                display(HTML(f"""
                <div style="display: flex; gap: 20px; margin-top: 15px;">
                    <div style="flex: 1; background: #e8f5e9; padding: 10px; border-radius: 5px; text-align: center;">
                        <strong>Number of edges</strong><br><span style="font-size: 1.5em;">{G.number_of_edges()}</span>
                    </div>
                    <div style="flex: 1; background: #e3f2fd; padding: 10px; border-radius: 5px; text-align: center;">
                        <strong>Average degree</strong><br><span style="font-size: 1.5em;">{np.mean(degree_list):.1f}</span>
                    </div>
                    <div style="flex: 1; background: #fff3e0; padding: 10px; border-radius: 5px; text-align: center;">
                        <strong>Clustering coefficient</strong><br><span style="font-size: 1.5em;">{nx.average_clustering(G):.3f}</span>
                    </div>
                    <div style="flex: 1; background: #fce4ec; padding: 10px; border-radius: 5px; text-align: center;">
                        <strong>Components</strong><br><span style="font-size: 1.5em;">{nx.number_connected_components(G)}</span>
                    </div>
                </div>
                """))
        
        num_nodes.observe(update, names='value')
        connections.observe(update, names='value')
        network_type.observe(update, names='value')
        
        display(widgets.VBox([network_type, num_nodes, connections]))
        display(output)
        
        update()
    
    # =========================================================================
    # SECTION DEFINITIONS
    # =========================================================================
    
    def _create_sections(self):
        """Create all sections in the learning module."""
        return [
            {
                "title": "1️⃣ What is a Graph?",
                "content": self._section_1_basics
            },
            {
                "title": "2️⃣ Build Your Own Graph",
                "content": self._section_2_graph_builder
            },
            {
                "title": "3️⃣ Centrality Measures",
                "content": self._section_3_centrality
            },
            {
                "title": "4️⃣ Experiment with Networks",
                "content": self._section_4_experiment
            },
            {
                "title": "5️⃣ Medical Applications",
                "content": self._section_5_medicine
            },
            {
                "title": "6️⃣ Final Quiz",
                "content": self._section_6_quiz
            }
        ]
    
    # =========================================================================
    # SECTION 1: Graph Basics
    # =========================================================================
    
    def _section_1_basics(self):
        display(HTML("""
        <div style="line-height: 1.8;">
            <h3>🔷 The Building Blocks of Graph Theory</h3>
            <p>A <strong>graph</strong> is a mathematical structure that describes <em>relationships</em> between objects.</p>
            
            <div style="display: flex; gap: 20px; margin: 20px 0;">
                <div style="flex: 1; background: #e3f2fd; padding: 15px; border-radius: 8px;">
                    <h4 style="margin-top: 0;">🔵 Nodes (vertices)</h4>
                    <p>The objects we study:</p>
                    <ul>
                        <li>Patients</li>
                        <li>Diseases</li>
                        <li>Symptoms</li>
                        <li>Proteins</li>
                    </ul>
                </div>
                <div style="flex: 1; background: #fff3e0; padding: 15px; border-radius: 8px;">
                    <h4 style="margin-top: 0;">➖ Edges</h4>
                    <p>Connections between nodes:</p>
                    <ul>
                        <li>Patient similarity</li>
                        <li>Disease-symptom</li>
                        <li>Protein interaction</li>
                        <li>Drug-side effect</li>
                    </ul>
                </div>
            </div>
        </div>
        """))
        
        # Example graph
        fig, ax = plt.subplots(figsize=(8, 5))
        G = nx.Graph()
        G.add_edges_from([('Patient', 'Diabetes'), ('Patient', 'Hypertension'), 
                          ('Diabetes', 'Hypertension'), ('Diabetes', 'Obesity')])
        pos = {'Patient': (0, 0), 'Diabetes': (1, 1), 'Hypertension': (1, -1), 'Obesity': (2, 1)}
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue',
               node_size=3000, font_size=11, font_weight='bold', edge_color='gray', width=2)
        ax.set_title('Example: Patient-Disease Network', fontsize=12)
        plt.tight_layout()
        plt.show()
        
        # Quiz
        self._create_quiz(
            "What does an **edge** represent in a patient similarity network?",
            ["A patient", "A disease", "A connection/similarity between two patients", "A symptom"],
            2,
            "Correct! Edges represent relationships – in a patient similarity network, an edge means that two patients have similar characteristics."
        )
        
        # Reflection question
        display(HTML("""
        <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin-top: 20px; border-left: 4px solid #9c27b0;">
            <strong>💭 Reflection:</strong> Think about your own medical experience. Can you identify a scenario 
            where it would be useful to visualize relationships as a network? For example: comorbidity, 
            drug interactions, or contact tracing?
        </div>
        """))
    
    # =========================================================================
    # SECTION 2: Graph Builder
    # =========================================================================
    
    def _section_2_graph_builder(self):
        display(HTML("""
        <h3>🔨 Practical Exercise: Build a Patient Similarity Network</h3>
        <p>Now you will build a network yourself! Imagine you have data about patients, and you want to 
        visualize which patients are similar to each other based on symptoms or diagnoses.</p>
        
        <div style="background: #fffde7; padding: 10px; border-radius: 5px; margin: 10px 0;">
            <strong>📌 Task:</strong> Add at least 2 new patients and create at least 3 connections.
        </div>
        """))
        
        self._show_graph_builder()
        
        display(HTML("""
        <div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin-top: 20px;">
            <h4 style="margin-top: 0;">💡 Think about:</h4>
            <ul>
                <li>Which patients have the most connections? These could be "typical" for a disease group.</li>
                <li>Are there any isolated patients? These could be special cases that need individual follow-up.</li>
                <li>Are there clusters of patients forming? This could indicate subgroups of a disease.</li>
            </ul>
        </div>
        """))
    
    # =========================================================================
    # SECTION 3: Centrality Measures
    # =========================================================================
    
    def _section_3_centrality(self):
        display(HTML("""
        <h3>📊 Who is Most Important? Centrality Measures Explained</h3>
        <p>In a network, not all nodes are equally important. <strong>Centrality measures</strong> help us 
        identify the most significant nodes – for example, patients who are "typical" for a group, 
        or diseases that connect many other diseases together.</p>
        
        <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: #bbdefb;">
                    <th style="padding: 10px; text-align: left;">Measure</th>
                    <th style="padding: 10px; text-align: left;">What it Measures</th>
                    <th style="padding: 10px; text-align: left;">Medical Interpretation</th>
                </tr>
                <tr>
                    <td style="padding: 10px;"><strong>Degree Centrality</strong></td>
                    <td style="padding: 10px;">Number of direct connections</td>
                    <td style="padding: 10px;">Patient who resembles many others</td>
                </tr>
                <tr style="background: #e3f2fd;">
                    <td style="padding: 10px;"><strong>Betweenness Centrality</strong></td>
                    <td style="padding: 10px;">Lies on paths between others</td>
                    <td style="padding: 10px;">Disease that connects different disease groups</td>
                </tr>
                <tr>
                    <td style="padding: 10px;"><strong>Closeness Centrality</strong></td>
                    <td style="padding: 10px;">Short distance to all others</td>
                    <td style="padding: 10px;">Patient relevant to many treatment pathways</td>
                </tr>
                <tr style="background: #e3f2fd;">
                    <td style="padding: 10px;"><strong>Eigenvector Centrality</strong></td>
                    <td style="padding: 10px;">Connected to important nodes</td>
                    <td style="padding: 10px;">Patient in a "core area" of the network</td>
                </tr>
            </table>
        </div>
        """))
        
        self._show_centrality_calculator()
        
        # Quiz
        self._create_quiz(
            "A patient has low degree centrality but high betweenness centrality. What does this mean?",
            [
                "The patient has many connections to other patients",
                "The patient is isolated in the network",
                "The patient acts as a 'bridge' between two patient groups",
                "The patient is not important in the network"
            ],
            2,
            "Correct! High betweenness centrality means the patient lies on many shortest paths between other nodes – an important 'bridge' even with few direct connections."
        )
    
    # =========================================================================
    # SECTION 4: Network Experiment
    # =========================================================================
    
    def _section_4_experiment(self):
        display(HTML("""
        <h3>🧪 Experiment: How Network Structure Affects Analysis</h3>
        <p>Different types of networks have different properties. Use the sliders below to see how 
        the network structure changes when you adjust the parameters.</p>
        
        <div style="background: #f3e5f5; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <h4 style="margin-top: 0;">Three Important Network Types:</h4>
            <ul>
                <li><strong>Random networks:</strong> Connections occur randomly – degrees are evenly distributed.</li>
                <li><strong>Scale-free:</strong> A few "hubs" have very many connections – a realistic model for many biological networks.</li>
                <li><strong>Small-world:</strong> High local clustering but short global distances – typical for social networks.</li>
            </ul>
        </div>
        """))
        
        self._show_network_experiment()
        
        display(HTML("""
        <div style="background: #fff3e0; padding: 15px; border-radius: 8px; margin-top: 20px;">
            <strong>🔍 Observe:</strong>
            <ul>
                <li>How does the degree distribution change when you switch network types?</li>
                <li>What happens to the clustering coefficient when you increase the connection probability?</li>
                <li>Can you make the network split into multiple components?</li>
            </ul>
        </div>
        """))
    
    # =========================================================================
    # SECTION 5: Medical Applications
    # =========================================================================
    
    def _section_5_medicine(self):
        display(HTML("""
        <h3>🏥 Graph Theory in Clinical Practice</h3>
        <p>Here are some concrete examples of how graph theory is used in medicine today:</p>
        """))
        
        # Examples with illustrations
        examples = [
            ("Disease Subtyping", "Patients with the same diagnosis may have different disease subtypes. Network analysis of patient similarity can reveal these groups.", "#e8f5e9"),
            ("Drug Interactions", "Networks of drugs and side effects help identify dangerous combinations.", "#fff3e0"),
            ("Contact Tracing", "During pandemics, contact networks are used to trace infections and identify super-spreaders.", "#e3f2fd"),
            ("Protein Interactions", "Network analysis of proteins helps identify new drug targets.", "#fce4ec")
        ]
        
        for title, description, color in examples:
            display(HTML(f"""
            <div style="background: {color}; padding: 15px; border-radius: 8px; margin: 10px 0;">
                <h4 style="margin-top: 0;">🔹 {title}</h4>
                <p>{description}</p>
            </div>
            """))
        
        # Case study
        display(HTML("""
        <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #2196F3;">
            <h4 style="margin-top: 0;">📋 Case Study: Cancer Subtyping</h4>
            <p>Researchers used patient similarity networks based on gene expression data from breast cancer patients. 
            By analyzing clusters in the network, they identified four distinct subgroups with different prognoses 
            and treatment responses. This has led to more personalized treatment.</p>
        </div>
        """))
        
        # Quiz
        self._create_quiz(
            "Why are scale-free networks relevant for understanding epidemics?",
            [
                "Because all people have the same number of contacts",
                "Because a few 'super-spreaders' (hubs) have very many contacts",
                "Because diseases spread randomly",
                "Because scale-free networks are easy to analyze"
            ],
            1,
            "Correct! In scale-free networks, a few nodes (super-spreaders) have extremely many connections. Vaccinating or isolating these hubs can stop an epidemic effectively."
        )
    
    # =========================================================================
    # SECTION 6: Final Quiz
    # =========================================================================
    
    def _section_6_quiz(self):
        display(HTML("""
        <h3>🏆 Test Your Knowledge!</h3>
        <p>Answer the questions below to test what you have learned.</p>
        """))
        
        self._create_quiz(
            "1. What is the main purpose of a patient similarity network?",
            [
                "To count the number of patients in a hospital",
                "To identify groups of patients with similar characteristics",
                "To calculate treatment costs",
                "To plan surgeries"
            ],
            1,
            "Patient similarity networks group patients based on similarities in symptoms, diagnoses, or treatment response – useful for personalized medicine."
        )
        
        self._create_quiz(
            "2. If a node has high betweenness centrality, what does it mean?",
            [
                "The node has no connections",
                "The node is centrally located and connects different parts of the network",
                "The node is the oldest in the network",
                "The node has the lowest degree"
            ],
            1,
            "High betweenness centrality means that many shortest paths go through this node – it acts as an important 'bridge' in the network."
        )
        
        self._create_quiz(
            "3. What characterizes a scale-free network?",
            [
                "All nodes have the same number of connections",
                "A few 'hubs' have very many connections, while most have few",
                "The network has no edges",
                "The network is always tree-shaped"
            ],
            1,
            "Scale-free networks follow a power-law distribution where a few hubs dominate. Protein interaction networks and social networks are typical examples."
        )
        
        self._create_quiz(
            "4. In an adjacency matrix for a directed graph, what do row i and column j represent?",
            [
                "There is an edge from j to i",
                "There is an edge from i to j",
                "i and j are neighbors regardless of direction",
                "i and j have the same degree"
            ],
            1,
            "In an adjacency matrix, the row represents the from-node and the column represents the to-node. matrix[i,j] = 1 means there is an edge from i to j."
        )
        
        # Summary
        display(HTML(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; 
                    padding: 20px; border-radius: 10px; margin-top: 20px; text-align: center;">
            <h2 style="margin-top: 0;">🎉 Congratulations!</h2>
            <p style="font-size: 1.2em;">You have completed the learning module on graph theory in medicine.</p>
            <p>Total quiz points: <strong>{self.quiz_points}</strong></p>
            <p style="font-size: 0.9em; margin-top: 15px;">
                Continue exploring network science in the next sections of the notebook!
            </p>
        </div>
        """))


# Alias for backward compatibility with the Norwegian class name
InteraktivLaeringsmodul = InteractiveLearningModule

# ============================================================================



