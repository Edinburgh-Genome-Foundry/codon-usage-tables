"""Basic tests to check that the main examples work."""

import os
import python_codon_tables as pct

def test_basics():

    # LOAD ONE TABLE BY NAME
    table = pct.get_codon_table("b_subtilis_1423")
    assert table['T']['ACA'] == 0.4
    assert table['*']['UAA'] == 0.61

    # LOAD ALL TABLES AT ONCE
    codon_tables = pct.get_all_available_codon_tables()
    assert codon_tables['c_elegans_6239']['L']['CUA'] == 0.09

def test_download_codon_table(tmpdir):
    table = pct.download_codon_table(taxid=316407)
    assert table['*']['UAG'] == 0.07
    target = os.path.join(str(tmpdir), 'test.csv')
    table = pct.download_codon_table(taxid=316407, target_file=target)