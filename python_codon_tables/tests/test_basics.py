"""Basic tests to check that the main examples work."""

import os
import python_codon_tables as pct

def test_basics():

    # LOAD ONE TABLE BY NAME
    table = pct.get_codons_table("b_subtilis_1423")
    assert table['T']['ACA'] == 0.4
    assert table['*']['UAA'] == 0.61

    # LOAD ALL TABLES AT ONCE
    codon_tables = pct.get_all_available_codons_tables()
    assert codon_tables['c_elegans_6239']['L']['CUA'] == 0.09

def test_download_codon_table(tmpdir):
    table = pct.download_codons_table(taxid=316407)
    assert table['*']['UAG'] == 0.07
    target = os.path.join(str(tmpdir), 'test.csv')
    table = pct.download_codons_table(taxid=316407, target_file=target)

def test_readme_example():
    table = pct.get_codons_table("b_subtilis_1423")
    assert table['T']['ACA'] == 0.4
    assert table['*']['UAA'] == 0.61

    # LOAD ALL TABLES AT ONCE
    codons_tables = pct.get_all_available_codons_tables()
    assert codons_tables['c_elegans_6239']['L']['CUA'] == 0.09

    # GET A TABLE DIRECTLY FROM THE INTERNET
    table = pct.download_codons_table(taxid=316407)
    assert table['*']['UGA'] == 0.29

def test_readme_example():
    table = pct.get_codons_table("b_subtilis_1423")
    assert table['T']['ACA'] == 0.4
    assert table['*']['UAA'] == 0.61

    # LOAD ALL TABLES AT ONCE
    codons_tables = pct.get_all_available_codons_tables()
    assert codons_tables['c_elegans_6239']['L']['CUA'] == 0.09

    # GET A TABLE DIRECTLY FROM THE INTERNET
    table = pct.download_codons_table(taxid=316407)
    assert table['*']['UGA'] == 0.29

def test_get_codons_table():
    for table_name in (1423, "1423", "b_subtilis", "b_subtilis_1423"):
        table = pct.get_codons_table(table_name)
        assert table['T']['ACA'] == 0.4
        assert table['*']['UAA'] == 0.61