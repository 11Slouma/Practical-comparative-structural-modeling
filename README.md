## Introduction
Lase (AA) is a protein derived from Alteromonas haloplanktis, a marine bacterium known for its adaptability to diverse environmental conditions. In this study, we embark on a molecular modeling endeavor to elucidate the structural features of Lase (AA) from Alteromonas haloplanktis. By employing computational tools and techniques, we aim to unravel its molecular architecture . this pipeline built an important number of homology-models protein starting from a template to a model of our target . This modeling method is based on [the Basic Modeling tutorial of Modeller] , and the choice of the template is taken from the structure with the highest sequence identity to the target sequence.
## Installation
```
python : 3.8.10
modeller : 10.5
pymol : 2.3.0
```
## Database 
- Uniprot(https://www.uniprot.org/)
- Blast(https://blast.ncbi.nlm.nih.gov/Blast.cgi)
## Method 
- The first step is to set up my file with the 6 temlpate i've choosen which have the most identical percentage with my target sequence and placed them in the bin file of modeller directory where your workspace shoul look like this :
```
.
├── template1.pdb
├── template2.pdb
├── template3.pdb
├── template4.pdb
├── template5.pdb
├── template6.pdb
├── align2d.py
├── compare.py
├── evaluate_model.py
├── model_single.py
└── P29957.ali
```
