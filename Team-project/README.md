# Team Project &nbsp;&nbsp;&nbsp; <span style="font-size: 16px;">[ELMED219 / BMED365]</span>
## _Precision Medicine and Quantitative Imaging in Glioblastoma_

> **Note:** This is a joint project between ELMED219 and BMED365. The **project report should be written in English** (see the [LaTeX template](./latex-template/)).

---

## Team Organization

This year we have **14 applicants from BMED365** and **14 applicants from ELMED219**. We will establish **5 interdisciplinary teams**, each with a balanced mix of students from both programs:

| Team | BMED365 students | ELMED219 students | Total |
|------|------------------|-------------------|-------|
| Team 1 | 3 (b01, b02, b03) | 3 (e01, e02, e03)| 6 |
| Team 2 | 3 (b04, b05, b06) | 3 (e04, e05, e06)| 6 |
| Team 3 | 3 (b07, b08, b09) | 3 (e07, e08, e09)| 6 |
| Team 4 | 3 (b10, b11, b12)| 2 (e10, e11)| 5 |
| Team 5 | 2 (b13, b14) | 3 (e12, e13, e14)| 5 |

This interdisciplinary composition reflects real-world research teams where medical expertise meets computational and technical skills.

### Target Audience

- **ELMED219**: Medical students in their 2nd to 5th year of medical school
- **BMED365**: Master students in biomedicine, including specializations in bioinformatics, medical physics, molecular biology, medical technology, and related fields. Some students have recently completed their BSc.

The project is designed to accommodate this diversity of backgrounds while encouraging collaboration and mutual learning.

---



## Team Project Presentation

**Tuesday 27.01.2026, 08:15-10**  (20 min per team, all team members participate)

## Team Project Report Submission

**Deadline: Thursday 29.01.2026, 16:00**  - One member submits the team report (as a PDF file) to Mitt-UiB on behalf of the team

---

## Learning Objectives

Upon completion of this project, students should be able to:

- **Describe** relevant imaging technologies and modalities used in glioblastoma diagnosis and monitoring
- **Identify** appropriate machine learning approaches for medical image segmentation and classification tasks
- **Integrate** knowledge from different fields (imaging, computation, clinical medicine) into a coherent research proposal
- **Recognize** key ethical considerations in AI-based medical imaging, including patient privacy, data protection, and fairness
- **Outline** a basic data management plan following FAIR principles
- **Collaborate** effectively in an interdisciplinary team to produce a joint written document

---

## Project Motivation

### Why a Grant Proposal Rather Than Data Analysis?

This project asks you to write a research plan (grant proposal sketch) rather than perform actual data analysis. This design is pedagogically motivated:

1. **Conceptual understanding**: Writing a research plan requires you to demonstrate understanding of the field without getting lost in technical debugging or implementation details.

2. **Real-world practice**: Researchers spend considerable time crafting proposals before any data collection. This mirrors authentic academic practice.

3. **Integrative thinking**: You must bring together knowledge across imaging, machine learning, ethics, and clinical domains, which is the kind of integrative thinking essential for translational research.

4. **Collaborative writing**: Group collaboration on a written document is more manageable than coordinating code across different skill levels and computational environments.

5. **Leveling the playing field**: Students with different technical backgrounds can contribute meaningfully. Medical students bring clinical insight; biomedical/technical students bring methodological knowledge.

### Why Glioblastoma?

Glioblastoma (GBM) represents a good case study for precision medicine and quantitative imaging:

- **Well-characterized**: Extensive literature and established imaging protocols (the BraTS challenge provides excellent benchmarks)
- **Clinical importance**: Poor prognosis (median survival around 15 months) creates genuine need for improved diagnostic and therapeutic approaches
- **Molecular markers**: Key biomarkers (IDH mutation status, MGMT methylation) exemplify precision medicine approaches
- **Multimodal imaging**: Standard clinical protocols include multiple MRI sequences (T1, T1+Gd, T2, FLAIR), with emerging roles for advanced techniques
- **Active research community**: Annual challenges, open datasets, and reproducible methods facilitate learning

---

## Project Description

Imagine that you are part of a group of established, successful researchers who will collaborate on an important biomedical and medical challenge. An open call for research projects has been announced under a new umbrella program titled **"Artificial Intelligence and Computational (Bio)medicine"**. Your interdisciplinary group is aiming for a project on **"Precision Medicine and Quantitative Imaging in Glioblastoma: A Multiscale Approach"**.

