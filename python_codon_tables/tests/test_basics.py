"""Basic tests to check that the main examples work."""

import python_codon_tables as pct

def test_basics():

    # LOAD ONE TABLE BY NAME
    table = pct.get_table("b_subtilis_1423")
    assert table['T']['ACA'] == 0.4
    assert table['*']['UAA'] == 0.61

    # LOAD ALL TABLES AT ONCE
    codon_tables = pct.get_all_tables()
    assert codon_tables['c_elegans_6239']['L']['CUA'] == 0.09
