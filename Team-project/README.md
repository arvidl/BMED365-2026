# Team Project &nbsp;&nbsp;&nbsp; <span style="font-size: 16px;">[ELMED219 / BMED365]</span>
## _Precision Medicine and Quantitative Imaging in Glioblastoma_

> **Note:** This is a joint project between ELMED219 and BMED365. The **project report should be written in English** (see the [LaTeX template](./latex-template/)).

---

## Description

Imagine that you are part of a group of established, successful researchers who will collaborate on an important biomedical and medical challenge. An open call for research projects has been announced under a new umbrella program titled "Artificial Intelligence and Computational (Bio)medicine". Your interdisciplinary group is aiming for a project on "Precision Medicine and Quantitative Imaging in Glioblastoma – A Multiscale Approach".

> **Important:** The task is to **write a research plan** (a grant proposal sketch) for a hypothetical project – **not** to actually conduct the project with data analysis or coding. You should describe *what* you would do, *how* and *why*, but not perform the actual analysis.

The focus of the assignment is:

1. Description of relevant imaging technologies and modalities – possibly at different scales
2. Proposals for image-derived biomarkers for glioblastoma
3. Machine learning techniques for segmentation, classification, treatment stratification, and prediction
4. The novelty and expected impact of your approach
5. Evaluation of the ethics of your project, along with a data management plan (and not so much the basic science of brain tumors itself)


## Report Organization

### Research Plan
(3-5 pages incl. figures and reference list)
- A brief background to the field
- Objectives and expected impact
- Materials and methods
- Evaluation

### Data Management Plan and Ethical Considerations
(1½-2½ pages incl. graphics / links)
- Description of collected/generated data and code
- Data and code sharing
- Ethical considerations

---

## *Prepare yourself and your computer for the team project*

### *Familiarize yourself with the material for the group project and how to use [LaTeX](https://www.latex-project.org) to write the report*

