#!/usr/bin/python3
import sys
from qtils.utils import update_references
import pathlib as pl

for x in sys.argv:
    if not isinstance(x, str):
        print("Inputs must be strings")
        sys.exit(0)
        
# choose a paper!
qmdfile = pl.Path(sys.argv[0])
bibfile = pl.Path(sys.argv[1])

print(qmdfile)
print(bibfile)

update_references(qmdfile,bibfile,inplace=True)

