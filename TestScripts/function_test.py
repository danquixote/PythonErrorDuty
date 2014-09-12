#!/usr/bin/env python

import sys
from connect_to_pd import PDIncident as pdi


@pdi('6243b99729d742bd981db183dfae0fa9')
def foo(a, b):
    print(int(a)/int(b))
    return int(a)/int(b)


if __name__ == '__main__':
    foo(sys.argv[1], sys.argv[2])

