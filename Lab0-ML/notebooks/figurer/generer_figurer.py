"""
Modul for å generere og lagre figurer brukt i ELMED219 notebooks.

Bruk:
    from figurer.generer_figurer import generer_alle_figurer
    generer_alle_figurer()  # Genererer og lagrer alle figurer

Eller for enkeltfigurer:
    from figurer.generer_figurer import plot_datasett_oppdeling
    fig = plot_datasett_oppdeling(lagre=True)
"""

import matplotlib
matplotlib.use('Agg')  # Bruk ikke-interaktiv backend for servere/scripts
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

# Finn katalogen der dette skriptet ligger
FIGUR_KATALOG = Path(__file__).parent


def plot_trening_test_split(figsize=(10, 3), lagre=False, filnavn="trening_test_split.png"):
    """
    Visualiserer enkel oppdeling av datasett i trenings- og testsett.
    
    Dette er den grunnleggende oppdelingen før vi introduserer valideringssett.
    Figuren viser to bokser: Treningssett (lys grå) og Testsett (mørk grå),
    med "Alle tilgjengelige data" som overskrift.
    
    Parametere:
    -----------
    figsize : tuple
        Størrelse på figuren (bredde, høyde)
    lagre : bool
        Om figuren skal lagres til fil
    filnavn : str
        Filnavn for lagring
        
    Returnerer:
    -----------
    fig, ax : matplotlib figur og akse
    """
    from matplotlib.patches import FancyBboxPatch
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # =========================================================================
    # FARGER OG DIMENSJONER
    # =========================================================================
    # Farger som matcher originalfiguren
    trening_farge = '#E5E5E5'      # Lys grå
    test_farge = '#808080'          # Mørk grå
    kant_farge = '#666666'          # Grå kant
    tekst_farge = '#333333'         # Mørk tekst
    
    # Dimensjoner
    total_bredde = 10
    trening_andel = 0.75            # 75% til trening
    test_andel = 0.25               # 25% til test
    høyde = 1.2
    y_pos = 1
    
    trening_bredde = total_bredde * trening_andel
    test_bredde = total_bredde * test_andel
    
    # =========================================================================
    # TEGN YTRE RAMME (HELE DATASETTET)
    # =========================================================================
    ytre_ramme = FancyBboxPatch(
        (0, y_pos), total_bredde, høyde,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor='none',
        edgecolor=kant_farge,
        linewidth=2
    )
    ax.add_patch(ytre_ramme)
    
    # =========================================================================
    # TEGN TRENINGSSETT (venstre del)
    # =========================================================================
    trening_boks = FancyBboxPatch(
        (0, y_pos), trening_bredde, høyde,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor=trening_farge,
        edgecolor=kant_farge,
        linewidth=1.5
    )
    ax.add_patch(trening_boks)
    
    # Treningssett-etikett
    ax.text(trening_bredde / 2, y_pos + høyde / 2, 'Treningssett',
           ha='center', va='center', fontsize=14, fontweight='normal',
           color=tekst_farge)
    
    # =========================================================================
    # TEGN TESTSETT (høyre del)
    # =========================================================================
    test_boks = FancyBboxPatch(
        (trening_bredde, y_pos), test_bredde, høyde,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor=test_farge,
        edgecolor=kant_farge,
        linewidth=1.5
    )
    ax.add_patch(test_boks)
    
    # Testsett-etikett (hvit tekst på mørk bakgrunn)
    ax.text(trening_bredde + test_bredde / 2, y_pos + høyde / 2, 'Testsett',
           ha='center', va='center', fontsize=14, fontweight='normal',
           color='white')
    
    # =========================================================================
    # TEGN "ALLE TILGJENGELIGE DATA" LINJE OG ETIKETT
    # =========================================================================
    linje_y = y_pos - 0.4
    
    # Horisontal linje
    ax.plot([0, total_bredde], [linje_y, linje_y], 
           color=tekst_farge, linewidth=1.5)
    
    # Vertikale endestykker
    ax.plot([0, 0], [linje_y - 0.1, linje_y + 0.1], 
           color=tekst_farge, linewidth=1.5)
    ax.plot([total_bredde, total_bredde], [linje_y - 0.1, linje_y + 0.1], 
           color=tekst_farge, linewidth=1.5)
    
    # Etikett
    ax.text(total_bredde / 2, linje_y - 0.35, 'Alle tilgjengelige data',
           ha='center', va='top', fontsize=12, fontweight='bold',
           color=tekst_farge)
    
    # =========================================================================
    # JUSTER AKSER OG LAYOUT
    # =========================================================================
    ax.set_xlim(-0.5, total_bredde + 0.5)
    ax.set_ylim(-0.2, y_pos + høyde + 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if lagre:
        filepath = FIGUR_KATALOG / filnavn
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figur lagret: {filepath}")
    
    return fig, ax


def plot_datasett_oppdeling(figsize=(10, 4), lagre=False, filnavn="datasett_oppdeling.png"):
    """
    Visualiserer oppdeling av datasett i trenings-, validerings- og testsett.
    
    Parametere:
    -----------
    figsize : tuple
        Størrelse på figuren (bredde, høyde)
    lagre : bool
        Om figuren skal lagres til fil
    filnavn : str
        Filnavn for lagring
        
    Returnerer:
    -----------
    fig, ax : matplotlib figur og akse
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Proporsjoner: Treningssett (3 deler), Validering (1 del), Test (1 del)
    høyde = 1
    gap = 0.3  # Mellomrom mellom hovedsett og testsett
    
    # Farger (matcher originalfiguren)
    trening_farge = '#FFFFFF'      # Hvit
    kant_farge = '#2C3E50'         # Mørk kant
    val_farge = '#F5B7B1'          # Lys rosa
    test_farge = '#CD6155'         # Mørkere rosa/rød
    
    # Tegn treningssett (3 hvite bokser med interne linjer)
    for i in range(3):
        rect = plt.Rectangle((i, 0), 1, høyde, 
                            facecolor=trening_farge, 
                            edgecolor=kant_farge, 
                            linewidth=2)
        ax.add_patch(rect)
    
    # Tegn valideringssett (1 lys rosa boks)
    rect_val = plt.Rectangle((3, 0), 1, høyde,
                             facecolor=val_farge,
                             edgecolor=kant_farge,
                             linewidth=2)
    ax.add_patch(rect_val)
    
    # Tegn testsett (1 mørk rosa boks, separert med gap)
    rect_test = plt.Rectangle((4 + gap, 0), 1, høyde,
                              facecolor=test_farge,
                              edgecolor=kant_farge,
                              linewidth=2.5)
    ax.add_patch(rect_test)
    
    # Tegn ytre ramme rundt trenings+valideringssett
    outer_rect = plt.Rectangle((0, 0), 4, høyde,
                               facecolor='none',
                               edgecolor=kant_farge,
                               linewidth=3)
    ax.add_patch(outer_rect)
    
    # Øvre klammeparentes for "Datasett D"
    brace_y = høyde + 0.15
    ax.plot([0, 0], [brace_y, brace_y + 0.15], 'k-', lw=1.5)
    ax.plot([0, 5.3], [brace_y + 0.15, brace_y + 0.15], 'k-', lw=1.5)
    ax.plot([5.3, 5.3], [brace_y, brace_y + 0.15], 'k-', lw=1.5)
    ax.text(2.65, brace_y + 0.35, r'Datasett $\mathcal{D}$', 
            ha='center', va='bottom', fontsize=14, fontstyle='italic')
    
    # Nedre klammeparenteser og etiketter
    brace_y_low = -0.15
    
    # Treningssett-klammer
    ax.plot([0.1, 0.1], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([0.1, 2.9], [brace_y_low - 0.1, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([2.9, 2.9], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.text(1.5, brace_y_low - 0.25, 'Treningssett', ha='center', va='top', fontsize=11)
    
    # Valideringssett-klammer
    ax.plot([3.1, 3.1], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([3.1, 3.9], [brace_y_low - 0.1, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([3.9, 3.9], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.text(3.5, brace_y_low - 0.25, 'Validerings-\nsett', ha='center', va='top', fontsize=10)
    
    # Testsett-klammer
    test_start = 4 + gap
    ax.plot([test_start + 0.1, test_start + 0.1], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([test_start + 0.1, test_start + 0.9], [brace_y_low - 0.1, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.plot([test_start + 0.9, test_start + 0.9], [brace_y_low, brace_y_low - 0.1], 'k-', lw=1.5)
    ax.text(test_start + 0.5, brace_y_low - 0.25, 'Testsett', ha='center', va='top', fontsize=11)
    
    # Juster akser
    ax.set_xlim(-0.3, 6)
    ax.set_ylim(-0.75, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if lagre:
        filepath = FIGUR_KATALOG / filnavn
        fig.savefig(filepath, dpi=150, bbox_inches='tight', 
                    facecolor='white', edgecolor='none')
        print(f"✓ Figur lagret: {filepath}")
    
    return fig, ax


def plot_kfold_kryssvalidering(k=5, figsize=(12, 4), lagre=False, 
                                filnavn="kfold_kryssvalidering.png"):
    """
    Visualiserer K-fold kryssvalidering (enkel versjon med bokser).
    Se plot_kfold_kryssvalidering_kuler() for versjon med fargede kuler.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Farger
    trening_farge = '#AED6F1'      # Lys blå
    val_farge = '#E74C3C'          # Rød
    kant_farge = '#2C3E50'         # Mørk kant
    
    boks_høyde = 0.6
    rad_avstand = 0.9
    
    for fold in range(k):
        y_pos = (k - 1 - fold) * rad_avstand
        
        for i in range(k):
            if i == fold:
                farge = val_farge
            else:
                farge = trening_farge
            
            rect = plt.Rectangle((i, y_pos), 1, boks_høyde,
                                 facecolor=farge,
                                 edgecolor=kant_farge,
                                 linewidth=1.5)
            ax.add_patch(rect)
        
        ax.text(-0.5, y_pos + boks_høyde/2, f'Fold {fold + 1}',
               ha='right', va='center', fontsize=10, fontweight='bold')
    
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=trening_farge, edgecolor=kant_farge, label='Treningsdata'),
        Patch(facecolor=val_farge, edgecolor=kant_farge, label='Valideringsdata')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
    ax.set_title(f'{k}-fold kryssvalidering', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(-1, k + 0.5)
    ax.set_ylim(-0.3, k * rad_avstand + 0.3)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    
    if lagre:
        filepath = FIGUR_KATALOG / filnavn
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figur lagret: {filepath}")
    
    return fig, ax


def plot_kfold_kryssvalidering_kuler(k=4, n_datapunkter=20, figsize=(14, 8), 
                                      lagre=False, filnavn="kfold_kuler.png"):
    """
    Visualiserer K-fold kryssvalidering med fargede kuler som representerer datapunkter.
    
    Denne figuren viser:
    - Hver rad representerer én iterasjon/fold
    - Fargede kuler representerer individuelle datapunkter
    - En ramme markerer test/valideringsfolden
    - Piler og etiketter forklarer oppdelingen
    
    Parametere:
    -----------
    k : int
        Antall folder (standard: 4)
    n_datapunkter : int
        Totalt antall datapunkter å vise (standard: 20)
    figsize : tuple
        Størrelse på figuren
    lagre : bool
        Om figuren skal lagres
    filnavn : str
        Filnavn for lagring
    """
    from matplotlib.patches import FancyBboxPatch, Circle
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.patches as mpatches
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # =========================================================================
    # FARGEPALETT - Matcher originalfiguren
    # =========================================================================
    # To hovedfarger for datapunktene (veksler mellom dem)
    farge_rod = '#E74C3C'          # Rød/korall
    farge_teal = '#1ABC9C'         # Teal/turkis
    
    # Lysere versjoner for testdata-seksjon (for å vise at de er "valgt ut")
    farge_rod_lys = '#F5B7B1'      # Lys rød/rosa
    farge_teal_lys = '#A3E4D7'     # Lys teal
    
    # Ramme og tekstfarger
    ramme_farge = '#2C3E50'        # Mørk blå/grå for rammer
    tekst_farge = '#3498DB'        # Blå for tekstbokser
    bakgrunn_farge = '#EBF5FB'     # Lys blå bakgrunn
    
    # =========================================================================
    # DIMENSJONER OG LAYOUT
    # =========================================================================
    kule_radius = 0.35
    kule_avstand = 0.9              # Avstand mellom kuler (senter til senter)
    rad_høyde = 1.8                 # Vertikal avstand mellom rader
    start_x = 3                     # X-posisjon der kulene starter
    
    # Beregn antall kuler per fold
    kuler_per_fold = n_datapunkter // k
    
    # Total bredde av alle kuler
    total_bredde = n_datapunkter * kule_avstand
    
    # =========================================================================
    # TEGN BAKGRUNN
    # =========================================================================
    bakgrunn = FancyBboxPatch(
        (start_x - 1, -0.5), 
        total_bredde + 1.5, 
        (k + 2) * rad_høyde,
        boxstyle="round,pad=0.1,rounding_size=0.3",
        facecolor=bakgrunn_farge,
        edgecolor=ramme_farge,
        linewidth=2
    )
    ax.add_patch(bakgrunn)
    
    # =========================================================================
    # FUNKSJON FOR Å TEGNE EN 3D-LIGNENDE KULE
    # =========================================================================
    def tegn_kule(ax, x, y, radius, farge, alpha=1.0):
        """
        Tegner en kule med 3D-effekt (gradient/skygge).
        """
        # Hovedsirkel
        circle = Circle((x, y), radius, 
                        facecolor=farge, 
                        edgecolor='white',
                        linewidth=0.5,
                        alpha=alpha)
        ax.add_patch(circle)
        
        # Lysrefleks (liten hvit sirkel øverst til venstre)
        refleks_x = x - radius * 0.3
        refleks_y = y + radius * 0.3
        refleks = Circle((refleks_x, refleks_y), radius * 0.2,
                         facecolor='white',
                         edgecolor='none',
                         alpha=0.6 * alpha)
        ax.add_patch(refleks)
        
        # Skygge (mørkere bue nederst)
        from matplotlib.patches import Arc
        skygge = Arc((x, y), radius * 1.8, radius * 1.8,
                    angle=0, theta1=200, theta2=340,
                    color='black', alpha=0.15 * alpha, linewidth=radius * 8)
        ax.add_patch(skygge)
    
    # =========================================================================
    # FUNKSJON FOR Å TEGNE TEKSTBOKS
    # =========================================================================
    def tegn_tekstboks(ax, x, y, tekst, farge=tekst_farge, fontsize=11):
        """
        Tegner en tekstboks med ramme.
        """
        bbox_props = dict(
            boxstyle="round,pad=0.3,rounding_size=0.2",
            facecolor='white',
            edgecolor=farge,
            linewidth=1.5
        )
        ax.text(x, y, tekst, ha='center', va='center',
               fontsize=fontsize, color=farge, fontweight='bold',
               bbox=bbox_props)
    
    # =========================================================================
    # TEGN OVERSKRIFTER OG PILER
    # =========================================================================
    topp_y = (k + 0.5) * rad_høyde
    
    # "Testdata" pil og etikett (over første fold-posisjon)
    test_start_x = start_x + kuler_per_fold * kule_avstand * 0.5
    tegn_tekstboks(ax, start_x + kuler_per_fold * kule_avstand / 2, topp_y + 0.8, 
                   'Testdata', farge=tekst_farge)
    
    # Pil ned fra "Testdata"
    ax.annotate('', xy=(start_x + kuler_per_fold * kule_avstand / 2, topp_y - 0.3),
                xytext=(start_x + kuler_per_fold * kule_avstand / 2, topp_y + 0.4),
                arrowprops=dict(arrowstyle='->', color=tekst_farge, lw=2))
    
    # "Treningsdata" pil og etikett
    trening_start_x = start_x + kuler_per_fold * kule_avstand
    trening_slutt_x = start_x + n_datapunkter * kule_avstand
    trening_midt_x = (trening_start_x + trening_slutt_x) / 2
    
    tegn_tekstboks(ax, trening_midt_x, topp_y + 0.8, 'Treningsdata', farge=tekst_farge)
    
    # Pil for treningsdata (horisontal med endepiler)
    ax.annotate('', xy=(trening_slutt_x - 0.5, topp_y - 0.3),
                xytext=(trening_start_x + 0.5, topp_y - 0.3),
                arrowprops=dict(arrowstyle='<->', color=tekst_farge, lw=2))
    
    # =========================================================================
    # TEGN ITERASJONER (RADER MED KULER)
    # =========================================================================
    for iterasjon in range(k):
        # Y-posisjon for denne raden (øverste rad først)
        y = (k - iterasjon) * rad_høyde
        
        # Iterasjonsetikett
        if iterasjon < k - 1:
            iterasjon_tekst = f'Iterasjon {iterasjon + 1}'
        else:
            iterasjon_tekst = f'Iterasjon k={k}'
        
        tegn_tekstboks(ax, 1.2, y, iterasjon_tekst, farge=tekst_farge, fontsize=10)
        
        # Pil fra tekstboks til kuler
        ax.annotate('', xy=(start_x - 0.8, y),
                    xytext=(2.2, y),
                    arrowprops=dict(arrowstyle='->', color=tekst_farge, lw=1.5))
        
        # Beregn hvilke kuler som er i testfolden for denne iterasjonen
        test_start_idx = iterasjon * kuler_per_fold
        test_slutt_idx = test_start_idx + kuler_per_fold
        
        # Tegn alle kuler for denne iterasjonen
        for i in range(n_datapunkter):
            x = start_x + i * kule_avstand
            
            # Velg farge basert på posisjon (veksler mellom rød og teal)
            if i % 2 == 0:
                base_farge = farge_rod
                lys_farge = farge_rod_lys
            else:
                base_farge = farge_teal
                lys_farge = farge_teal_lys
            
            # Bruk lysere farge for testdata
            if test_start_idx <= i < test_slutt_idx:
                kule_farge = lys_farge
            else:
                kule_farge = base_farge
            
            tegn_kule(ax, x, y, kule_radius, kule_farge)
        
        # Tegn ramme rundt testfolden
        ramme_x = start_x + test_start_idx * kule_avstand - kule_radius - 0.15
        ramme_bredde = kuler_per_fold * kule_avstand + 0.1
        ramme_y = y - kule_radius - 0.2
        ramme_høyde = kule_radius * 2 + 0.4
        
        test_ramme = FancyBboxPatch(
            (ramme_x, ramme_y), ramme_bredde, ramme_høyde,
            boxstyle="round,pad=0.02,rounding_size=0.1",
            facecolor='none',
            edgecolor=ramme_farge,
            linewidth=2.5
        )
        ax.add_patch(test_ramme)
        
        # Legg til vertikal stiplet linje etter siste rad (for "...")
        if iterasjon == 2:  # Etter iterasjon 3
            for dot_y in [y - rad_høyde * 0.3, y - rad_høyde * 0.5, y - rad_høyde * 0.7]:
                ax.plot(1.2, dot_y, 'o', color=tekst_farge, markersize=4)
                for dot_x in [start_x + n_datapunkter * kule_avstand / 3,
                             start_x + n_datapunkter * kule_avstand * 2 / 3]:
                    ax.plot(dot_x, dot_y, 'o', color=tekst_farge, markersize=3)
    
    # =========================================================================
    # TEGN "ALLE DATA" PILER OG ETIKETT NEDERST
    # =========================================================================
    bunn_y = 0.3
    
    # Horisontal pil for "Alle data"
    ax.annotate('', xy=(start_x + n_datapunkter * kule_avstand - 0.3, bunn_y),
                xytext=(start_x - 0.3, bunn_y),
                arrowprops=dict(arrowstyle='<->', color=tekst_farge, lw=2))
    
    tegn_tekstboks(ax, start_x + n_datapunkter * kule_avstand / 2, bunn_y - 0.7, 
                   'Alle data', farge=tekst_farge)
    
    # =========================================================================
    # JUSTER AKSER OG LAYOUT
    # =========================================================================
    ax.set_xlim(-0.5, start_x + n_datapunkter * kule_avstand + 1)
    ax.set_ylim(-1.5, (k + 2) * rad_høyde)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if lagre:
        filepath = FIGUR_KATALOG / filnavn
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figur lagret: {filepath}")
    
    return fig, ax


def plot_forvirringsmatrise_forklaring(figsize=(8, 6), lagre=False,
                                        filnavn="forvirringsmatrise_forklaring.png"):
    """
    Visualiserer strukturen til en forvirringsmatrise med forklaringer.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Farger
    tp_farge = '#27AE60'   # Grønn (bra)
    tn_farge = '#27AE60'   # Grønn (bra)
    fp_farge = '#E74C3C'   # Rød (feil)
    fn_farge = '#E74C3C'   # Rød (feil)
    
    # Tegn 2x2 matrise
    farger = [[tn_farge, fp_farge], [fn_farge, tp_farge]]
    etiketter = [['Sann\nNegativ\n(TN)', 'Falsk\nPositiv\n(FP)'],
                 ['Falsk\nNegativ\n(FN)', 'Sann\nPositiv\n(TP)']]
    
    for i in range(2):
        for j in range(2):
            rect = plt.Rectangle((j, 1-i), 1, 1,
                                 facecolor=farger[i][j],
                                 edgecolor='white',
                                 linewidth=3,
                                 alpha=0.7)
            ax.add_patch(rect)
            ax.text(j + 0.5, 1.5 - i, etiketter[i][j],
                   ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Akselabeler
    ax.text(1, -0.15, 'Predikert', ha='center', va='top', fontsize=12, fontweight='bold')
    ax.text(0.5, -0.35, 'Negativ', ha='center', va='top', fontsize=10)
    ax.text(1.5, -0.35, 'Positiv', ha='center', va='top', fontsize=10)
    
    ax.text(-0.15, 1, 'Faktisk', ha='right', va='center', fontsize=12, 
            fontweight='bold', rotation=90)
    ax.text(-0.3, 1.5, 'Negativ', ha='right', va='center', fontsize=10)
    ax.text(-0.3, 0.5, 'Positiv', ha='right', va='center', fontsize=10)
    
    ax.set_xlim(-0.6, 2.5)
    ax.set_ylim(-0.6, 2.3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if lagre:
        filepath = FIGUR_KATALOG / filnavn
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figur lagret: {filepath}")
    
    return fig, ax


def plot_sensitivitet_spesifisitet(figsize=(10, 14), lagre=False,
                                    filnavn="sensitivitet_spesifisitet.png"):
    """
    Visualiserer sensitivitet og spesifisitet med et Venn-lignende diagram.
    
    Figuren viser:
    - Venstre halvdel (grønn): Relevante elementer (faktisk positive/syke)
    - Høyre halvdel (grå): Ikke-relevante elementer (faktisk negative/friske)
    - Oval i midten: Utvalgte elementer (predikert positive)
    - Fire regioner: Sanne positive (TP), Falske positive (FP), 
                     Falske negative (FN), Sanne negative (TN)
    - Formler for sensitivitet og spesifisitet nederst
    """
    from matplotlib.patches import Ellipse, Circle, FancyBboxPatch, Rectangle
    from matplotlib.lines import Line2D
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # =========================================================================
    # FARGER
    # =========================================================================
    grønn_lys = '#C8E6C9'          # Lys grønn (relevant bakgrunn)
    grønn_mørk = '#81C784'         # Mørkere grønn (TP-region)
    grå_lys = '#E0E0E0'            # Lys grå (ikke-relevant bakgrunn)
    rød_lys = '#FFCDD2'            # Lys rød/rosa (FP-region)
    tekst_farge = '#333333'        # Mørk tekst
    ramme_farge = '#666666'        # Grå ramme
    
    # =========================================================================
    # DIMENSJONER
    # =========================================================================
    # Hovedrektangel
    rekt_x, rekt_y = 0, 4
    rekt_bredde, rekt_høyde = 10, 8
    
    # Ellipse (utvalgte elementer)
    ellipse_cx = rekt_x + rekt_bredde / 2
    ellipse_cy = rekt_y + rekt_høyde * 0.55
    ellipse_bredde = rekt_bredde * 0.7
    ellipse_høyde = rekt_høyde * 0.55
    
    # =========================================================================
    # TEGN BAKGRUNNSREKTANGLER (venstre: grønn, høyre: grå)
    # =========================================================================
    # Venstre halvdel (grønn - faktisk positive)
    venstre_rekt = FancyBboxPatch(
        (rekt_x, rekt_y), rekt_bredde / 2, rekt_høyde,
        boxstyle="round,pad=0,rounding_size=0.3",
        facecolor=grønn_lys,
        edgecolor=ramme_farge,
        linewidth=2
    )
    ax.add_patch(venstre_rekt)
    
    # Høyre halvdel (grå - faktisk negative)
    høyre_rekt = FancyBboxPatch(
        (rekt_x + rekt_bredde / 2, rekt_y), rekt_bredde / 2, rekt_høyde,
        boxstyle="round,pad=0,rounding_size=0.3",
        facecolor=grå_lys,
        edgecolor=ramme_farge,
        linewidth=2
    )
    ax.add_patch(høyre_rekt)
    
    # Ytre ramme
    ytre_ramme = FancyBboxPatch(
        (rekt_x, rekt_y), rekt_bredde, rekt_høyde,
        boxstyle="round,pad=0,rounding_size=0.3",
        facecolor='none',
        edgecolor=ramme_farge,
        linewidth=2.5
    )
    ax.add_patch(ytre_ramme)
    
    # =========================================================================
    # TEGN ELLIPSE (UTVALGTE ELEMENTER) MED TO FARGER
    # =========================================================================
    # Tegn ellipsen ved å fylle med mange små punkter/polygoner
    # Alternativ: bruk fill_between med ellipse-kurve
    
    # Generer ellipse-punkter
    theta = np.linspace(0, 2*np.pi, 200)
    ellipse_x = ellipse_cx + (ellipse_bredde/2) * np.cos(theta)
    ellipse_y = ellipse_cy + (ellipse_høyde/2) * np.sin(theta)
    
    # Venstre halvdel (grønn - sanne positive): theta fra pi/2 til 3pi/2
    theta_left = np.linspace(np.pi/2, 3*np.pi/2, 100)
    x_left = ellipse_cx + (ellipse_bredde/2) * np.cos(theta_left)
    y_left = ellipse_cy + (ellipse_høyde/2) * np.sin(theta_left)
    # Lukk formen
    x_left = np.append(x_left, x_left[0])
    y_left = np.append(y_left, y_left[0])
    ax.fill(x_left, y_left, color=grønn_mørk, alpha=0.8)
    
    # Høyre halvdel (rød - falske positive): theta fra -pi/2 til pi/2
    theta_right = np.linspace(-np.pi/2, np.pi/2, 100)
    x_right = ellipse_cx + (ellipse_bredde/2) * np.cos(theta_right)
    y_right = ellipse_cy + (ellipse_høyde/2) * np.sin(theta_right)
    # Lukk formen
    x_right = np.append(x_right, x_right[0])
    y_right = np.append(y_right, y_right[0])
    ax.fill(x_right, y_right, color=rød_lys, alpha=0.9)
    
    # Tegn ellipse-outline
    ax.plot(ellipse_x, ellipse_y, color=ramme_farge, linewidth=2)
    
    # =========================================================================
    # TEGN DATAPUNKTER (PRIKKER)
    # =========================================================================
    np.random.seed(42)  # For reproduserbarhet
    
    def tegn_fylt_prikk(x, y, radius=0.18):
        """Tegn fylt prikk (faktisk positiv)"""
        circle = Circle((x, y), radius, facecolor='#555555', edgecolor='#333333', linewidth=1)
        ax.add_patch(circle)
    
    def tegn_tom_prikk(x, y, radius=0.18):
        """Tegn tom prikk (faktisk negativ)"""
        circle = Circle((x, y), radius, facecolor='white', edgecolor='#555555', linewidth=1.5)
        ax.add_patch(circle)
    
    # Sanne positive (fylte prikker inne i ellipsen, venstre side)
    tp_posisjoner = [(2.5, 9.5), (3.2, 8.5), (2.8, 7.5), (3.5, 8.0), (4.0, 9.0), (3.0, 8.8)]
    for x, y in tp_posisjoner:
        tegn_fylt_prikk(x, y)
    
    # Falske negative (fylte prikker utenfor ellipsen, venstre side)
    fn_posisjoner = [(1.0, 10.5), (0.8, 9.0), (1.5, 7.0), (2.0, 5.5), (0.5, 6.5), 
                     (1.2, 11.0), (2.5, 5.0), (1.8, 10.8)]
    for x, y in fn_posisjoner:
        tegn_fylt_prikk(x, y)
    
    # Falske positive (tomme prikker inne i ellipsen, høyre side)
    fp_posisjoner = [(6.0, 9.0), (6.5, 8.0), (7.0, 8.8), (5.8, 7.5)]
    for x, y in fp_posisjoner:
        tegn_tom_prikk(x, y)
    
    # Sanne negative (tomme prikker utenfor ellipsen, høyre side)
    tn_posisjoner = [(8.0, 10.5), (9.0, 9.5), (8.5, 6.0), (9.5, 8.0), 
                     (8.2, 11.0), (9.2, 7.0), (7.5, 5.5), (9.0, 5.0)]
    for x, y in tn_posisjoner:
        tegn_tom_prikk(x, y)
    
    # =========================================================================
    # ETIKETTER FOR REGIONENE
    # =========================================================================
    # Øvre etiketter
    ax.text(rekt_bredde / 4, rekt_y + rekt_høyde - 0.6, 'falske negative',
           ha='center', va='center', fontsize=14, fontstyle='italic', color=tekst_farge)
    ax.text(3 * rekt_bredde / 4, rekt_y + rekt_høyde - 0.6, 'sanne negative',
           ha='center', va='center', fontsize=14, fontstyle='italic', color=tekst_farge)
    
    # Etiketter inne i ellipsen
    ax.text(3.0, 8.2, 'sanne\npositive',
           ha='center', va='center', fontsize=14, fontstyle='italic', color=tekst_farge)
    ax.text(6.5, 8.2, 'falske\npositive',
           ha='center', va='center', fontsize=14, fontstyle='italic', color=tekst_farge)
    
    # =========================================================================
    # OVERSKRIFTER MED KLAMMEPARENTESER
    # =========================================================================
    # "relevante elementer" (øverst, over venstre halvdel)
    brace_y_top = rekt_y + rekt_høyde + 0.3
    ax.plot([rekt_x + 0.2, rekt_x + 0.2], [brace_y_top, brace_y_top + 0.2], 'k-', lw=1.5)
    ax.plot([rekt_x + 0.2, rekt_x + rekt_bredde/2 - 0.2], [brace_y_top + 0.2, brace_y_top + 0.2], 'k-', lw=1.5)
    ax.plot([rekt_x + rekt_bredde/2 - 0.2, rekt_x + rekt_bredde/2 - 0.2], [brace_y_top, brace_y_top + 0.2], 'k-', lw=1.5)
    ax.text(rekt_bredde / 4, brace_y_top + 0.6, 'relevante elementer',
           ha='center', va='bottom', fontsize=15, fontweight='bold', color=tekst_farge)
    
    # "utvalgte elementer" (nederst, under ellipsen)
    brace_y_bottom = rekt_y - 0.3
    # Pil ned fra ellipsen til etiketten
    ax.annotate('', xy=(ellipse_cx, brace_y_bottom - 0.5),
                xytext=(ellipse_cx, rekt_y + 0.5),
                arrowprops=dict(arrowstyle='-', color='black', lw=1.5))
    ax.plot([ellipse_cx - 0.1, ellipse_cx + 0.1], [brace_y_bottom - 0.5, brace_y_bottom - 0.5], 'k-', lw=1.5)
    ax.text(ellipse_cx, brace_y_bottom - 0.9, 'utvalgte elementer',
           ha='center', va='top', fontsize=15, fontweight='bold', color=tekst_farge)
    
    # =========================================================================
    # FORKLARINGER NEDERST
    # =========================================================================
    forklaring_y = 1.5
    
    # Venstre forklaring (Sensitivitet)
    ax.text(2.5, forklaring_y + 0.8, 'Hvor mange relevante\nelementer er valgt?',
           ha='center', va='top', fontsize=13, color=tekst_farge, linespacing=1.3)
    ax.text(2.5, forklaring_y - 0.3, 'F.eks. Hvor mange syke\nblir korrekt identifisert\nsom syke.',
           ha='center', va='top', fontsize=11, color='#666666', fontstyle='italic', linespacing=1.3)
    
    # Høyre forklaring (Spesifisitet)
    ax.text(7.5, forklaring_y + 0.8, 'Hvor mange ikke-utvalgte\nelementer er faktisk negative?',
           ha='center', va='top', fontsize=13, color=tekst_farge, linespacing=1.3)
    ax.text(7.5, forklaring_y - 0.3, 'F.eks. Hvor mange friske\nblir korrekt identifisert\nsom friske.',
           ha='center', va='top', fontsize=11, color='#666666', fontstyle='italic', linespacing=1.3)
    
    # =========================================================================
    # FORMLER FOR SENSITIVITET OG SPESIFISITET
    # =========================================================================
    formel_y = -1.0
    
    # Sensitivitet
    ax.text(2.5, formel_y, 'Sensitivitet =',
           ha='right', va='center', fontsize=16, fontweight='bold', color=tekst_farge)
    
    # Brøkstrek og mini-diagrammer for sensitivitet
    # Teller: grønn halvdel av sirkel (TP)
    sens_teller_x = 3.3
    from matplotlib.patches import Wedge
    
    # Grønn halvsirkel (høyre side = TP i utvalgte)
    wedge_tp = Wedge((sens_teller_x, formel_y + 0.35), 0.25, -90, 90, 
                     facecolor=grønn_mørk, edgecolor=ramme_farge, linewidth=1)
    ax.add_patch(wedge_tp)
    # Hvit halvsirkel (venstre side)
    wedge_white1 = Wedge((sens_teller_x, formel_y + 0.35), 0.25, 90, 270,
                         facecolor='white', edgecolor=ramme_farge, linewidth=1)
    ax.add_patch(wedge_white1)
    
    # Brøkstrek
    ax.plot([sens_teller_x - 0.4, sens_teller_x + 0.4], [formel_y, formel_y], 'k-', lw=2)
    
    # Nevner: hele grønn sirkel (alle positive)
    circle_all_pos = Circle((sens_teller_x, formel_y - 0.35), 0.25,
                            facecolor=grønn_mørk, edgecolor=ramme_farge, linewidth=1)
    ax.add_patch(circle_all_pos)
    
    # Spesifisitet
    ax.text(7.0, formel_y, 'Spesifisitet =',
           ha='right', va='center', fontsize=16, fontweight='bold', color=tekst_farge)
    
    # Mini-diagrammer for spesifisitet
    spek_teller_x = 7.8
    
    # Teller: grå halvsirkel (TN - ikke utvalgte som er negative)
    wedge_tn = Wedge((spek_teller_x, formel_y + 0.35), 0.25, 90, 270,
                     facecolor=grå_lys, edgecolor=ramme_farge, linewidth=1)
    ax.add_patch(wedge_tn)
    # Hvit halvsirkel (høyre side)
    wedge_white2 = Wedge((spek_teller_x, formel_y + 0.35), 0.25, -90, 90,
                         facecolor='white', edgecolor=ramme_farge, linewidth=1)
    ax.add_patch(wedge_white2)
    
    # Brøkstrek
    ax.plot([spek_teller_x - 0.4, spek_teller_x + 0.4], [formel_y, formel_y], 'k-', lw=2)
    
    # Nevner: grå + rød (alle negative) - vis som rektangel med to farger
    from matplotlib.patches import Rectangle
    # Grå halvdel
    rect_neg = Rectangle((spek_teller_x - 0.3, formel_y - 0.55), 0.3, 0.4,
                         facecolor=grå_lys, edgecolor=ramme_farge, linewidth=1)
    ax.add_patch(rect_neg)
    # Rød halvdel  
    rect_fp = Rectangle((spek_teller_x, formel_y - 0.55), 0.3, 0.4,
                        facecolor=rød_lys, edgecolor=ramme_farge, linewidth=1)
    ax.add_patch(rect_fp)
    
    # =========================================================================
    # JUSTER AKSER
    # =========================================================================
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2.5, 14)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    
    if lagre:
        filepath = FIGUR_KATALOG / filnavn
        fig.savefig(filepath, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"✓ Figur lagret: {filepath}")
    
    return fig, ax


def generer_alle_figurer():
    """
    Genererer og lagrer alle figurer til figurer/-katalogen.
    Kjør denne funksjonen for å oppdatere alle figurer.
    """
    print("Genererer figurer for ELMED219 notebooks...")
    print("=" * 50)
    
    # Enkel trenings-/testsett-oppdeling (Figur 3)
    fig, ax = plot_trening_test_split(lagre=True)
    plt.close(fig)
    
    # Datasett-oppdeling med validering (Figur 4)
    fig, ax = plot_datasett_oppdeling(lagre=True)
    plt.close(fig)
    
    # K-fold kryssvalidering (enkel versjon)
    fig, ax = plot_kfold_kryssvalidering(lagre=True)
    plt.close(fig)
    
    # K-fold kryssvalidering med kuler (detaljert versjon)
    fig, ax = plot_kfold_kryssvalidering_kuler(lagre=True)
    plt.close(fig)
    
    # Forvirringsmatrise forklaring
    fig, ax = plot_forvirringsmatrise_forklaring(lagre=True)
    plt.close(fig)
    
    # Sensitivitet og spesifisitet
    fig, ax = plot_sensitivitet_spesifisitet(lagre=True)
    plt.close(fig)
    
    print("=" * 50)
    print("✓ Alle figurer generert!")


if __name__ == "__main__":
    generer_alle_figurer()

