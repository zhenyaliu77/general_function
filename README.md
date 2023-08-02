# general_function
Various scripts commonly used in bioinformatics，genomics and deep learning

## genomics
 * Screen for genes which include structural variants（SVs）

   `python search_gene.py -k 0.5 -sv sv.txt -gff genome.gff`

   k=0.5 indicates that the proportion of sv and gene overlap is greater than or equal to 50%
