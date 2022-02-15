[![DOI](https://zenodo.org/badge/429068361.svg)](https://zenodo.org/badge/latestdoi/429068361)

# **ED-NM_CSV**
### **Script to calculate and output edit distances for mapped reads**

This script produces a CSV file with statistics related to read edit distances (mean, percentage and count) for each interval and reads equal or above a defined mapping quality. If output is not specified basic stats will still be printed to stdout.

# Requirements
You will need the following python packages to run the script:
- python
- numpy
- pysam
- pysamstats

# Usage example:
Standard usage:
```
 python ED-NM_CSV.py -b in.bam -d 5 -o out.csv
 ```

Only consider specific regions:
 ```
 python ED-NM_CSV.py -b in.bam -d 5 -o out.csv -r CHR:1-150000 CHR:500000-1500000
 ```

Output all headers seperatly and only for reads MQ>30:
  ```
 python ED-NM_CSV.py -b in.bam -d 5 -o out.csv -s -q 30
 ```

For help use:
```
 python ED-NM_CSV.py -h
 ```

# Cite:
Please cite using the DOI:
Meriam Guellil. (2021). MeriamGuellil/ED-NM_CSV. Zenodo. https://doi.org/10.5281/zenodo.5707905

# References:
Walt, Stéfan van der, S. Chris Colbert, and Gaël Varoquaux. 2011. “The NumPy Array: A Structure for Efficient Numerical Computation.” Computing in Science & Engineering 13 (2): 22–30. https://doi.org/10.1109/MCSE.2011.37.

Pysam: Pysam Is a Python Module for Reading and Manipulating SAM/BAM/VCF/BCF Files. It’s a Lightweight Wrapper of the Htslib C-API, the Same One That Powers Samtools, Bcftools, and Tabix. n.d. Github. https://github.com/pysam-developers/pysam.

Miles, Alistair. Pysamstats. Github. https://github.com/alimanfoo/pysamstats.

