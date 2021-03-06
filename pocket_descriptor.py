#!/usr/bin/env python

import argparse
from binding_pocket import BindingPocketFeaturizer, check_residues

parser = argparse.ArgumentParser(description='BindingPocketFeaturizer')
parser.add_argument('--protein', '-p', type=str, required=True, help='Potein file')
parser.add_argument('--ligand', '-l', type=str, required=True, help='Ligand file')
parser.add_argument('--threshold', '-t', type=float, default=.3, help='Threshold')
args = parser.parse_args()

protein_fname = args.protein
ligand_fname = args.ligand
threshold = args.threshold

pocket_featurizer = BindingPocketFeaturizer()

print(' ' + '  '.join(pocket_featurizer.residues + ['other']))
check = check_residues(protein_fname, pocket_featurizer.residues)
print(' '.join('%4d' % count for count in check))

pocket_features, ligand_features, labels = pocket_featurizer.multi_featurize(protein_fname, ligand_fname, threshold=threshold)

print(pocket_features)
print(pocket_features.shape)
print(ligand_features.shape)
print(labels)
