## Introduction
Lase (AA) is a protein derived from Alteromonas haloplanktis, a marine bacterium known for its adaptability to diverse environmental conditions. In this study, we embark on a molecular modeling endeavor to elucidate the structural features of Lase (AA) from Alteromonas haloplanktis. By employing computational tools and techniques, we aim to unravel its molecular architecture . this pipeline built an important number of homology-models protein starting from a template to a model of our target . This modeling method is based on [the Basic Modeling tutorial of Modeller] , and the choice of the template is taken from the structure with the highest sequence identity to the target sequence.
## Installation
```
python : 3.13
modeller : 10.5
gnuplot : 6.0
pymol : 3.0.3
```
## Database 
- Uniprot(https://www.uniprot.org/)
- Blast(https://blast.ncbi.nlm.nih.gov/Blast.cgi)
- RCSB PDB(https://www.rcsb.org/)
## Method 
- The first step is to set up my file with the 6 temlpate i've chosen which have the most identical percentage with my target sequence(i have choosen them from others species to avoid falling into variants ) and placed them in the bin file of modeller directory where your workspace shoul look like this :
```
.
├── 1hx0.pdb
├── 1pif.pdb
├── 1ua3.pdb
├── 3blk.pdb
├── 3l2l.pdb
├── 8orp.pdb
├── align2d.py
├── compare.py
├── evaluate_model.py
├── model_single.py
└── P29957.ali
```
## Script 
- Start automated modelling using the `compare.py` to generate the `compare.log` file with the comparisons.
```
Weighted pair-group average clustering based on a distance matrix:


                                                               .--- 1hx0A @1.4     0.0000
                                                               |
                                                              .---- 1ua3A @2.0     1.0000
                                                              |
                                                             .----- 1pifA @2.3     1.5000
                                                             |
                                             .--------------------- 3l2lA @2.1    14.3750
                                             |
        .---------------------------------------------------------- 3blkA @2.0    44.5000
        |
      .------------------------------------------------------------ 8orpA @2.0

      +----+----+----+----+----+----+----+----+----+----+----+----+
    46.2800   38.2700   30.2600   22.2500   14.2400    6.2300   -1.7800
         42.2750   34.2650   26.2550   18.2450   10.2350    2.2250
```
- i did the process of alignement using the `align2d. py` file and choose the best template (based on the  better crystallography resolution)
- After establishing a target-template alignment, MODELLER automatically generates a 3D model of the target using its AutoModel class, streamlining the process without manual intervention.
Following script will generate five similar models based on the template and the alignment in the file it will generate models
Execute the `single_model. py`
```shell
26/05/2024  00:56           408 505 P29957.B99990001.pdb
26/05/2024  00:57           408 505 P29957.B99990002.pdb
26/05/2024  00:58           408 505 P29957.B99990003.pdb
26/05/2024  00:59           408 505 P29957.B99990004.pdb
26/05/2024  01:00           408 505 P29957.B99990005.pdb
```
- The most important output file is `single_model.log`, its help to choose one of the models based on the best DOPE score
```
>> Summary of successfully produced models:
Filename                          molpdf     DOPE score    GA341 score
----------------------------------------------------------------------
P29957.B99990001.pdb          6930.19385   -57792.11719        0.99877
P29957.B99990002.pdb          7038.89258   -56546.31250        0.91655
P29957.B99990003.pdb          7054.19873   -56667.73047        0.98017
P29957.B99990004.pdb          6878.17285   -56487.44531        0.92107
P29957.B99990005.pdb          7610.35645   -56625.14453        0.92490
```
##Model evaluation
-Now I evaluated my model with the `evaluate_model. py` and create a plot with GNUPLOT using the generated `MYtemplate1. profile` file 
Launch a new PyMol session and load the model, crystal, and template structures, then execute the following commands.
```shell
select reference, 1AQM and name CA
select P29957.B99990004 , P29957.B99990004 and name CA
align P29957.B99990004 , reference
```
the output is the calculation of  RMSD
```
RMSD =    0.598 (322 to 322 atoms)
```
the model may not be relible due to my lack oof experience in this field and the difficulty of interpreting the results , i also have choosed the template from another organism evoiding confortation with variants ,there may be a more suitable model that could produce a better results 
This model is a work on progress and can be improved with further research and work
```
