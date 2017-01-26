#!/usr/bin/env python
"""Retrieve a Codon usage table from kazusa.or.jp, and store in a CSV file.

Usage:
> python retrieve_cdu.py all
> python retrieve_cdu.py [TaxidNumber] [TargetFile.csv]
"""

import sys
import re
import os

if (sys.version_info[0] == 3):
    import urllib.request
    urlopen = urllib.request.urlopen
else:
    import urllib2
    urlopen = urllib2.urlopen

kazusa_url = ("http://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi"
              "?aa=1&style=N&species=%s")
codon_regexpr = r"([ATGCU]{3}) ([A-Z]|\*) (\d.\d+)"

def create_codon_table(taxid=316407, target_file="codon_usage.csv"):
    html_content = urlopen(kazusa_url % taxid).read().replace("\n", " ")
    data = "\n".join(sorted([
        "%s;%s;%s" % (aa, codon, usage)
        for codon, aa, usage in re.findall(codon_regexpr, html_content)
    ]))
    with open(target_file, "w+") as f:
        f.write("amino_acid;codon;relative_frequency\n")
        f.write(data)


def get_all_tables():
    with open("organisms.csv", "r") as f:
        for line in f.readlines()[1:]:
            organism, taxid = line.strip("\n").split(";")
            print("Retrieving %s (taxid %s)" % (organism, taxid))
            target = os.path.join("tables", "%s_%s.csv" % (organism, taxid))
            create_codon_table(taxid=taxid, target_file=target)

if __name__ == "__main__":
    print (" ".join(sys.argv))
    if sys.argv[1] == "all":
        get_all_tables()
    else:
        create_codon_table(sys.argv[1], sys.argv[2])
