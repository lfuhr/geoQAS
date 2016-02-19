#!/usr/bin/env python

import re, os
import fileinput
for fi in os.listdir('.'):
    print(fi)
    print(type(fi))
    if fi in {".DS_Store", "1.py", ".1.py.swp"}:
        continue
    with open(fi) as f:
        data = ''.join(i for i in f.read() if not i.isdigit())

    with open(fi, 'w') as f:
        f.write(data)
