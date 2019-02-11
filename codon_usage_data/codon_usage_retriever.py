#!/usr/bin/env python
"""Retrieve a Codon usage table from kazusa.or.jp, and store in a CSV file.

Usage:
------
To retrieve a codon table for one organism, given its TaxID, use:

> python codon_usage_retriever.py [TaxidNumber] [TargetFile.csv]

For instance:

> python codon_usage_retriever.py 316407 e_coli_codon_usage.csv

To retrieve codon tables from all organisms in ``organisms.csv`` at once, use:

> python codon_usage_retriever.py all



"""
import sys
import os
from python_codon_tables import download_codons_table

def download_all_tables():
    with open("organisms.csv", "r") as f:
        for line in f.readlines()[1:]:
            organism, taxid = line.strip("\n").split(",")
            print("Retrieving %s (taxid %s)" % (organism, taxid))
            target = os.path.join("tables", "%s_%s.csv" % (organism, taxid))
            download_codons_table(taxid=taxid, target_file=target)

if __name__ == "__main__":
    print (" ".join(sys.argv))
    if sys.argv[1] == "all":
        download_all_tables()
    else:
        download_codons_table(sys.argv[1], sys.argv[2])
