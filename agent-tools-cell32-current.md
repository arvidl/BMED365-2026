---

# 🩺 Et medisinsk eksempel: Diabetes-prediksjon

Nå tar vi steget fra blomster til **ekte medisin**! Vi skal bruke maskinlæring til å predikere diabetes – en av de største folkehelseutfordringene i verden.

## Hvorfor diabetes?

### Den globale diabetesepidemien

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DIABETES I TALL (2024)                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   🌍  537 millioner voksne lever med diabetes globalt               │
│   📈  Forventet å øke til 783 millioner innen 2045                  │
│   ⚠️  1 av 2 voksne med diabetes er udiagnostisert                  │
│   💀  6.7 millioner dødsfall årlig relatert til diabetes            │
│   🇳🇴  ~245 000 nordmenn har diabetes (5% av befolkningen)           │
│                                                                     │
│   Kilde: International Diabetes Federation (IDF)                    │
└─────────────────────────────────────────────────────────────────────┘
```

### Hvorfor er tidlig oppdagelse viktig?

Diabetes utvikler seg ofte **gradvis og uten symptomer**. Mange lever med uoppdaget diabetes i årevis, og i mellomtiden:

| Komplikasjon | Risiko ved ubehandlet diabetes |
|--------------|-------------------------------|
| **Hjertesykdom** | 2-4x høyere risiko for hjerteinfarkt og slag |
| **Nyresvikt** | Ledende årsak til dialyse |
| **Synstap** | Diabetisk retinopati kan føre til blindhet |
| **Amputasjon** | Nerveskader og dårlig sirkulasjon i føtter |
| **Nevropati** | Kroniske smerter og følelsestap |

> 💡 **Maskinlæringens rolle:** Ved å identifisere høyrisiko-pasienter tidlig kan vi:
> - Starte forebyggende tiltak (livsstilsendringer)
> - Sette inn behandling før komplikasjoner oppstår
> - Redusere helsekostnader og menneskelig lidelse

---

## Pima Indians Diabetes Database

Vi bruker et klassisk medisinsk datasett: **Pima Indians Diabetes Database**.

### Bakgrunn

Datasettet stammer fra en studie utført av National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK) på **Pima-indianere i Arizona, USA**.

**Hvorfor akkurat denne befolkningen?**
- Pima-indianerne har en av verdens høyeste forekomster av type 2-diabetes
- Genetiske og livsstilsfaktorer gjør dem til en viktig studiepopulasjon
- Studien har bidratt enormt til vår forståelse av diabetesrisikofaktorer

### Om datasettet

| Egenskap | Verdi |
|----------|-------|
| **Antall pasienter** | 768 kvinner |
| **Alder** | ≥ 21 år |
| **Etnisitet** | Pima-indianere |
| **Antall egenskaper** | 8 |
| **Målvariabel** | Diabetes (ja/nei) |
| **Balanse** | ~35% har diabetes, ~65% har ikke |

---

## 📊 Egenskapene (Features) i datasettet

Hver pasient er beskrevet med 8 kliniske measurements:

| # | Egenskap | Beskrivelse | Typisk normalverdi |
|---|----------|-------------|-------------------|
| 1 | **pregnancies** | Antall graviditeter | - |
| 2 | **glucose** | Plasmaglukose etter 2 timer (oral glukosetoleranse-test) | < 140 mg/dL |
| 3 | **diastolic** | Diastolisk blodtrykk (mm Hg) | 60-80 mm Hg |
| 4 | **triceps** | Hudfold-tykkelse på triceps (mm) | - |
| 5 | **insulin** | 2-timers serum-insulin (µU/ml) | 16-166 µU/ml |
| 6 | **bmi** | Body Mass Index (kg/m²) | 18.5-24.9 |
| 7 | **dpf** | Diabetes Pedigree Function (genetisk risiko) | - |
| 8 | **age** | Alder (år) | - |

### Hva er disse egenskapene?

**🩸 Glucose (plasmaglukose)**
- Måles etter oral glukosetoleransetest (OGTT)
- Viser hvor godt kroppen håndterer sukker
- Høye verdier indikerer insulinresistens eller diabetes

**💓 Diastolic (blodtrykk)**
- Det "nedre" blodtrykket (når hjertet hviler)
- Høyt blodtrykk er assosiert med diabetes og hjertesykdom

**📏 Triceps (hudfoldtykkelse)**
- Mål på underhudsfett
- Indikerer generell kroppsfettandel

**💉 Insulin**
- Hormonet som regulerer blodsukker
- Høye verdier kan indikere insulinresistens (kroppen trenger mer insulin)

**⚖️ BMI (Body Mass Index)**
- Standardmål for vekt i forhold til høyde
- BMI > 25 = overvekt, BMI > 30 = fedme
- Sterk risikofaktor for type 2-diabetes

**🧬 Diabetes Pedigree Function (DPF)**
- Kompleks genetisk risikoberegning
- Basert på diabetesforekomst i familien
- Høyere verdi = høyere genetisk risiko

**🎂 Age (alder)**
- Risikoen for type 2-diabetes øker med alderen
- Spesielt etter 45 år

---

## Utfordringer med dette datasettet

I motsetning til Iris-datasettet har diabetes-datasettet flere **realistiske utfordringer**:

| Utfordring | Beskrivelse | Konsekvens |
|------------|-------------|------------|
| **Overlappende klasser** | Friske og syke har lignende verdier | Vanskeligere å skille |
| **Manglende verdier** | Noen measurements er 0 (som egentlig er missing) | Må håndteres |
| **Ubalanserte klasser** | 65% ikke-diabetes, 35% diabetes | Accuracy kan være misvisende |
| **Biologisk variasjon** | Stor naturlig variasjon mellom individer | Lavere nøyaktighet |
| **Latente faktorer** | Livsstil, kosthold ikke inkludert | Mangler viktig informasjon |

> ⚠️ **Viktig lærdom:** I virkelig medisinsk AI er det sjelden så "pent" som i lærebokeksempler. Denne kompleksiteten gjør diabetes-datasettet til et utmerket eksempel på realistisk maskinlæring!

---

## Etiske betraktninger

Før vi begynner, la oss reflektere over noen etiske aspekter:

1. **Populasjonsspesifisitet**: Modellen er trent på Pima-kvinner – fungerer den på andre populasjoner?
2. **Kjønnsbalanse**: Kun kvinner i datasettet – kan vi generalisere til menn?
3. **Historisk kontekst**: Dataene er fra 1988 – er de fortsatt relevante?
4. **Beslutningsstøtte, ikke erstatning**: En slik modell bør *støtte* leger, ikke erstatte dem

---

## La oss laste inn og utforske dataene!