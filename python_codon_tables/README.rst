Python Codon Tables
===================

.. image:: https://travis-ci.org/Edinburgh-Genome-Foundry/codon-usage-tables.svg?branch=master
    :target: https://travis-ci.org/Edinburgh-Genome-Foundry/codon-usage-tables

Provides codon usage tables as dictionnaries, for Python 3+

Supported organisms include:

- *B. subtilis*
- *C. elegans*
- *D. melanogaster*
- *E. coli*
- *G. gallus*
- *H. sapiens*
- *M. musculus*
- *M. musculus domesticus*
- *S. cerevisiae*

It is also possible to download new tables directly with
``download_codons_table(taxid=316407)``.

All the tables are from `kazusa.or.jp <http://www.kazusa.or.jp/codon/readme_codon.html>`_
and here is the original paper to cite:

.. code::

    Codon usage tabulated from the international DNA sequence databases:
    status for the year 2000.
    Nakamura, Y., Gojobori, T. and Ikemura, T. (2000) Nucl. Acids Res. 28, 292.


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

Usage
-----

.. code:: python

    import python_codon_tables as pct

    # PRINT THE LIST OF NAMES OF ALL AVAILABLE TABLES
    print ('Available tables:', pct.available_codon_tables_names)

    # LOAD ONE TABLE BY NAME
    table = pct.get_codons_table("b_subtilis_1423")
    print (table['T']['ACA'])  # returns 0.4
    print (table['*']['UAA'])  # returns 0.61

    # LOAD ALL TABLES AT ONCE
    codons_tables = pct.get_all_available_codons_tables()
    print (codons_tables['c_elegans_6239']['L']['CUA'])  # returns 0.09

    # GET A TABLE DIRECTLY FROM THE INTERNET
    table = pct.download_codons_table(taxid=316407)
    print (table['*']['UGA'])  # returns 0.29

If you have an internet connection you can also enter any taxid in
``get_codons_table`` and the table will be downloaded from the Kasuza website.
You can write for instance:

.. code:: python

    table = get_codons_table(1423)
    table = get_codons_table("1423")
    table = get_codons_table("b_subtilis_1423")
    table = get_codons_table("b_subtilis")

In the last line above we provided a "shorthand" notation ``b_subtilis``, which
will be automatically extended to b_subtilis_1423 as it appears so in the
built-in table (use this feature at your own risks!)