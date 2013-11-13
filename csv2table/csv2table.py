import csv
import sys

with open(sys.argv[1]) as f:
    data = csv.reader(f)
    
    texTable=[' & '.join(x) for x in data]

    names = texTable.pop(0)
    names=names.split('&')
    names = [r'{\bf '+x+'}' for x in names]
    names = '&'.join(names)
    cols = names.count('&')+1
    
    env = r'\begin{tabular}{|'
    env += ''.join(['c|']*cols) +'} \n'
    env += r'\hline' +'\n'
    x = r'\\'+'\n'+r'\hline'+'\n'
    texTable = x.join(texTable)
    names = names+x
    texTable = names+texTable
    
    texTable = env+texTable+x+'\end{tabular}'
    print(texTable)
