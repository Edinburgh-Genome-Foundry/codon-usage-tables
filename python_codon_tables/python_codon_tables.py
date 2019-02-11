import sys
import re
import os
from functools import lru_cache

if (sys.version_info[0] == 3):
    import urllib.request
    urlopen = urllib.request.urlopen
else:
    import urllib2
    urlopen = urllib2.urlopen

_this_dir = os.path.dirname(os.path.realpath(__file__))
_tables_dir = os.path.join(_this_dir, '..', "codon_usage_data", "tables")

available_codon_tables = [
    filename[:-4] for filename in os.listdir(_tables_dir)]

def csv_string_to_codons_dict(csv_string):
    """Transform a CSV string of a codon table to a dict."""
    result = {}
    for line in csv_string.split("\n")[1:]:
        aa, codon, freq = line.split(',')
        if aa not in result:
            result[aa] = {}
        result[aa][codon] = float(freq)
    return result

def get_codon_table(table_name):
    """Get data from one of this package's builtin codon usage tables."""
    with open(os.path.join(_tables_dir, table_name + '.csv'), 'r') as f:
        return csv_string_to_codons_dict(f.read())

def get_all_available_codon_tables():
    """Get all data from all of this package's builtin codon usage tables."""
    return {
        table_name: get_codon_table(table_name)
        for table_name in available_codon_tables
    }

@lru_cache(maxsize=128)
def download_codon_table(taxid=316407, target_file=None):
    """Get all data from all of this package's builtin codon usage tables."""
    _kazusa_url = ("http://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi"
                   "?aa=1&style=N&species=%s")
    _codon_regexpr = r"([ATGCU]{3}) ([A-Z]|\*) (\d.\d+)"
    url = _kazusa_url % taxid
    html_content = urlopen(url).read().decode().replace("\n", " ")
    csv_data = "\n".join(sorted([
        "%s,%s,%s" % (aa, codon, usage)
        for codon, aa, usage in re.findall(_codon_regexpr, html_content)
    ]))
    if target_file is not None:
        with open(target_file, "w+") as f:
            f.write("amino_acid,codon,relative_frequency\n")
            f.write(csv_data)
    else:
        return csv_string_to_codons_dict(csv_data)