> **Important:** The task is to **write a research plan** (a grant proposal sketch) for a hypothetical project, **not** to actually conduct the project with data analysis or coding. You should describe *what* you would do, *how* and *why*, but not perform the actual analysis.

### Focus Areas

1. **Imaging technologies and modalities**: possibly at different scales (macro: MRI/PET; micro: histopathology; molecular: genomics/proteomics)
2. **Image-derived biomarkers** for glioblastoma diagnosis, prognosis, and treatment response
3. **Machine learning techniques** for segmentation, classification, and prediction
4. **Graph theory and patient similarity networks** for discovering patient subgroups and supporting precision medicine approaches *(optional alternative or complementary approach)*
5. **Relevance and potential impact** of your proposed approach
6. **Ethics and data management**: including privacy considerations, GDPR awareness, and data sharing plans

---

## Report Organization

### Research Plan
**(3 to 5 pages including figures and reference list)**

| Section | Content | Questions to Consider |
|---------|---------|----------------------|
| **Background** | Brief introduction to the field | What is the clinical problem? What are current approaches? |
| **Objectives** | Aims and expected outcomes | What do you want to achieve? Why is it relevant? |
| **Materials** | Data sources, patient cohorts | Which datasets would you use? What kind of images? |
| **Methods** | Imaging analysis, ML approaches | How would you process images? Which methods would you apply? |
| **Evaluation** | How to assess results | How would you know if your approach works? |

#### Guidance on Methods and Evaluation

Your methods section should describe (at a conceptual level):

- **Preprocessing**: What needs to happen to images before analysis? (e.g., registration to a common space, intensity normalization). You do not need to specify exact software commands, but should understand why preprocessing matters.

- **Segmentation or classification approach**: What type of method would you use? (e.g., a convolutional neural network like U-Net for segmentation, or a classifier for predicting tumor type). Describe the general approach and why it is suitable for the task.

- **Training and validation**: Where would training data come from? How would you check that the model works on new data it has not seen before? (e.g., splitting data into training and test sets, or using data from different hospitals).

- **Performance metrics**: How would you measure success? For segmentation, metrics like Dice score measure overlap between predicted and true tumor regions. For classification, accuracy or area under the ROC curve (AUROC) are common.

> **Note for students**: You are not expected to implement these methods or know all technical details. The goal is to show that you understand the general workflow and can describe it clearly. Use the literature and resources provided to learn about common approaches.

### Data Management Plan and Ethical Considerations
**(1.5 to 2.5 pages including graphics or links)**

| Section | Content |
|---------|---------|
| **Data description** | Types of data you would use, formats, approximate volume |
| **Data and code sharing** | Where would you store and share data/code? |
| **FAIR principles** | How would you make data Findable, Accessible, Interoperable, Reusable? |
| **Ethical considerations** | Patient consent, privacy protection, potential biases |

#### Key Ethical Considerations for AI in Medical Imaging

Your ethics section should address:

- **Patient consent and privacy**: How is patient data protected? What does anonymization mean?
- **Data protection regulations**: Awareness of GDPR and its implications for medical data
- **Fairness and bias**: Could the AI system work differently for different patient groups? Why might this happen?
- **Transparency**: Can clinicians understand and trust the AI system's outputs?

> **Note**: You do not need to be a legal expert. The goal is to demonstrate awareness of these issues and show that you have thought about them in the context of your proposed project.

---

## Assessment Criteria

| Component | Weight | What We Look For |
|-----------|--------|------------------|
| **Background and Objectives** | 20% | Clear description of the problem, well-defined aims, understanding of clinical relevance |
| **Materials and Methods** | 30% | Appropriate choice of data and methods, logical workflow, demonstration of understanding |
| **Relevance and Impact** | 20% | Why this project matters, potential benefits, realistic scope |
| **Ethics and Data Management** | 20% | Awareness of privacy and ethical issues, basic data management plan, FAIR principles |
| **Writing Quality** | 10% | Clear structure, appropriate use of references, readable figures, good language |

> **Note**: We do not expect you to propose something completely novel or to have deep technical expertise. We are looking for evidence that you understand the field, can describe a reasonable approach, and have thought carefully about the ethical dimensions.

