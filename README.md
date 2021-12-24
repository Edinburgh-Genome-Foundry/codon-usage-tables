Codon usage tables for various organisms, in CSV format
-------------------------------------------------------

This repository contains simple CSV files (in [``data/tables/``](https://github.com/Edinburgh-Genome-Foundry/codon-usage-tables/tree/master/data/tables)) of the codon usage of various organisms,
meant to be used by codon optimization software. All files are in the form

```
amino_acid,codon,relative_frequency
*,UAA,0.64
*,UAG,0.07
*,UGA,0.29
A,GCA,0.21
A,GCC,0.27
K,AAA,0.76
K,AAG,0.24
etc.
```

It also contains a script to download new codon usage tables, using a TaxID to identify organisms.

The data comes from [http://www.kazusa.or.jp](http://www.kazusa.or.jp) (they computed the codon usages from NCBI sequence data).

More informations are available [here](http://www.kazusa.or.jp/codon/readme_codon.html
) and here is the original paper to cite:

```
Codon usage tabulated from the international DNA sequence databases:
status for the year 2000.
Nakamura, Y., Gojobori, T. and Ikemura, T. (2000) Nucl. Acids Res. 28, 292.
```

Python bindings
---------------

To get these tables from Python, use the [python_codon_tables](https://github.com/Edinburgh-Genome-Foundry/codon-usage-tables/tree/master/python_codon_tables) package.



Contribute
----------

This repo was started at the Edinburgh Genome Foundry by Zulko and is released on [Github](https://github.com/Edinburgh-Genome-Foundry/codon-usage-tables) into the Public Domain, and is also available under the [CC0 license](LICENSE) (and no warranty whatsoever, please cross-check the codon usage with other sources if you are not sure). Feel free to add other tables if you think of more commonly used species.
