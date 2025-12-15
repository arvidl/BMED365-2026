# ============================================================================
# 🎓 INTERAKTIV LÆRINGSMODUL: GRAFTEORI I MEDISIN
# ============================================================================
# Denne modulen inneholder:
# - Interaktive lysbilder med quiz
# - Grafbygger der du kan lage egne nettverk
# - Sentralitetskalkulator med visualisering
# - Parametersliders for nettverkseksperimentering
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
# HOVEDKLASSE: Interaktiv læringsmodul
# ============================================================================

class InteraktivLaeringsmodul:
    """En interaktiv læringsmodul om grafteori i medisin."""
    
    def __init__(self):
        self.gjeldende_seksjon = 0
        self.quiz_poeng = 0
        self.totale_quiz = 0
        self.fullforte_seksjoner = set()
        
        # Grafen som brukes i grafbyggeren
        self.bruker_graf = nx.Graph()
        self.bruker_graf.add_nodes_from(['Pasient A', 'Pasient B', 'Pasient C'])
        
        # Lag seksjoner
        self.seksjoner = self._opprett_seksjoner()
        
        # CSS for bedre formatering
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
        
        self._vis_hovedmeny()
    
    # =========================================================================
    # HOVEDMENY OG NAVIGASJON
    # =========================================================================
    
    def _vis_hovedmeny(self):
        """Vis hovedmenyen med seksjonsvalg."""
        clear_output(wait=True)
        
        # Overskrift
        display(HTML("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; border-radius: 10px; margin-bottom: 20px;">
            <h1 style="margin: 0;">🎓 Grafteori i medisin</h1>
            <p style="margin: 10px 0 0 0; font-size: 1.1em;">Interaktiv læringsmodul</p>
        </div>
        """))
        
        # Fremgangsmåler
        fullfort = len(self.fullforte_seksjoner)
        totalt = len(self.seksjoner)
        prosent = int(100 * fullfort / totalt) if totalt > 0 else 0
        
        display(HTML(f"""
        <div style="margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 8px;">
            <strong>📊 Din fremgang:</strong> {fullfort}/{totalt} seksjoner fullført ({prosent}%)
            <div style="background: #e0e0e0; height: 10px; border-radius: 5px; margin-top: 10px;">
                <div style="background: linear-gradient(90deg, #4CAF50, #8BC34A); height: 100%; 
                           width: {prosent}%; border-radius: 5px; transition: width 0.5s;"></div>
            </div>
            <p style="margin-top: 10px;">🏆 <strong>Quiz-poeng:</strong> {self.quiz_poeng} riktige svar</p>
        </div>
        """))
        
        # Seksjonsknapper
        display(HTML("<h3>📚 Velg en seksjon:</h3>"))
        
        for i, seksjon in enumerate(self.seksjoner):
            fullfort_markering = "✅ " if i in self.fullforte_seksjoner else ""
            knapp = widgets.Button(
                description=f"{fullfort_markering}{seksjon['tittel']}",
                layout=widgets.Layout(width='100%', height='50px'),
                style={'button_color': '#e8f5e9' if i in self.fullforte_seksjoner else '#e3f2fd'}
            )
            knapp.on_click(lambda _, idx=i: self._vis_seksjon(idx))
            display(knapp)
    
    def _vis_seksjon(self, idx):
        """Vis en spesifikk seksjon."""
        self.gjeldende_seksjon = idx
        seksjon = self.seksjoner[idx]
        
        clear_output(wait=True)
        
        # Navigasjonsknapper
        nav_knapper = widgets.HBox([
            widgets.Button(description='🏠 Hovedmeny', layout=widgets.Layout(width='120px')),
            widgets.Button(description='← Forrige', layout=widgets.Layout(width='100px')),
            widgets.HTML(value=f'<h4 style="margin: 0 20px;">Seksjon {idx + 1}/{len(self.seksjoner)}</h4>'),
            widgets.Button(description='Neste →', layout=widgets.Layout(width='100px'))
        ], layout=widgets.Layout(justify_content='center', margin='10px 0'))
        
        nav_knapper.children[0].on_click(lambda _: self._vis_hovedmeny())
        nav_knapper.children[1].on_click(lambda _: self._vis_seksjon(max(0, idx - 1)))
        nav_knapper.children[3].on_click(lambda _: self._vis_seksjon(min(len(self.seksjoner) - 1, idx + 1)))
        
        display(nav_knapper)
        
        # Seksjonstittel
        display(HTML(f"""
        <div style="text-align: center; padding: 15px; background: #f0f4f8; border-radius: 8px; margin: 10px 0;">
            <h2 style="margin: 0; color: #2c3e50;">{seksjon['tittel']}</h2>
        </div>
        """))
        
        # Vis seksjonsinnhold
        seksjon['innhold']()
        
        # Marker som fullført
        self.fullforte_seksjoner.add(idx)
    
    # =========================================================================
    # QUIZ-SYSTEM
    # =========================================================================
    
    def _lag_quiz(self, sporsmal, alternativer, riktig_indeks, forklaring):
        """Lag et interaktivt quiz-spørsmål."""
        quiz_output = widgets.Output()
        
        display(HTML(f"""
        <div style="background: #fff3e0; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800; margin: 15px 0;">
            <strong>❓ Quiz:</strong> {sporsmal}
        </div>
        """))
        
        knapper = []
        for i, alt in enumerate(alternativer):
            knapp = widgets.Button(
                description=alt,
                layout=widgets.Layout(width='100%', height='40px', margin='5px 0'),
                style={'button_color': '#e3f2fd'}
            )
            
            def sjekk_svar(_, idx=i):
                with quiz_output:
                    clear_output()
                    if idx == riktig_indeks:
                        self.quiz_poeng += 1
                        display(HTML(f"""
                        <div style="background: #d4edda; padding: 15px; border-radius: 8px; 
                                    border-left: 4px solid #28a745; margin: 10px 0;">
                            <strong>✅ Riktig!</strong><br>{forklaring}
                        </div>
                        """))
                    else:
                        display(HTML(f"""
                        <div style="background: #f8d7da; padding: 15px; border-radius: 8px; 
                                    border-left: 4px solid #dc3545; margin: 10px 0;">
                            <strong>❌ Ikke helt.</strong> Riktig svar: <em>{alternativer[riktig_indeks]}</em><br>{forklaring}
                        </div>
                        """))
                    self.totale_quiz += 1
            
            knapp.on_click(sjekk_svar)
            knapper.append(knapp)
            display(knapp)
        
        display(quiz_output)
    
    # =========================================================================
    # INTERAKTIV GRAFBYGGER
    # =========================================================================
    
    def _vis_grafbygger(self):
        """Vis en interaktiv grafbygger."""
        display(HTML("""
        <div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <h3 style="margin-top: 0;">🔨 Bygg ditt eget pasient-likhetsnettverk</h3>
            <p>Bruk verktøyene nedenfor for å legge til pasienter og forbindelser mellom dem.</p>
        </div>
        """))
        
        graf_output = widgets.Output()
        
        # Legg til node
        ny_node_input = widgets.Text(placeholder='Pasientnavn (f.eks. "Pasient D")', layout=widgets.Layout(width='200px'))
        legg_til_node_knapp = widgets.Button(description='➕ Legg til pasient', style={'button_color': '#4CAF50'})
        
        # Legg til kant
        node1_dropdown = widgets.Dropdown(options=list(self.bruker_graf.nodes()), description='Fra:')
        node2_dropdown = widgets.Dropdown(options=list(self.bruker_graf.nodes()), description='Til:')
        legg_til_kant_knapp = widgets.Button(description='🔗 Koble pasienter', style={'button_color': '#2196F3'})
        
        # Slett kant
        slett_kant_knapp = widgets.Button(description='✂️ Fjern forbindelse', style={'button_color': '#f44336'})
        
        # Tilbakestill
        tilbakestill_knapp = widgets.Button(description='🔄 Tilbakestill', style={'button_color': '#9e9e9e'})
        
        def oppdater_dropdowns():
            noder = list(self.bruker_graf.nodes())
            node1_dropdown.options = noder
            node2_dropdown.options = noder
        
        def tegn_graf():
            with graf_output:
                clear_output(wait=True)
                fig, ax = plt.subplots(figsize=(8, 6))
                
                if len(self.bruker_graf.nodes()) > 0:
                    pos = nx.spring_layout(self.bruker_graf, seed=42)
                    nx.draw(self.bruker_graf, pos, ax=ax, with_labels=True,
                           node_color='lightblue', node_size=2000, font_size=10,
                           font_weight='bold', edge_color='gray', width=2)
                    
                    # Vis statistikk
                    ax.set_title(f'Noder: {self.bruker_graf.number_of_nodes()} | '
                                f'Kanter: {self.bruker_graf.number_of_edges()}', fontsize=12)
                else:
                    ax.text(0.5, 0.5, 'Ingen noder ennå.\nLegg til pasienter!', 
                           ha='center', va='center', fontsize=14)
                    ax.axis('off')
                
                plt.tight_layout()
                plt.show()
        
        def legg_til_node(_):
            navn = ny_node_input.value.strip()
            if navn and navn not in self.bruker_graf.nodes():
                self.bruker_graf.add_node(navn)
                ny_node_input.value = ''
                oppdater_dropdowns()
                tegn_graf()
        
        def legg_til_kant(_):
            if node1_dropdown.value and node2_dropdown.value:
                if node1_dropdown.value != node2_dropdown.value:
                    self.bruker_graf.add_edge(node1_dropdown.value, node2_dropdown.value)
                    tegn_graf()
        
        def slett_kant(_):
            if node1_dropdown.value and node2_dropdown.value:
                if self.bruker_graf.has_edge(node1_dropdown.value, node2_dropdown.value):
                    self.bruker_graf.remove_edge(node1_dropdown.value, node2_dropdown.value)
                    tegn_graf()
        
        def tilbakestill(_):
            self.bruker_graf.clear()
            self.bruker_graf.add_nodes_from(['Pasient A', 'Pasient B', 'Pasient C'])
            oppdater_dropdowns()
            tegn_graf()
        
        legg_til_node_knapp.on_click(legg_til_node)
        legg_til_kant_knapp.on_click(legg_til_kant)
        slett_kant_knapp.on_click(slett_kant)
        tilbakestill_knapp.on_click(tilbakestill)
        
        # Layout
        display(widgets.HBox([ny_node_input, legg_til_node_knapp]))
        display(widgets.HBox([node1_dropdown, node2_dropdown, legg_til_kant_knapp, slett_kant_knapp]))
        display(tilbakestill_knapp)
        display(graf_output)
        
        tegn_graf()
    
    # =========================================================================
    # SENTRALITETSKALKULATOR
    # =========================================================================
    
    def _vis_sentralitetskalkulator(self):
        """Vis en interaktiv sentralitetskalkulator."""
        display(HTML("""
        <div style="background: #fff3e0; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <h3 style="margin-top: 0;">📊 Sentralitetskalkulator</h3>
            <p>Se hvordan ulike sentralitetsmål identifiserer "viktige" noder i et nettverk.</p>
        </div>
        """))
        
        # Lag eksempelnettverk
        G = nx.karate_club_graph()
        
        sentralitet_dropdown = widgets.Dropdown(
            options=[
                ('Gradsentralitet (antall forbindelser)', 'degree'),
                ('Mellomleddsentralitet (bronoder)', 'betweenness'),
                ('Nærhetssentralitet (avstand til andre)', 'closeness'),
                ('Egenvektorsentralitet (viktige naboer)', 'eigenvector')
            ],
            value='degree',
            description='Velg mål:'
        )
        
        output = widgets.Output()
        
        def oppdater_visualisering(change):
            with output:
                clear_output(wait=True)
                
                # Beregn sentralitet
                if change['new'] == 'degree':
                    sentralitet = nx.degree_centrality(G)
                    tittel = "Gradsentralitet"
                    forklaring = "Noder med mange forbindelser er store/mørke."
                elif change['new'] == 'betweenness':
                    sentralitet = nx.betweenness_centrality(G)
                    tittel = "Mellomleddsentralitet"
                    forklaring = "Noder som ligger på mange korteste stier er viktige 'broer'."
                elif change['new'] == 'closeness':
                    sentralitet = nx.closeness_centrality(G)
                    tittel = "Nærhetssentralitet"
                    forklaring = "Noder med kort avstand til alle andre kan spre informasjon raskt."
                else:
                    sentralitet = nx.eigenvector_centrality(G, max_iter=1000)
                    tittel = "Egenvektorsentralitet"
                    forklaring = "Noder koblet til andre viktige noder er selv viktige."
                
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
                
                # Graf-visualisering
                pos = nx.spring_layout(G, seed=42)
                verdier = list(sentralitet.values())
                
                nx.draw(G, pos, ax=ax1, with_labels=True,
                       node_color=verdier, cmap=plt.cm.YlOrRd,
                       node_size=[v * 3000 + 300 for v in verdier],
                       font_size=8, edge_color='lightgray')
                ax1.set_title(f'{tittel}\n{forklaring}', fontsize=11)
                
                # Bar chart
                sortert = sorted(sentralitet.items(), key=lambda x: x[1], reverse=True)[:10]
                noder, verdier = zip(*sortert)
                farger = plt.cm.YlOrRd([v/max(verdier) for v in verdier])
                ax2.barh(range(len(noder)), verdier, color=farger)
                ax2.set_yticks(range(len(noder)))
                ax2.set_yticklabels([f'Node {n}' for n in noder])
                ax2.set_xlabel('Sentralitetsverdi')
                ax2.set_title('Topp 10 mest sentrale noder')
                ax2.invert_yaxis()
                
                plt.tight_layout()
                plt.show()
                
                # Forklaring
                display(HTML(f"""
                <div style="background: #e3f2fd; padding: 10px; border-radius: 5px; margin-top: 10px;">
                    <strong>💡 Tolkning:</strong> Node {sortert[0][0]} har høyest {tittel.lower()} 
                    ({sortert[0][1]:.3f}), mens node {sortert[-1][0]} har lavest blant topp 10 ({sortert[-1][1]:.3f}).
                </div>
                """))
        
        sentralitet_dropdown.observe(oppdater_visualisering, names='value')
        display(sentralitet_dropdown)
        display(output)
        
        # Trigger initial visualisering
        oppdater_visualisering({'new': 'degree'})
    
    # =========================================================================
    # NETTVERKSPARAMETRE-EKSPERIMENT
    # =========================================================================
    
    def _vis_nettverks_eksperiment(self):
        """La brukeren eksperimentere med nettverksparametere."""
        display(HTML("""
        <div style="background: #f3e5f5; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <h3 style="margin-top: 0;">🧪 Eksperimenter med nettverk</h3>
            <p>Juster sliderne for å se hvordan ulike parametere påvirker nettverksstrukturen.</p>
        </div>
        """))
        
        # Sliders
        antall_noder = widgets.IntSlider(value=20, min=5, max=50, description='Antall pasienter:',
                                          style={'description_width': '120px'})
        forbindelser = widgets.FloatSlider(value=0.2, min=0.05, max=0.5, step=0.05, 
                                           description='Tilkoblingsgrad:',
                                           style={'description_width': '120px'})
        nettverkstype = widgets.Dropdown(
            options=[
                ('Tilfeldig nettverk', 'random'),
                ('Scale-free (huber)', 'scalefree'),
                ('Small-world', 'smallworld')
            ],
            value='random',
            description='Nettverkstype:',
            style={'description_width': '120px'}
        )
        
        output = widgets.Output()
        
        def oppdater(change=None):
            with output:
                clear_output(wait=True)
                
                n = antall_noder.value
                p = forbindelser.value
                
                # Generer nettverk
                if nettverkstype.value == 'random':
                    G = nx.erdos_renyi_graph(n, p)
                    beskrivelse = f"Tilfeldig nettverk: {n} noder, {p:.0%} tilkoblingssannsynlighet"
                elif nettverkstype.value == 'scalefree':
                    G = nx.barabasi_albert_graph(n, max(1, int(n * p / 2)))
                    beskrivelse = f"Scale-free: {n} noder med preferensiel tilkobling"
                else:
                    G = nx.watts_strogatz_graph(n, max(2, int(n * p)), 0.3)
                    beskrivelse = f"Small-world: {n} noder med lokal klynging"
                
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
                
                # Nettverksvisualisering
                pos = nx.spring_layout(G, seed=42)
                grader = dict(G.degree())
                nodestorrelser = [grader[n] * 50 + 100 for n in G.nodes()]
                nodefarger = [grader[n] for n in G.nodes()]
                
                nx.draw(G, pos, ax=ax1, with_labels=False,
                       node_color=nodefarger, cmap=plt.cm.YlOrRd,
                       node_size=nodestorrelser, edge_color='lightgray', alpha=0.8)
                ax1.set_title(beskrivelse)
                
                # Gradfordeling
                grader_liste = [d for n, d in G.degree()]
                ax2.hist(grader_liste, bins=range(max(grader_liste) + 2), 
                        edgecolor='white', color='steelblue', alpha=0.7)
                ax2.set_xlabel('Antall forbindelser (grad)')
                ax2.set_ylabel('Antall pasienter')
                ax2.set_title('Gradfordeling: Hvor mange forbindelser har hver pasient?')
                
                plt.tight_layout()
                plt.show()
                
                # Nettverksstatistikk
                display(HTML(f"""
                <div style="display: flex; gap: 20px; margin-top: 15px;">
                    <div style="flex: 1; background: #e8f5e9; padding: 10px; border-radius: 5px; text-align: center;">
                        <strong>Antall kanter</strong><br><span style="font-size: 1.5em;">{G.number_of_edges()}</span>
                    </div>
                    <div style="flex: 1; background: #e3f2fd; padding: 10px; border-radius: 5px; text-align: center;">
                        <strong>Gjennomsnittlig grad</strong><br><span style="font-size: 1.5em;">{np.mean(grader_liste):.1f}</span>
                    </div>
                    <div style="flex: 1; background: #fff3e0; padding: 10px; border-radius: 5px; text-align: center;">
                        <strong>Klyngekoeffisient</strong><br><span style="font-size: 1.5em;">{nx.average_clustering(G):.3f}</span>
                    </div>
                    <div style="flex: 1; background: #fce4ec; padding: 10px; border-radius: 5px; text-align: center;">
                        <strong>Komponenter</strong><br><span style="font-size: 1.5em;">{nx.number_connected_components(G)}</span>
                    </div>
                </div>
                """))
        
        antall_noder.observe(oppdater, names='value')
        forbindelser.observe(oppdater, names='value')
        nettverkstype.observe(oppdater, names='value')
        
        display(widgets.VBox([nettverkstype, antall_noder, forbindelser]))
        display(output)
        
        oppdater()
    
    # =========================================================================
    # SEKSJONSDEFINISJONER
    # =========================================================================
    
    def _opprett_seksjoner(self):
        """Opprett alle seksjoner i læringsmodulen."""
        return [
            {
                "tittel": "1️⃣ Hva er en graf?",
                "innhold": self._seksjon_1_grunnleggende
            },
            {
                "tittel": "2️⃣ Bygg din egen graf",
                "innhold": self._seksjon_2_grafbygger
            },
            {
                "tittel": "3️⃣ Sentralitetsmål",
                "innhold": self._seksjon_3_sentralitet
            },
            {
                "tittel": "4️⃣ Eksperimenter med nettverk",
                "innhold": self._seksjon_4_eksperiment
            },
            {
                "tittel": "5️⃣ Medisinske anvendelser",
                "innhold": self._seksjon_5_medisin
            },
            {
                "tittel": "6️⃣ Avsluttende quiz",
                "innhold": self._seksjon_6_quiz
            }
        ]
    
    # =========================================================================
    # SEKSJON 1: Grunnleggende om grafer
    # =========================================================================
    
    def _seksjon_1_grunnleggende(self):
        display(HTML("""
        <div style="line-height: 1.8;">
            <h3>🔷 Byggesteinene i grafteori</h3>
            <p>En <strong>graf</strong> er en matematisk struktur som beskriver <em>relasjoner</em> mellom objekter.</p>
            
            <div style="display: flex; gap: 20px; margin: 20px 0;">
                <div style="flex: 1; background: #e3f2fd; padding: 15px; border-radius: 8px;">
                    <h4 style="margin-top: 0;">🔵 Noder (vertices)</h4>
                    <p>Objektene vi studerer:</p>
                    <ul>
                        <li>Pasienter</li>
                        <li>Sykdommer</li>
                        <li>Symptomer</li>
                        <li>Proteiner</li>
                    </ul>
                </div>
                <div style="flex: 1; background: #fff3e0; padding: 15px; border-radius: 8px;">
                    <h4 style="margin-top: 0;">➖ Kanter (edges)</h4>
                    <p>Forbindelser mellom noder:</p>
                    <ul>
                        <li>Pasient-likhet</li>
                        <li>Sykdom-symptom</li>
                        <li>Protein-interaksjon</li>
                        <li>Legemiddel-bivirkning</li>
                    </ul>
                </div>
            </div>
        </div>
        """))
        
        # Eksempelgraf
        fig, ax = plt.subplots(figsize=(8, 5))
        G = nx.Graph()
        G.add_edges_from([('Pasient', 'Diabetes'), ('Pasient', 'Hypertensjon'), 
                          ('Diabetes', 'Hypertensjon'), ('Diabetes', 'Fedme')])
        pos = {'Pasient': (0, 0), 'Diabetes': (1, 1), 'Hypertensjon': (1, -1), 'Fedme': (2, 1)}
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue',
               node_size=3000, font_size=11, font_weight='bold', edge_color='gray', width=2)
        ax.set_title('Eksempel: Pasient-sykdom-nettverk', fontsize=12)
        plt.tight_layout()
        plt.show()
        
        # Quiz
        self._lag_quiz(
            "Hva representerer en **kant** i et pasient-likhetsnettverk?",
            ["En pasient", "En sykdom", "En forbindelse/likhet mellom to pasienter", "Et symptom"],
            2,
            "Riktig! Kanter representerer relasjoner – i et pasient-likhetsnettverk betyr en kant at to pasienter har lignende egenskaper."
        )
        
        # Refleksjonsspørsmål
        display(HTML("""
        <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin-top: 20px; border-left: 4px solid #9c27b0;">
            <strong>💭 Refleksjon:</strong> Tenk på din egen medisinske erfaring. Kan du identifisere et scenario 
            der det ville vært nyttig å visualisere relasjoner som et nettverk? For eksempel: komorbiditet, 
            legemiddelinteraksjoner, eller smittesporing?
        </div>
        """))
    
    # =========================================================================
    # SEKSJON 2: Grafbygger
    # =========================================================================
    
    def _seksjon_2_grafbygger(self):
        display(HTML("""
        <h3>🔨 Praktisk øvelse: Bygg et pasient-likhetsnettverk</h3>
        <p>Nå skal du selv bygge et nettverk! Forestill deg at du har data om pasienter, og at du vil 
        visualisere hvilke pasienter som ligner på hverandre basert på symptomer eller diagnoser.</p>
        
        <div style="background: #fffde7; padding: 10px; border-radius: 5px; margin: 10px 0;">
            <strong>📌 Oppgave:</strong> Legg til minst 2 nye pasienter og opprett minst 3 forbindelser.
        </div>
        """))
        
        self._vis_grafbygger()
        
        display(HTML("""
        <div style="background: #e8f5e9; padding: 15px; border-radius: 8px; margin-top: 20px;">
            <h4 style="margin-top: 0;">💡 Tenk over:</h4>
            <ul>
                <li>Hvilke pasienter har flest forbindelser? Disse kan være "typiske" for en sykdomsgruppe.</li>
                <li>Er det noen isolerte pasienter? Disse kan være spesielle tilfeller som trenger individuell oppfølging.</li>
                <li>Danner det seg klynger av pasienter? Dette kan indikere undergrupper av en sykdom.</li>
            </ul>
        </div>
        """))
    
    # =========================================================================
    # SEKSJON 3: Sentralitetsmål
    # =========================================================================
    
    def _seksjon_3_sentralitet(self):
        display(HTML("""
        <h3>📊 Hvem er viktigst? Sentralitetsmål forklart</h3>
        <p>I et nettverk er ikke alle noder like viktige. <strong>Sentralitetsmål</strong> hjelper oss å 
        identifisere de mest betydningsfulle nodene – for eksempel pasienter som er "typiske" for en gruppe, 
        eller sykdommer som kobler mange andre sykdommer sammen.</p>
        
        <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: #bbdefb;">
                    <th style="padding: 10px; text-align: left;">Mål</th>
                    <th style="padding: 10px; text-align: left;">Hva det måler</th>
                    <th style="padding: 10px; text-align: left;">Medisinsk tolkning</th>
                </tr>
                <tr>
                    <td style="padding: 10px;"><strong>Gradsentralitet</strong></td>
                    <td style="padding: 10px;">Antall direkte forbindelser</td>
                    <td style="padding: 10px;">Pasient som ligner på mange andre</td>
                </tr>
                <tr style="background: #e3f2fd;">
                    <td style="padding: 10px;"><strong>Mellomleddsentralitet</strong></td>
                    <td style="padding: 10px;">Ligger på veien mellom andre</td>
                    <td style="padding: 10px;">Sykdom som kobler ulike sykdomsgrupper</td>
                </tr>
                <tr>
                    <td style="padding: 10px;"><strong>Nærhetssentralitet</strong></td>
                    <td style="padding: 10px;">Kort avstand til alle andre</td>
                    <td style="padding: 10px;">Pasient som er relevant for mange behandlingsveier</td>
                </tr>
                <tr style="background: #e3f2fd;">
                    <td style="padding: 10px;"><strong>Egenvektorsentralitet</strong></td>
                    <td style="padding: 10px;">Koblet til viktige noder</td>
                    <td style="padding: 10px;">Pasient i et "kjerneområde" av nettverket</td>
                </tr>
            </table>
        </div>
        """))
        
        self._vis_sentralitetskalkulator()
        
        # Quiz
        self._lag_quiz(
            "En pasient har lav gradsentralitet men høy mellomleddsentralitet. Hva betyr dette?",
            [
                "Pasienten har mange forbindelser til andre pasienter",
                "Pasienten er isolert i nettverket",
                "Pasienten fungerer som en 'bro' mellom to pasientgrupper",
                "Pasienten er ikke viktig i nettverket"
            ],
            2,
            "Riktig! Høy mellomleddsentralitet betyr at pasienten ligger på mange korteste stier mellom andre noder – en viktig 'bro' selv med få direkte forbindelser."
        )
    
    # =========================================================================
    # SEKSJON 4: Nettverkseksperiment
    # =========================================================================
    
    def _seksjon_4_eksperiment(self):
        display(HTML("""
        <h3>🧪 Eksperimenter: Hvordan nettverksstruktur påvirker analyse</h3>
        <p>Ulike typer nettverk har ulike egenskaper. Bruk sliderne nedenfor for å se hvordan 
        nettverksstrukturen endres når du justerer parameterne.</p>
        
        <div style="background: #f3e5f5; padding: 15px; border-radius: 8px; margin: 15px 0;">
            <h4 style="margin-top: 0;">Tre viktige nettverkstyper:</h4>
            <ul>
                <li><strong>Tilfeldige nettverk:</strong> Forbindelser oppstår tilfeldig – gradene er jevnt fordelt.</li>
                <li><strong>Scale-free:</strong> Noen få "huber" har veldig mange forbindelser – en realistisk modell for mange biologiske nettverk.</li>
                <li><strong>Small-world:</strong> Høy lokal klynging men korte globale avstander – typisk for sosiale nettverk.</li>
            </ul>
        </div>
        """))
        
        self._vis_nettverks_eksperiment()
        
        display(HTML("""
        <div style="background: #fff3e0; padding: 15px; border-radius: 8px; margin-top: 20px;">
            <strong>🔍 Observer:</strong>
            <ul>
                <li>Hvordan endres gradfordelingen når du bytter nettverkstype?</li>
                <li>Hva skjer med klyngekoeffisienten når du øker tilkoblingsgraden?</li>
                <li>Kan du få nettverket til å splittes i flere komponenter?</li>
            </ul>
        </div>
        """))
    
    # =========================================================================
    # SEKSJON 5: Medisinske anvendelser
    # =========================================================================
    
    def _seksjon_5_medisin(self):
        display(HTML("""
        <h3>🏥 Grafteori i klinisk praksis</h3>
        <p>Her er noen konkrete eksempler på hvordan grafteori brukes i medisin i dag:</p>
        """))
        
        # Eksempler med illustrasjoner
        eksempler = [
            ("Sykdomsundertyping", "Pasienter med samme diagnose kan ha ulike sykdomsundertyper. Nettverksanalyse av pasientlikhet kan avdekke disse gruppene.", "#e8f5e9"),
            ("Legemiddelinteraksjoner", "Nettverk av legemidler og bivirkninger hjelper med å identifisere farlige kombinasjoner.", "#fff3e0"),
            ("Smittesporing", "Under pandemier brukes kontaktnettverk for å spore smitte og identifisere superspreiere.", "#e3f2fd"),
            ("Protein-interaksjoner", "Nettverksanalyse av proteiner hjelper med å identifisere nye legemiddelmål.", "#fce4ec")
        ]
        
        for tittel, beskrivelse, farge in eksempler:
            display(HTML(f"""
            <div style="background: {farge}; padding: 15px; border-radius: 8px; margin: 10px 0;">
                <h4 style="margin-top: 0;">🔹 {tittel}</h4>
                <p>{beskrivelse}</p>
            </div>
            """))
        
        # Case study
        display(HTML("""
        <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #2196F3;">
            <h4 style="margin-top: 0;">📋 Kasusstudie: Kreftundertyping</h4>
            <p>Forskere brukte pasient-likhetsnettverk basert på genekspresjonsdata fra brystkreftpasienter. 
            Ved å analysere klynger i nettverket identifiserte de fire distinkte undergrupper med ulik prognose 
            og behandlingsrespons. Dette har ført til mer persontilpasset behandling.</p>
        </div>
        """))
        
        # Quiz
        self._lag_quiz(
            "Hvorfor er scale-free nettverk relevante for å forstå epidemier?",
            [
                "Fordi alle personer har like mange kontakter",
                "Fordi noen få 'superspreiere' (huber) har veldig mange kontakter",
                "Fordi sykdommer sprer seg tilfeldig",
                "Fordi scale-free nettverk er enkle å analysere"
            ],
            1,
            "Riktig! I scale-free nettverk har noen få noder (superspreiere) ekstremt mange forbindelser. Vaksinering eller isolering av disse hubene kan stoppe en epidemi effektivt."
        )
    
    # =========================================================================
    # SEKSJON 6: Avsluttende quiz
    # =========================================================================
    
    def _seksjon_6_quiz(self):
        display(HTML("""
        <h3>🏆 Test din kunnskap!</h3>
        <p>Svar på spørsmålene nedenfor for å teste hva du har lært.</p>
        """))
        
        self._lag_quiz(
            "1. Hva er hovedformålet med et pasient-likhetsnettverk?",
            [
                "Å telle antall pasienter på et sykehus",
                "Å identifisere grupper av pasienter med lignende egenskaper",
                "Å beregne kostnader for behandling",
                "Å planlegge operasjoner"
            ],
            1,
            "Pasient-likhetsnettverk grupperer pasienter basert på likheter i symptomer, diagnoser eller behandlingsrespons – nyttig for persontilpasset medisin."
        )
        
        self._lag_quiz(
            "2. Hvis en node har høy mellomleddsentralitet, hva betyr det?",
            [
                "Noden har ingen forbindelser",
                "Noden ligger sentralt og kobler ulike deler av nettverket",
                "Noden er den eldste i nettverket",
                "Noden har lavest grad"
            ],
            1,
            "Høy mellomleddsentralitet betyr at mange korteste stier går gjennom denne noden – den fungerer som en viktig 'bro' i nettverket."
        )
        
        self._lag_quiz(
            "3. Hva kjennetegner et scale-free nettverk?",
            [
                "Alle noder har samme antall forbindelser",
                "Noen få 'huber' har veldig mange forbindelser, mens de fleste har få",
                "Nettverket har ingen kanter",
                "Nettverket er alltid treformet"
            ],
            1,
            "Scale-free nettverk følger en power-law-fordeling der noen få huber dominerer. Protein-interaksjonsnettverk og sosiale nettverk er typiske eksempler."
        )
        
        self._lag_quiz(
            "4. I en nabomatrise for en rettet graf, hva representerer rad i og kolonne j?",
            [
                "Det finnes en kant fra j til i",
                "Det finnes en kant fra i til j",
                "i og j er naboer uansett retning",
                "i og j har samme grad"
            ],
            1,
            "I en nabomatrise representerer raden fra-noden og kolonnen til-noden. matrise[i,j] = 1 betyr at det finnes en kant fra i til j."
        )
        
        # Oppsummering
        display(HTML(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; 
                    padding: 20px; border-radius: 10px; margin-top: 20px; text-align: center;">
            <h2 style="margin-top: 0;">🎉 Gratulerer!</h2>
            <p style="font-size: 1.2em;">Du har fullført læringsmodulen om grafteori i medisin.</p>
            <p>Total quiz-poeng: <strong>{self.quiz_poeng}</strong></p>
            <p style="font-size: 0.9em; margin-top: 15px;">
                Fortsett å utforske nettverksvitenskap i de neste seksjonene av notebooken!
            </p>
        </div>
        """))

# ============================================================================