---

## Preparation Guide

### Familiarize yourself with LaTeX and the report template

We use the online, collaborative LaTeX editor [Overleaf](https://www.overleaf.com) for writing the report.

**LaTeX resources:**
- [What is LaTeX?](https://en.wikipedia.org/wiki/LaTeX)
- [Why use LaTeX for scientific writing?](https://mildopinions.wordpress.com/2008/07/07/why-i-use-latex-in-biology)
- [LaTeX best practices](https://www.tug.org/pracjourn/2007-4/senthil/senthil.pdf)
- [Academic journal templates](https://www.overleaf.com/latex/templates/tagged/academic-journal)

**Project template:**
- LaTeX source: [[BMED365_2026_project_team_k.tex](./latex-template/BMED365_2026_project_team_k.tex)]
- Example figure: [[bmed365_dummy_fig.png](./latex-template/bmed365_dummy_fig.png)]
- Compiled PDF: [[BMED365_2026_project_team_k.pdf](./latex-template/BMED365_2026_project_team_k.pdf)]

**Example of expected detail level:**
- Seili Summer School 2019 project report (Prostate Cancer theme):
  - Overleaf project: [[view](https://www.overleaf.com/read/xwjxwcnpzhqv)]
  - Source files: [[main.tex](./latex-template/Seili_2020_example/main.tex)], [[Fig1](./latex-template/Seili_2020_example/Fig1_The_process_of_autoEncoder.png)], [[Fig2](./latex-template/Seili_2020_example/Fig2_Overview_of_the_process.png)]
  - Compiled PDF: [[Seili_2020_project_template.pdf](./latex-template/Seili_2020_example/Seili_2020_project_template.pdf)]

---

## Information Sources

### Background Knowledge

#### Brain Biology and Pathology
- Coursera: [Medical Neuroscience](https://www.coursera.org/learn/neurobiology), especially the lecture on [brain tumors](https://www.coursera.org/lecture/neurobiology/brain-tumors-fUcn4)
- The Human Protein Atlas: [Brain Atlas](https://www.proteinatlas.org/humanproteome/brain)

#### WHO Classification of CNS Tumors

> **Important:** The WHO 2021 classification introduces significant changes. The diagnosis "Glioblastoma, IDH-wildtype" now *requires* molecular analysis to confirm IDH wild-type status.

- Louis DN et al. **The 2021 WHO Classification of Tumors of the Central Nervous System: a summary.** Neuro-Oncology 2021;23(8):1231-1251. [[link](https://academic.oup.com/neuro-oncology/article/23/8/1231/6311214)]

- Louis DN et al. The 2016 World Health Organization Classification of Tumors of the Central Nervous System: A Summary. Acta Neuropathol 2016;131(6):803-820. [[link](https://link.springer.com/article/10.1007/s00401-016-1545-1)]

- Aldape K et al. Challenges to curing primary brain tumors. Nat Rev Clin Oncol 2019;16:509-520. [[link](https://www.nature.com/articles/s41571-019-0177-5)]

---

### Brain Tumors and Neuroimaging

#### Review Articles

- Abd-Ellah MK et al. A review on brain tumor diagnosis from MRI images: Practical implications, key achievements, and lessons learned. Magnetic Resonance Imaging 2019;61:300-318. [[link](https://www.sciencedirect.com/science/article/pii/S0730725X18304302)]

- Stable O et al. Brain tumor segmentation and classification from magnetic resonance images: Review of selected methods from 2014 to 2019. Pattern Recognition Letters 2020;131:244-260. [[link](https://www.sciencedirect.com/science/article/pii/S016786551930340X)]

- Nadeem MW et al. Brain Tumor Analysis Empowered with Deep Learning: A Review, Taxonomy, and Future Challenges. Brain Sci 2020;10(2):118. [[link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7071415)]

- Lohmann P et al. PET/MRI Radiomics in Patients With Brain Metastases. Front. Neurol. 2020. [[link](https://www.frontiersin.org/articles/10.3389/fneur.2020.00001/full)]

#### BraTS Challenge (Brain Tumor Segmentation)

The **BraTS Challenge** is an annual international competition focusing on brain tumor segmentation from MRI. Since 2023, it is organized via the Synapse platform and has expanded to include multiple sub-challenges.

- **BraTS 2024 Challenge**: [[synapse.org/brats](https://www.synapse.org/brats)]
  - Sub-challenges include: Adult Glioma (GLI), Post-treatment Glioma, Meningioma (MEN), Brain Metastases (MET), Pediatric Tumors (PED), Sub-Saharan Africa (SSA)

- Menze BH et al. The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS). IEEE Trans Med Imaging 2015;34(10):1993-2024. [[link](https://ieeexplore.ieee.org/document/6975210)]

- Bakas S et al. Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features. Scientific Data 2017;4:170117. [[link](https://www.nature.com/articles/sdata2017117)]

- Correia de Verdier M et al. **The 2024 Brain Tumor Segmentation (BraTS) Challenge: Glioma Segmentation on Post-treatment MRI.** arXiv 2024. [[link](https://arxiv.org/abs/2405.18368)]
  - *The 2024 challenge introduced post-treatment glioma segmentation, including the resection cavity as a new region.*

---

### Artificial Intelligence in Neuro-Oncology

#### Foundational Articles

- Lundervold AS, Lundervold A. **An overview of deep learning in medical imaging focusing on MRI.** Zeitschrift für Medizinische Physik 2019;29(2):102-127. [[link](https://www.sciencedirect.com/science/article/pii/S0939388918301181)]

- Rudie JD et al. **Emerging Applications of Artificial Intelligence in Neuro-Oncology.** Radiology 2019;290(3):607-618. [[link](https://pubs.rsna.org/doi/10.1148/radiol.2019181928)]

#### Clinical Applications

- Hollon TC et al. Near Real-Time Intraoperative Brain Tumor Diagnosis Using Stimulated Raman Histology and Deep Neural Networks. Nature Medicine 2020;26(1):52-58. [[link](https://www.nature.com/articles/s41591-019-0715-9)] [[GitHub](https://github.com/toddhollon/srh_cnn)]

- Yogananda CGB et al. A novel fully automated MRI-based deep-learning method for classification of IDH mutation status in brain gliomas. Neuro-Oncology 2020;22(3):402-411. [[link](https://academic.oup.com/neuro-oncology/article/22/3/402/5584591)]

- Kickingereder P et al. Automated quantitative tumour response assessment of MRI in neuro-oncology with artificial neural networks. The Lancet Oncology 2019;20(5):728-740. [[link](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30098-1/fulltext)]

#### Recent Advances (2022-2025)

- Pati S et al. **Federated learning enables big data for rare cancer boundary detection.** Nature Communications 2022;13:7346. [[link](https://www.nature.com/articles/s41467-022-33407-5)]
  - *Describes the FeTS (Federated Tumor Segmentation) initiative enabling multi-institutional collaboration without sharing sensitive patient data.*

- Kofler F et al. **BraTS Toolkit: Translating BraTS Brain Tumor Segmentation Algorithms Into Clinical and Scientific Practice.** Frontiers in Neuroscience 2020;14:125. [[link](https://www.frontiersin.org/articles/10.3389/fnins.2020.00125)]

- Ghadimi N et al. **Deep Learning-Based Techniques in Glioma Brain Tumor Segmentation Using Multi-Parametric MRI: A Review on Clinical Applications and Future Outlooks.** Journal of Magnetic Resonance Imaging 2025;61(1):52-69. [[link](https://onlinelibrary.wiley.com/doi/10.1002/jmri.29543)]
  - *Comprehensive 2025 review covering CNN architectures, attention mechanisms, and transformer models for glioma segmentation.*

- Booth TC et al. **A review of deep learning for brain tumor analysis in MRI.** npj Precision Oncology 2025;9:2. [[link](https://www.nature.com/articles/s41698-024-00789-2)]
  - *Recent review exploring deep learning applications in tumor segmentation, classification, and survival prediction.*

- Karniadakis D et al. **A Review on Deep Learning Methods for Glioma Segmentation, Limitations, and Future Perspectives.** Cancers 2025. [[link](https://pmc.ncbi.nlm.nih.gov/articles/PMC12387613/)]
  - *Evaluates over 80 state-of-the-art models, comparing CNN-based, Transformer, and hybrid architectures.*

- Kim S et al. **Deep learning-driven brain tumor classification and segmentation using non-contrast MRI.** Scientific Reports 2025;15:26799. [[link](https://www.nature.com/articles/s41598-025-13591-2)]
  - *Demonstrates high accuracy tumor classification and segmentation using non-contrast T1w and T2w MRI.*

- Kabir T et al. **A Bayesian deep segmentation framework for glioblastoma tumor segmentation using follow-up MRIs.** Frontiers in Neuroimaging 2025. [[link](https://www.frontiersin.org/journals/neuroimaging/articles/10.3389/fnimg.2025.1630245/full)]
  - *Introduces uncertainty estimation in deep learning for more reliable clinical segmentation.*

- White NS et al. **Deep Learning Segmentation of Infiltrative and Enhancing Cellular Tumor at Pre- and Posttreatment Multishell Diffusion MRI of Glioblastoma.** Radiology 2024;312(3):e240424. [[link](https://pubmed.ncbi.nlm.nih.gov/39166970/)]
  - *Demonstrates deep learning for segmenting cellular tumor from advanced diffusion MRI, predicting survival.*

---

### Foundation Models for Medical Imaging

A new development in medical image analysis involves **foundation models**: large models pretrained on diverse datasets that can be adapted to specific tasks. These are worth knowing about, though detailed understanding is not required.

#### Segment Anything Model (SAM) and Medical Adaptations

- Ma J et al. **Segment Anything in Medical Images.** Nature Communications 2024;15:654. [[link](https://www.nature.com/articles/s41467-024-44824-z)] [[GitHub](https://github.com/bowang-lab/MedSAM)]
  - MedSAM: Fine-tuned on 1.5M+ medical image-mask pairs across 10 modalities
  - Achieves strong performance on glioma segmentation tasks

- Nguyen et al. **Necessity and impact of specialization of large foundation model for medical segmentation tasks.** Medical Physics 2025. [[link](https://aapm.onlinelibrary.wiley.com/doi/full/10.1002/mp.17470)]
  - *Shows that foundation models often need task-specific fine-tuning for best clinical performance.*

> **For your research plan:** You can mention foundation models as an emerging approach, but traditional methods like U-Net or nnU-Net are equally valid choices. Focus on describing your chosen approach clearly rather than using the most advanced method.

---

### Graph Theory and Patient Similarity Networks

> **Note:** This is an *optional alternative or complementary* approach to deep learning methods. Teams may choose to incorporate network-based analysis alongside or instead of traditional ML approaches.

#### Concept and Motivation

Patient Similarity Networks (PSN) represent patients as nodes in a graph, with edges connecting patients who are similar based on clinical, imaging, or molecular features. This approach enables:
- **Patient stratification**: Discovering natural subgroups (e.g., glioblastoma subtypes with different prognosis)
- **Precision medicine**: Identifying similar patients to inform treatment decisions
- **Multimodal integration**: Combining imaging features, molecular markers, and clinical variables in a unified framework

#### Foundational Articles

- Pai S, Bader GD. **Patient Similarity Networks for Precision Medicine.** Journal of Molecular Biology 2018;430(18):2924-2938. [[link](https://www.sciencedirect.com/science/article/pii/S0022283618308489)]
  - *Comprehensive review of PSN methods, similarity metrics, and applications in precision medicine.*

- Ruan P et al. **Using Association Signal Annotations to Boost Similarity Network Fusion.** Bioinformatics 2019;35(19):3718-3726. [[link](https://academic.oup.com/bioinformatics/article/35/19/3718/5368011)]

- Wang B et al. **Similarity network fusion for aggregating data types on a genomic scale.** Nature Methods 2014;11:333-337. [[link](https://www.nature.com/articles/nmeth.2810)]
  - *Foundational method for combining multiple data types using patient similarity networks.*

#### Applications in Neuro-Oncology and Clinical Research

- Lundervold A et al. **Brain Structure, Cognition, and Fatigue in IBS Assessed Through a Patient Similarity Network.** Diagnostics 2025;15(4):470. [[link](https://doi.org/10.3390/diagnostics15040470)]
  - *Example of PSN methodology applied to neuroimaging and cognitive data.*

- Research groups have applied PSN to:
  - Stratifying glioma patients based on radiomic features
  - Identifying molecular subtypes from multimodal data
  - Predicting treatment response in brain tumor cohorts

#### Course Resources

See [Lab 1: Network Science and Patient Similarity Networks](../Lab1-NetworkSci-PSN/) for practical examples including:
- Introduction to graph theory and network science
- Building PSN from clinical data
- Community detection for patient stratification

> **For your research plan:** You can propose a PSN-based approach for patient stratification, either as the main method or as a complementary analysis to deep learning segmentation. Consider how network-based analysis could help identify glioblastoma subtypes or predict outcomes based on multimodal patient similarity.

---

### Software and Tools

Even though you will not run code yourself, it is useful to know which tools exist so you can describe realistic methods in your research plan.

#### Deep Learning Frameworks for Medical Imaging

| Tool | Description | Link |
|------|-------------|------|
| **nnU-Net** | Self-configuring segmentation method; frequently wins BraTS challenges | [[GitHub](https://github.com/MIC-DKFZ/nnUNet)] |
| **MONAI** | PyTorch-based framework for medical image analysis | [[monai.io](https://monai.io/)] |
| **MedSAM** | Foundation model for medical image segmentation | [[GitHub](https://github.com/bowang-lab/MedSAM)] |
| **3DUnetCNN** | 3D U-Net implementation with BraTS tutorial | [[GitHub](https://github.com/ellisdg/3DUnetCNN)] |
| **DeepNeuro** | Open-source deep learning toolbox for neuroimaging | [[GitHub](https://github.com/QTIM-Lab/DeepNeuro)] |
| **NetworkX** | Python library for network/graph analysis and patient similarity networks | [[networkx.org](https://networkx.org/)] |
| **SNFtool** | R package for Similarity Network Fusion | [[CRAN](https://cran.r-project.org/package=SNFtool)] |

#### Community Resources

- **Papers With Code**: Brain Tumor Segmentation [[paperswithcode.com](https://paperswithcode.com/task/brain-tumor-segmentation)]
- **BraTS Toolkit**: Tools for applying BraTS algorithms [[GitHub](https://github.com/neuronflow/BraTS-Toolkit)]

#### Pretrained Models

- 3DUnetCNN pretrained models for BraTS: [[Zenodo](https://zenodo.org/record/4289225)]

![Brain Tumor Segmentation Illustration](https://github.com/ellisdg/3DUnetCNN/raw/master/legacy/doc/tumor_segmentation_illusatration.gif)
*Brain tumor segmentation example from the 3DUnetCNN BraTS tutorial*

---

### Data Collections

| Dataset | Description | Link |
|---------|-------------|------|
| **BraTS Challenge Data** | Multimodal MRI with expert segmentations | [[synapse.org/brats](https://www.synapse.org/brats)] |
| **TCGA-GBM** | The Cancer Genome Atlas Glioblastoma collection | [[TCIA](https://wiki.cancerimagingarchive.net/display/Public/TCGA-GBM)] |
| **UCSF-PDGM** | Preoperative Diffuse Glioma MRI (500 patients) | [[TCIA](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=119705830)] |
| **The Cancer Imaging Archive** | General repository for cancer imaging data | [[cancerimagingarchive.net](https://www.cancerimagingarchive.net/)] |

**Reference for UCSF-PDGM:**
- Calabrese E et al. The University of California San Francisco Preoperative Diffuse Glioma MRI Dataset. Radiology: Artificial Intelligence 2022;4(6):e220058. [[link](https://pubs.rsna.org/doi/10.1148/ryai.220058)]

---

### Ethics in AI and Healthcare

#### General Resources

- Morley J et al. **The ethics of AI in health care: A mapping review.** Social Science & Medicine 2020;260:113172. [[link](https://www.sciencedirect.com/science/article/pii/S0277953620303919)]

- Vollmer S et al. **Machine learning and artificial intelligence research for patient benefit: 20 critical questions on transparency, replicability, ethics, and effectiveness.** BMJ 2020;368:l6927. [[link](https://www.bmj.com/content/368/bmj.l6927)]

- Rigby MJ. **Ethical Dimensions of Using Artificial Intelligence in Health Care.** AMA Journal of Ethics 2019. [[link](https://journalofethics.ama-assn.org/article/ethical-dimensions-using-artificial-intelligence-health-care/2019-02)]

- Stanford Encyclopedia of Philosophy: **Ethics of Artificial Intelligence and Robotics** [[link](https://plato.stanford.edu/entries/ethics-ai)]

#### Fairness and Bias in Medical AI

- Gichoya JW et al. **AI recognition of patient race in medical imaging: a modelling study.** Lancet Digital Health 2022;4(6):e406-e414. [[link](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(22)00063-2/fulltext)]
  - *Demonstrates that AI models can encode demographic information from medical images, raising fairness considerations.*

- Chen RJ et al. **Algorithm fairness in artificial intelligence for medicine and healthcare.** Nature Biomedical Engineering 2023;7:719-742. [[link](https://pmc.ncbi.nlm.nih.gov/articles/PMC10632090/)]
  - *Reviews fairness issues and mitigation strategies in healthcare AI.*

- Park SH et al. **Fairness of artificial intelligence in healthcare: review and recommendations.** Japanese Journal of Radiology 2024;42:3-15. [[link](https://pmc.ncbi.nlm.nih.gov/articles/PMC10764412/)]
  - *Introduces the FAIR (Fairness of AI Recommendations) statement for best practices.*

- Defined N et al. **Bias in artificial intelligence for medical imaging: fundamentals, detection, avoidance, mitigation, challenges, ethics, and prospects.** Diagnostic and Interventional Radiology 2025;31(2):101-117. [[link](https://pmc.ncbi.nlm.nih.gov/articles/PMC11880872/)]
  - *Comprehensive 2025 review covering bias detection, mitigation strategies, and ethical principles.*

- Ali S et al. **Ethical framework for responsible foundational models in medical imaging.** Frontiers in Radiology 2025. [[link](https://pmc.ncbi.nlm.nih.gov/articles/PMC12128638/)]
  - *Proposes ethical framework integrating privacy, fairness, and explainability for AI in medical imaging.*

#### Regulatory Framework

- **EU AI Act** (2024): The world's first comprehensive AI regulation. Medical AI is typically classified as "high-risk."
  - EU AI Act overview: [[digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)]

- **Ethics of AI in Radiology**: European and North American Multisociety Statement 2019 [[pdf](https://www.acr.org/-/media/ACR/Files/Informatics/Ethics-of-AI-in-Radiology-European-and-North-American-Multisociety-Statement--6-13-2019.pdf)]

---

### Data Management Planning

#### FAIR Principles

Your data management plan should address how your project would ensure data and code are:
- **F**indable: persistent identifiers, descriptive metadata
- **A**ccessible: clear access protocols, documentation
- **I**nteroperable: standard formats (NIfTI, DICOM), common terminology
- **R**eusable: clear licenses, provenance documentation

**Resources:**
- FAIR Principles: [[go-fair.org](https://www.go-fair.org/fair-principles/)]
- Science Europe: Practical Guide to Research Data Management [[link](https://scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/)]

#### Suggested Repositories

| Type | Repository | Use Case |
|------|------------|----------|
| Code | GitHub/GitLab | Version control, collaboration |
| Models | Zenodo, Hugging Face | Trained model weights with DOI |
| Data | TCIA, Synapse | Medical imaging data sharing |
| Preprints | arXiv, medRxiv | Rapid dissemination |

---

### AI Tools for Writing

These tools may help with literature search, writing, and understanding complex concepts:

| Tool | Use Case | Link |
|------|----------|------|
| **Claude** | Text analysis, academic writing, explaining concepts | [claude.ai](https://claude.ai) |
| **ChatGPT** | General AI assistant, brainstorming | [chat.openai.com](https://chat.openai.com) |
| **NotebookLM** | Document analysis and synthesis | [notebooklm.google.com](https://notebooklm.google.com) |
| **Elicit** | AI-powered literature search | [elicit.com](https://elicit.com) |
| **Connected Papers** | Visualization of citation networks | [connectedpapers.com](https://www.connectedpapers.com) |
| **Semantic Scholar** | Academic search with AI features | [semanticscholar.org](https://www.semanticscholar.org) |

> **Note:** Always verify AI-generated content against primary sources. Use these tools to help your work, not to replace critical thinking.

---

## Team Checklist

Before you start, make sure everyone on the team has completed these tasks:

### Individual Preparation
- [ ] Created a free [Overleaf](https://www.overleaf.com) account (preferably using your Mitt-UiB Innloggings-ID)
- [ ] Accessed the LaTeX template and understood its structure
- [ ] Read at least one background article on glioblastoma and its imaging
- [ ] Familiarized themselves with the WHO 2021 classification of CNS tumors
- [ ] Explored relevant datasets (BraTS, TCGA-GBM) to understand available data
- [ ] Looked at at least one software tool or framework (nnU-Net, MONAI, MedSAM)

### Team Organization
- [ ] Established a communication channel ([Discord](https://support.discord.com) channel _Team k_ - using your Mitt-UiB Innloggings-ID as user name)
- [ ] Assigned roles and responsibilities for different sections
- [ ] Created a shared Overleaf project from the template
- [ ] Set up a timeline with milestones and internal deadlines
- [ ] Agreed on how to manage references (BibTeX file)

### Before Submission
- [ ] All team members have reviewed the complete document
- [ ] References are complete and properly formatted
- [ ] Figures are clear and properly captioned
- [ ] Document compiles without errors
- [ ] Page limits are respected (3 to 5 pages research plan + 1.5 to 2.5 pages DMP/ethics)

### Submission Deadline
- [ ] Thursday 29.01.2026, 16:00 - One member submits the team report (as a PDF file) to Mitt-UiB on behalf of the team

---

## Frequently Asked Questions

**Q: Do we need to write code or analyze data?**

A: No. This is a research plan describing what you *would* do. Focus on methodology and reasoning, not implementation.

**Q: How technical should the methods section be?**

A: Technical enough to show you understand the general approaches, but accessible to your teammates with different backgrounds. Explain *why* you choose specific methods, not just *what* they are.

**Q: I am a medical student with limited technical background. How can I contribute?**

A: Your clinical knowledge is essential. You can contribute to the background section (clinical relevance, patient perspective), help ensure the proposed approach makes clinical sense, and lead the ethics discussion. The interdisciplinary nature of the teams means everyone has something valuable to offer.

**Q: I am a BMED365 student who just finished my BSc. Is this project too advanced?**

A: The project is designed to be accessible. You are not expected to have prior expertise in brain tumor imaging or deep learning. Use the provided resources to learn, and remember that describing methods clearly is more important than proposing the most advanced approach.

**Q: Can we propose using methods we have not learned in class?**

A: Yes, as long as you can explain them adequately and justify why they are appropriate. The literature review is part of the learning process.

**Q: How many references should we include?**

A: Quality over quantity. Typically 15 to 25 well-chosen references demonstrate good scholarship without padding.

**Q: Should we focus on one specific aspect or cover everything broadly?**

A: Find a balance. You need breadth to show understanding of the overall workflow, but you can go deeper on one or two aspects that interest your team.

**Q: Can we use graph theory and patient similarity networks instead of deep learning?**

A: Yes. You may propose a PSN-based approach for patient stratification, or combine network analysis with imaging methods. For example, you could extract radiomic features from segmented tumors, then use PSN to identify patient subgroups with different prognoses. See [Lab 1](../Lab1-NetworkSci-PSN/) for practical examples and background material.

**Q: How do we divide work in an interdisciplinary team?**

A: Consider dividing by expertise: medical students might lead on clinical background and ethics, while technical students lead on methods. However, everyone should contribute to all sections. The final product should be coherent, not a collection of separate parts.

---

## Contact and Support

- Course repository: [https://github.com/arvidl/BMED365-2026](https://github.com/arvidl/BMED365-2026)
- For technical questions about LaTeX/Overleaf, consult the [Overleaf documentation](https://www.overleaf.com/learn)
- For questions about the project, contact the course instructors

---

_Last updated: January 2026_

---

<details>
<summary><b>Version History</b></summary>

| Date | Changes |
|------|---------|
| January 2026 | Added graph theory and patient similarity networks (PSN) as optional methodological approach; added new PSN section with foundational articles and course resources; updated software tools with NetworkX and SNFtool; added FAQ entry for PSN-based approaches |
| January 2026 | Added team organization for 28 students in 5 teams; updated references to include 2025 publications; adjusted learning objectives and assessment criteria for mixed student audience; expanded guidance for students with different backgrounds; removed M-dashes |
| December 2024 | Initial version |

</details>
