import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import numpy as np
import seaborn as sns

# Konfigurasjon
plt.style.use('seaborn-v0_8-whitegrid')
UIB_BLUE = '#003A70'
ACCENT_ORANGE = '#E67E22'
LIGHT_BG = '#F5F7FA'

# Opprett figur
fig = plt.figure(figsize=(16, 22), facecolor='white')
gs = gridspec.GridSpec(5, 2, figure=fig, height_ratios=[0.5, 1.5, 1.5, 1.5, 0.5], hspace=0.3, wspace=0.2)

# =============================================================================
# 1. HEADER
# =============================================================================
ax_header = fig.add_subplot(gs[0, :])
ax_header.set_facecolor(UIB_BLUE)
ax_header.axis('off')

# Blå boks bak header
rect = patches.Rectangle((0, 0), 1, 1, transform=ax_header.transAxes, color=UIB_BLUE, zorder=0)
ax_header.add_patch(rect)

ax_header.text(0.5, 0.7, "ELMED219: LAB 0 - MASKINLÆRING I MEDISIN", 
              ha='center', va='center', fontsize=32, fontweight='bold', color='white')
ax_header.text(0.5, 0.35, "Fra data til diagnose: En reise gjennom Iris, Diabetes og Etikk", 
              ha='center', va='center', fontsize=20, color='#DDDDDD')

# =============================================================================
# 2. KONSEPTET: ML & IRIS (Venstre side)
# =============================================================================
ax_iris = fig.add_subplot(gs[1, 0])
ax_iris.set_title("1. KONSEPTET: Maskinlæring lærer mønstre", fontsize=16, fontweight='bold', color=UIB_BLUE, loc='left')

# Generer syntetiske Iris-data for illustrasjon
np.random.seed(42)
x1 = np.random.normal(1.5, 0.2, 30)
y1 = np.random.normal(0.3, 0.1, 30)
x2 = np.random.normal(4.0, 0.4, 30)
y2 = np.random.normal(1.3, 0.2, 30)
x3 = np.random.normal(5.5, 0.5, 30)
y3 = np.random.normal(2.0, 0.3, 30)

ax_iris.scatter(x1, y1, c='red', label='Setosa', alpha=0.7, s=80)
ax_iris.scatter(x2, y2, c='green', label='Versicolor', alpha=0.7, s=80)
ax_iris.scatter(x3, y3, c='blue', label='Virginica', alpha=0.7, s=80)
ax_iris.set_xlabel("Petal Length")
ax_iris.set_ylabel("Petal Width")
ax_iris.legend(loc='upper left')
ax_iris.text(0.5, -0.15, "Maskinlæring finner linjene som skiller gruppene automatisk.", 
            transform=ax_iris.transAxes, ha='center', fontsize=12, style='italic', bbox=dict(facecolor=LIGHT_BG, alpha=0.5, edgecolor='none'))

# =============================================================================
# 3. MODELLEN: RANDOM FOREST (Høyre side)
# =============================================================================
ax_model = fig.add_subplot(gs[1, 1])
ax_model.axis('off')
ax_model.set_title("2. MODELLEN: Random Forest", fontsize=16, fontweight='bold', color=UIB_BLUE, loc='left')

def draw_tree(ax, x, y, scale=1):
    ax.add_patch(patches.Rectangle((x-0.02*scale, y-0.2*scale), 0.04*scale, 0.2*scale, color='brown'))
    ax.add_patch(patches.Polygon([[x-0.15*scale, y], [x+0.15*scale, y], [x, y+0.3*scale]], color='green'))

draw_tree(ax_model, 0.2, 0.5, 0.8)
draw_tree(ax_model, 0.5, 0.5, 0.8)
draw_tree(ax_model, 0.8, 0.5, 0.8)

ax_model.text(0.5, 0.2, "Ensemble av beslutningstrær", ha='center', fontsize=14, fontweight='bold')
ax_model.text(0.5, 0.1, "\"Flertallsavstemning gir robusthet\"", ha='center', fontsize=12, style='italic')

ax_model.annotate("", xy=(0.5, 0.4), xytext=(0.5, 0.0), arrowprops=dict(arrowstyle="->", lw=2))
ax_model.text(0.5, 0.85, "Prediksjon", ha='center', fontsize=14, fontweight='bold', color=ACCENT_ORANGE)


# =============================================================================
# 4. EVALUERING: CONFUSION MATRIX (Venstre side)
# =============================================================================
ax_cm = fig.add_subplot(gs[2, 0])
ax_cm.set_title("3. EVALUERING: Accuracy er ikke alt", fontsize=16, fontweight='bold', color=UIB_BLUE, loc='left')

