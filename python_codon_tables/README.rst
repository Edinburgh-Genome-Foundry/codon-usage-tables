Python Codon Tables
===================

.. image:: https://travis-ci.org/Edinburgh-Genome-Foundry/codon-usage-tables.svg?branch=master
    :target: https://travis-ci.org/Edinburgh-Genome-Foundry/codon-usage-tables

Provides codon usage tables as dictionnaries, for Python 3+.

Tables for the following organisms are provided with the library (any other
table can be downloaded using a TaxID):

- *B. subtilis*
- *C. elegans*
- *D. melanogaster*
- *E. coli*
- *G. gallus*
- *H. sapiens*
- *M. musculus*
- *M. musculus domesticus*
- *S. cerevisiae*

All the tables are from `kazusa.or.jp <http://www.kazusa.or.jp/codon/readme_codon.html>`_
and here is the original paper to cite:

.. code::

    Codon usage tabulated from the international DNA sequence databases:
    status for the year 2000.
    Nakamura, Y., Gojobori, T. and Ikemura, T. (2000) Nucl. Acids Res. 28, 292.

Usage
-----

.. code:: python

    import python_codon_tables as pct

    # PRINT THE LIST OF NAMES OF ALL AVAILABLE TABLES
    print ('Available tables:', pct.available_codon_tables_names)

    # LOAD ONE TABLE BY NAME
    table = pct.get_codons_table("b_subtilis_1423")
    print (table['T']['ACA'])  # returns 0.4
    print (table['*']['TAA'])  # returns 0.61

    # LOAD ONE TABLE BY TAXID (it will get it from the internet if it is not
    # in the builtin tables)
    table = pct.get_codons_table(1423)
    print (table['T']['ACA'])  # returns 0.4
    print (table['*']['TAA'])  # returns 0.61

    # LOAD ALL BUIL-IN TABLES AT ONCE
    codons_tables = pct.get_all_available_codons_tables()
    print (codons_tables['c_elegans_6239']['L']['CTA'])  # returns 0.09

- Notice that by default the tables use nucleotide T instead of U. Using ``get_codons_table('e_coli', replace_U_by_T=False)`` will leave Us as Us.

- In ``get_codons_table`` you can also provide a "shorthand" notation ``b_subtilis``, which will be automatically extended to ``b_subtilis_1423`` as it appears so in the built-in table (use this feature at your own risks!)

Contribute
----------

This project was started at the Edinburgh Genome Foundry by Zulko and is released on `Github <https://github.com/Edinburgh-Genome-Foundry/codon-usage-tables>`_ under a Public Domain licence (and no warranty whatsoever, please cross-check the codon usage with other sources if you are not sure). Feel free to add other tables if you think of more commonly used species.

Installation
------------

via pip:

.. code:: bash

    pip install python_codon_tables

Manual:

.. code:: bash

    (sudo) python setup.py install

More biology software
-----------------------

.. image:: https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/Edinburgh-Genome-Foundry.github.io/master/static/imgs/logos/egf-codon-horizontal.png
  :target: https://edinburgh-genome-foundry.github.io/

This library is part of the `EGF Codons <https://edinburgh-genome-foundry.github.io/>`_ synthetic biology software suite for DNA design, manufacturing and validation.
