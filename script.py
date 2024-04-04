# -*- coding: utf-8 -*-
from modeller import *

# Chemin vers le fichier de séquence protéique (au format FASTA)
sequence_file = "sequence.fasta"

# Chemin vers le fichier de modèle (au format PDB)
template_file = "template.pdb"

# Initialiser l'environnement Modeller
env = environ()
env.io.atom_files_directory = ['./', '/home/aymen/Bureau/modeller/modeller_10.5-1_amd64/usr/lib/modeller10.5/bin/mod11']

# Créer un objet pour le modèle
mdl = model(env, file=template_file)

# Créer un objet pour le template (séquence protéique connue)
aln = alignment(env)
mdl_sequence = alignment(env)
mdl_sequence.append_model(mdl, align_codes='model', atom_files=template_file)
aln.append(mdl_sequence)

# Charger la séquence protéique cible à prédire
target_sequence = sequence(env, file=sequence_file)

# Aligner la séquence cible sur le modèle
aln.append_sequence(target_sequence)

# Construire un modèle basé sur l'alignement
mdl1 = model(env, align_code='model', atom_files=template_file)
mdl2 = model(env, align_code='target', sequence=target_sequence)
aln.append_model(mdl1, align_codes='model', atom_files=template_file)
aln.append_model(mdl2, align_codes='target')

# Générer la structure 3D
mdl.clear_topology()
mdl.generate_topology(aln)
mdl.transfer_xyz(aln)
mdl.build(initialize_xyz=False, build_method='INTERNAL_COORDINATES')

# Écrire la structure 3D prédite dans un fichier au format PDB
mdl.write(file="predicted_structure.pdb")