cm_data = np.array([[98, 22], [29, 43]])
sns.heatmap(cm_data, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax_cm, annot_kws={"size": 20})
ax_cm.set_xlabel('Predikert')
ax_cm.set_ylabel('Faktisk')
ax_cm.set_xticklabels(['Frisk', 'Syk'])
ax_cm.set_yticklabels(['Frisk', 'Syk'])

ax_cm.text(1.6, 0.5, "Falske Positive\n(Unødvendig test)", color='red', ha='center', va='center', fontsize=10)
ax_cm.text(0.4, 1.5, "Falske Negative\n(FARLIG!)", color='red', ha='center', va='center', fontsize=10, fontweight='bold')


# =============================================================================
# 5. XAI: FEATURE IMPORTANCE (Høyre side)
# =============================================================================
ax_xai = fig.add_subplot(gs[2, 1])
ax_xai.set_title("4. XAI: Åpne den svarte boksen", fontsize=16, fontweight='bold', color=UIB_BLUE, loc='left')

features = ['Glucose', 'BMI', 'Age', 'DPF', 'Pregnancies']
importance = [0.28, 0.18, 0.14, 0.10, 0.08]

y_pos = np.arange(len(features))
ax_xai.barh(y_pos, importance, align='center', color=ACCENT_ORANGE)
ax_xai.set_yticks(y_pos)
ax_xai.set_yticklabels(features)
ax_xai.invert_yaxis()
ax_xai.set_xlabel('Viktighet')

ax_xai.text(0.6, 0.5, "Hva driver risikoen?\n\nGlukose og BMI er\nde viktigste faktorene\nfor modellen.", 
           transform=ax_xai.transAxes, ha='left', va='center', fontsize=12, bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="gray", alpha=0.8))


# =============================================================================
# 6. ETISKE UTFORDRINGER (Venstre side)
# =============================================================================
ax_ethics = fig.add_subplot(gs[3, 0])
ax_ethics.axis('off')
ax_ethics.set_title("5. ETIKK & BIAS", fontsize=16, fontweight='bold', color=UIB_BLUE, loc='left')

circle1 = patches.Circle((0.2, 0.6), 0.15, color='#e74c3c', alpha=0.2)
circle2 = patches.Circle((0.5, 0.6), 0.15, color='#3498db', alpha=0.2)
circle3 = patches.Circle((0.8, 0.6), 0.15, color='#9b59b6', alpha=0.2)
ax_ethics.add_patch(circle1)
ax_ethics.add_patch(circle2)
ax_ethics.add_patch(circle3)

ax_ethics.text(0.2, 0.6, "Populasjons-\nbias", ha='center', va='center', fontsize=12, fontweight='bold')
ax_ethics.text(0.5, 0.6, "Historisk\nbias", ha='center', va='center', fontsize=12, fontweight='bold')
ax_ethics.text(0.8, 0.6, "Kjønns-\nbias", ha='center', va='center', fontsize=12, fontweight='bold')

ax_ethics.text(0.5, 0.2, "Kan vi bruke Pima-data (1988) på norske pasienter i 2026?", 
              ha='center', fontsize=12, style='italic', bbox=dict(facecolor='#FEF9E7', edgecolor='none'))

# =============================================================================
# 7. TRUSTWORTHY AI (Høyre side)
# =============================================================================
ax_trust = fig.add_subplot(gs[3, 1])
ax_trust.axis('off')
ax_trust.set_title("6. TRUSTWORTHY AI", fontsize=16, fontweight='bold', color=UIB_BLUE, loc='left')

# Bruk tekst i stedet for emojis som kan mangle glypher
pillars = [
    "(1) NØYAKTIGHET",
    "(2) FORKLARBARHET",
    "(3) RETTFERDIGHET",
    "(4) ROBUSTHET",
    "(5) PERSONVERN",
    "(6) ANSVARLIGHET"
]

for i, pillar in enumerate(pillars):
    col = 0 if i < 3 else 1
    row = i % 3
    ax_trust.text(0.1 + col*0.5, 0.8 - row*0.25, pillar, fontsize=14, fontweight='bold', color='#333333')

# =============================================================================
# 8. FOOTER
# =============================================================================
ax_footer = fig.add_subplot(gs[4, :])
ax_footer.set_facecolor(UIB_BLUE)
ax_footer.axis('off')
rect_foot = patches.Rectangle((0, 0), 1, 1, transform=ax_footer.transAxes, color=UIB_BLUE, zorder=0)
ax_footer.add_patch(rect_foot)

ax_footer.text(0.5, 0.5, "Konklusjon: Medisinsk AI handler om mer enn bare accuracy. Kontekst, etikk og forklaring er nøkkelen.", 
              ha='center', va='center', fontsize=18, color='white', fontweight='bold')

# Lagre
plt.savefig('Lab0-ML/ELMED219_Lab0_Infographic.png', dpi=300, bbox_inches='tight')
print("Infografikk lagret som Lab0-ML/ELMED219_Lab0_Infographic.png")
