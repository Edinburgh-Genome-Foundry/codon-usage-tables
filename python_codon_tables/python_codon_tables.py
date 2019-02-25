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

available_codon_tables_names = [
    filename[:-4] for filename in os.listdir(_tables_dir)]

available_codon_tables_shortnames = {
    "_".join(table_name.split('_')[:-1]): table_name
    for table_name in available_codon_tables_names
}

def csv_string_to_codons_dict(csv_string):
    """Transform a CSV string of a codon table to a dict."""
    result = {}
    for line in csv_string.split("\n")[1:]:
        aa, codon, freq = line.split(',')
        if aa not in result:
            result[aa] = {}
        result[aa][codon] = float(freq)
    return result

@lru_cache(maxsize=128)
def get_codons_table(table_name):
    """Get data from one of this package's builtin codon usage tables.
    
    Returns a dict {"*": {'UAA': 0.64...}, 'K': {'AAA': 0.76...}, ...}
    
    The table_name argument very flexible on purpose, it can be either an
    integer representing a taxonomic ID (which will be downloaded from
    the kazusa database), or a string "12245" representing a TaxID, or a string
    "e_coli_316407" referring to a builtin table of python_codon_optimization,
    or a short form "e_coli" which will be automatically extended to
    "e_coli_316407" (at your own risks).
    """
    if isinstance(table_name, int) or str.isdigit(table_name):
        return download_codons_table(taxid=table_name)
    if table_name in available_codon_tables_shortnames:
        table_name = available_codon_tables_shortnames[table_name]
    with open(os.path.join(_tables_dir, table_name + '.csv'), 'r') as f:
        return csv_string_to_codons_dict(f.read())

def get_all_available_codons_tables():
    """Get all data from all of this package's builtin codon usage tables."""
    return {
        table_name: get_codons_table(table_name)
        for table_name in available_codon_tables_names
    }

@lru_cache(maxsize=128)
def download_codons_table(taxid=316407, target_file=None):
    """Get all data from all of this package's builtin codon usage tables."""
    _kazusa_url = ("http://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi"
                   "?aa=1&style=N&species=%s")
    _codon_regexpr = r"([ATGCU]{3}) ([A-Z]|\*) (\d.\d+)"
    url = _kazusa_url % taxid
    html_content = urlopen(url).read().decode().replace("\n", " ")
    csv_data = "\n".join(["amino_acid,codon,relative_frequency"] + sorted([
        "%s,%s,%s" % (aa, codon, usage)
        for codon, aa, usage in re.findall(_codon_regexpr, html_content)
    ]))
    if target_file is not None:
        with open(target_file, "w+") as f:
            f.write(csv_data)
    else:
        return csv_string_to_codons_dict(csv_data)