import python_codon_tables as pct

# PRINT THE LIST OF NAMES OF ALL AVAILABLE TABLES
print ('Available tables:', pct.available_codon_tables_names)

# LOAD ONE TABLE BY NAME
table = pct.get_codons_table("b_subtilis_1423")
print (table['T']['ACA'])  # returns 0.4
print (table['*']['UAA'])  # returns 0.61


# LOAD ALL TABLES AT ONCE
codon_tables = pct.get_all_available_codons_tables()
print (codon_tables['c_elegans_6239']['L']['CUA'])  # returns 0.09
