csv2table
=====

Ever have a csv table that you wish you could
insert into a LaTeX `\tabular` environment without
too much hassle?

Example Usage
------
```shell
$ python3 csv2table.py example.csv 
\begin{tabular}{|c|c|} 
\hline
{\bf Year }&{\bf  Production (In Thousands of Barrels)}\\
\hline
1949 & 1841940\\
\hline
1950 & 1973574\\
\hline
1951 & 2247711\\
\hline
...
...
```
Copy `csv2table.py` into any directory with csvs, and
quickly generate copyable LaTeX tables.
 