- We use the online, collaborative LaTeX editor [Overleaf](https://www.overleaf.com) (for more information about LaTeX, see [here](https://en.wikipedia.org/wiki/LaTeX), [here](https://www.tug.org/pracjourn/2007-4/senthil/senthil.pdf) and [here](https://mildopinions.wordpress.com/2008/07/07/why-i-use-latex-in-biology), and for LaTeX templates, see e.g. [here](https://www.overleaf.com/latex/templates/template-for-submissions-to-molecular-systems-biology/kyxgttpbzhht) and [here](https://www.overleaf.com/latex/templates/tagged/academic-journal))

- **LaTeX template for the report** can be found [[here](./latex-template/BMED365_2026_project_team_k.tex)] with an example figure [[here](./latex-template/bmed365_dummy_fig.png)], resulting in the following example report [[pdf](./latex-template/BMED365_2026_project_team_k.pdf)].

- **Expected level of detail** is illustrated by a [project report](https://www.overleaf.com/read/xwjxwcnpzhqv) from the summer school in Seili 2019 (where *Prostate Cancer* was the theme). It is available on Overleaf [[here](https://www.overleaf.com/project/5ec71af71aca320001385354)] and in this repo as [[main.tex](./latex-template/Seili_2020_example/main.tex)], [[fig1](./latex-template/Seili_2020_example/Fig1_The_process_of_autoEncoder.png)], [[fig2](./latex-template/Seili_2020_example/Fig2_Overview_of_the_process.png)], resulting in [[pdf](./latex-template/Seili_2020_example/Seili_2020_project_template.pdf)].


---

## Information Sources (Brain Tumors – Neuroimaging – AI – Software and Data)

### Background Knowledge and Reading

- For those of you with limited knowledge of brain biology and pathology or who wish to refresh your knowledge, we recommend the free Coursera course [https://www.coursera.org/learn/neurobiology](https://www.coursera.org/learn/neurobiology), especially the lecture on [brain tumors](https://www.coursera.org/lecture/neurobiology/brain-tumors-fUcn4).

- The Brain Atlas: [https://www.proteinatlas.org/humanproteome/brain](https://www.proteinatlas.org/humanproteome/brain)

#### WHO Classification of CNS Tumors (updated 2021)

- Louis DN et al. **The 2021 WHO Classification of Tumors of the Central Nervous System: a summary.** Neuro-Oncology 2021;23(8):1231-1251. [[link](https://academic.oup.com/neuro-oncology/article/23/8/1231/6311214)]
  - *Note: The WHO 2021 classification introduces important changes, including that the diagnosis "Glioblastoma, IDH-wildtype" now requires IDH mutation analysis.*

- Louis DN et al. The 2016 World Health Organization Classification of Tumors of the Central Nervous System: A Summary. Acta Neuropathol 2016;131(6):803-820. [[link](https://link.springer.com/article/10.1007/s00401-016-1545-1)]

- Aldape K et al. Challenges to curing primary brain tumors. Nat Rev Clin Oncol 2019;16:509-520. [[link](https://www.nature.com/articles/s41571-019-0177-5)]

---

### Brain Tumors and Neuroimaging (Selected References)

- Abd-Ellah MK et al. A review on brain tumor diagnosis from MRI images: Practical implications, key achievements, and lessons learned. Magnetic Resonance Imaging 2019;61:300-318. [[link](https://www.sciencedirect.com/science/article/pii/S0730725X18304302)]

- Hamid MAA, Khan NA. Investigation and Classification of MRI Brain Tumors Using Feature Extraction Technique. Journal of Medical and Biological Engineering 2020;40:307–317. [[link](https://link.springer.com/article/10.1007/s40846-020-00510-1)]

- Lohmann P et al. PET/MRI Radiomics in Patients With Brain Metastases. Front. Neurol., 07 February 2020. [[link](https://www.frontiersin.org/articles/10.3389/fneur.2020.00001/full)]

- Tiwari A et al. Brain tumor segmentation and classification from magnetic resonance images: Review of selected methods from 2014 to 2019. Pattern Recognition Letters 2020;131:244-260. [[link](https://www.sciencedirect.com/science/article/pii/S016786551930340X)]

- Nadeem MW et al. Brain Tumor Analysis Empowered with Deep Learning: A Review, Taxonomy, and Future Challenges. Brain Sci 2020;10(2):118. [[link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7071415)]

#### BraTS Challenge (Brain Tumor Segmentation)

- **BraTS Challenge** is an annual international competition focusing on brain tumor segmentation from MRI images. From 2023, the competition is organized via the Synapse platform.

- BraTS 2023/2024 Challenge: [[synapse.org/brats](https://www.synapse.org/brats)]

- Menze BH et al. The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS). IEEE Trans Med Imaging 2015;34(10):1993-2024. [[link](https://ieeexplore.ieee.org/document/6975210)]

- Bakas S et al. Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features. Scientific Data 2017;4:170117. [[link](https://www.nature.com/articles/sdata2017117)]

---

### Brain Tumors and Artificial Intelligence (Selected References)

- NCI: Artificial Intelligence Expedites Brain Tumor Diagnosis during Surgery. 2020 Feb 12. [[link](https://www.cancer.gov/news-events/cancer-currents-blog/2020/artificial-intelligence-brain-tumor-diagnosis-surgery)]

- Hollon TC et al. Near Real-Time Intraoperative Brain Tumor Diagnosis Using Stimulated Raman Histology and Deep Neural Networks. Nature Medicine 2020;26(1):52-58. [[link](https://www.nature.com/articles/s41591-019-0715-9)] [[GitHub](https://github.com/toddhollon/srh_cnn)] [[video](https://labblog.uofmhealth.org/health-tech/artificial-intelligence-improves-brain-tumor-diagnosis)]

- Yogananda CGB et al. A novel fully automated MRI-based deep-learning method for classification of IDH mutation status in brain gliomas. Neuro-Oncology 2020;22(3):402–411. [[link](https://academic.oup.com/neuro-oncology/article/22/3/402/5584591)]

- Kickingereder P et al. Automated quantitative tumour response assessment of MRI in neuro-oncology with artificial neural networks: a multicentre, retrospective study. The Lancet Oncology 2019;20(5):728-740. [[link](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30098-1/fulltext)]

- Eitel F et al. Patch individual filter layers in CNNs to harness the spatial homogeneity of neuroimaging data. Scientific Reports 2021;11:24447. [[link](https://www.nature.com/articles/s41598-021-03785-9)]

#### Recent AI Articles on Brain Tumors (2022-2024)

- Rudie JD et al. **Emerging Applications of Artificial Intelligence in Neuro-Oncology.** Radiology 2019;290(3):607-618. [[link](https://pubs.rsna.org/doi/10.1148/radiol.2019181928)]

- Pati S et al. **Federated learning enables big data for rare cancer boundary detection.** Nature Communications 2022;13:7346. [[link](https://www.nature.com/articles/s41467-022-33407-5)]
  - *Describes the FeTS (Federated Tumor Segmentation) initiative that enables collaboration between institutions without sharing sensitive patient data.*

- Kofler F et al. **BraTS Toolkit: Translating BraTS Brain Tumor Segmentation Algorithms Into Clinical and Scientific Practice.** Frontiers in Neuroscience 2020;14:125. [[link](https://www.frontiersin.org/articles/10.3389/fnins.2020.00125)]

---

### Software and Data (Resources to Describe in the Research Plan)

Even though you will not run code or analyze data yourself, it is important to know which tools and datasets exist – so that you can describe them realistically in the research plan.

#### Papers With Code and GitHub Resources

- Brain Tumor Segmentation | Papers With Code: [[paperswithcode.com/task/brain-tumor-segmentation](https://paperswithcode.com/task/brain-tumor-segmentation)]

- Akshay Kumaar M. Brain Tumor Classification (using ResNet50 and Google Colab): [[GitHub](https://github.com/aksh-ai/brain_tumor_classification)]

- Joohyun Lee. BraTs (Brain Tumor Segmentation): [[GitHub](https://github.com/cv-lee/BraTs)]

- Ellis DG. **3DUnetCNN**: [[GitHub](https://github.com/ellisdg/3DUnetCNN)]
  - Includes BraTS tutorial and pretrained models
  - Pretrained models: [[zenodo](https://zenodo.org/record/4289225)]

#### Data Collections

- **TCGA-GBM**: The Cancer Genome Atlas Glioblastoma Multiforme Collection [[link](https://wiki.cancerimagingarchive.net/display/Public/TCGA-GBM)]

- **UCSF-PDGM**: University of California San Francisco Preoperative Diffuse Glioma MRI [[link](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=119705830)]
  - Calabrese E et al. The University of California San Francisco Preoperative Diffuse Glioma MRI Dataset. Radiology: Artificial Intelligence 2022;4(6):e220058. [[link](https://pubs.rsna.org/doi/10.1148/ryai.220058)]

- **The Cancer Imaging Archive (TCIA)**: [[cancerimagingarchive.net](https://www.cancerimagingarchive.net/)]

#### Tools for Medical Image Processing

- **DeepNeuro**: An open-source deep learning toolbox for neuroimaging [[GitHub](https://github.com/QTIM-Lab/DeepNeuro)]
  - Beers A et al. DeepNeuro: an open-source deep learning toolbox for neuroimaging. Neuroinformatics 2020. [[link](https://link.springer.com/article/10.1007/s12021-020-09477-5)]

- **MONAI**: Medical Open Network for Artificial Intelligence [[monai.io](https://monai.io/)]
  - Modern PyTorch-based framework for medical image analysis

- **nnU-Net**: Self-configuring Method for Deep Learning-based Biomedical Image Segmentation [[GitHub](https://github.com/MIC-DKFZ/nnUNet)]
  - State-of-the-art segmentation method often used in the BraTS challenge

#### Overview Article

- Lundervold AS, Lundervold A. **An overview of deep learning in medical imaging focusing on MRI.** Zeitschrift für Medizinische Physik 2019;29(2):102-127. [[link](https://www.sciencedirect.com/science/article/pii/S0939388918301181)]


David G. Ellis [BraTS 2020 Tutorial](https://github.com/ellisdg/3DUnetCNN/tree/master/examples/brats2020) with [3DUNetCNN](https://github.com/ellisdg/3DUnetCNN):

![Brain Tumor Segmentation (BraTS) Tutorial](https://github.com/ellisdg/3DUnetCNN/raw/master/legacy/doc/tumor_segmentation_illusatration.gif)

---

### Ethics in Artificial Intelligence and Machine Learning (Selected References)

- Wikipedia: Ethics of artificial intelligence [[link](https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence)]

- Rigby MJ. **Ethical Dimensions of Using Artificial Intelligence in Health Care.** AMA Journal of Ethics, Feb 2019. [[link](https://journalofethics.ama-assn.org/article/ethical-dimensions-using-artificial-intelligence-health-care/2019-02)]

- Morley J et al. **The ethics of AI in health care: A mapping review.** Social Science & Medicine 2020;260:113172. [[link](https://www.sciencedirect.com/science/article/pii/S0277953620303919)]

- Bostrom N, Yudkowsky E. The Ethics of Artificial Intelligence. In: Cambridge Handbook of Artificial Intelligence, CUP 2014. [[pdf](https://intelligence.org/files/EthicsofAI.pdf)]

- Ethics of Artificial Intelligence and Robotics. Stanford Encyclopedia of Philosophy. [[link](https://plato.stanford.edu/entries/ethics-ai)]

- Vollmer S et al. **Machine learning and artificial intelligence research for patient benefit: 20 critical questions on transparency, replicability, ethics, and effectiveness.** BMJ 2020;368:l6927. [[link](https://www.bmj.com/content/368/bmj.l6927)]

- Ethics of AI in Radiology. European and North American Multisociety Statement 2019. [[pdf](https://www.acr.org/-/media/ACR/Files/Informatics/Ethics-of-AI-in-Radiology-European-and-North-American-Multisociety-Statement--6-13-2019.pdf)]

#### EU AI Act and Regulation (2024)

- **EU AI Act**: The world's first comprehensive AI regulation, adopted in 2024. Relevant for medical AI classified as "high-risk".
  - EU AI Act overview: [[digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)]

---

### Data Management Plan (DMP)

For writing the data management plan, it is recommended to look at:

- **Science Europe**: Practical Guide to the International Alignment of Research Data Management [[link](https://scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/)]

- **FAIR Principles**: Findable, Accessible, Interoperable, Reusable [[go-fair.org](https://www.go-fair.org/fair-principles/)]

---

### Useful AI Tools for Writing the Research Plan

To work efficiently on writing the research plan, the following AI tools may be useful:

| Tool | Use Case | Link |
|------|----------|------|
| **ChatGPT** | General AI assistant, code explanations, literature search | [chat.openai.com](https://chat.openai.com) |
| **Claude** | Text analysis, academic writing | [claude.ai](https://claude.ai) |
| **Gemini** | Integrated in Google Colab for code help | [gemini.google.com](https://gemini.google.com) |
| **NotebookLM** | Document analysis and knowledge synthesis | [notebooklm.google.com](https://notebooklm.google.com) |
| **Cursor** | AI-assisted code development | [cursor.sh](https://cursor.sh) |
| **Elicit** | AI-powered literature search | [elicit.com](https://elicit.com) |
| **Connected Papers** | Visualization of literature networks | [connectedpapers.com](https://www.connectedpapers.com) |

---

## Checklist for the Team

Before you start, make sure everyone on the team has:

- [ ] Created an [Overleaf](https://www.overleaf.com) account (free)
- [ ] Access to the LaTeX template and understood the structure
- [ ] Read through at least one background article on glioblastoma
- [ ] Familiarized themselves with the WHO 2021 classification of CNS tumors
- [ ] Explored relevant data sources and software (to be able to describe them in the plan)
- [ ] Agreed on a communication channel for the team (e.g., Teams, Discord, Slack)
- [ ] Divided tasks and created a preliminary plan

---

_Updated: December 2025_

