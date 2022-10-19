from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i <= n:
    col = 1
    first_char = (ord('A') + n ) - i
    while col <= i:
        print(chr(first_char - 1 + col), end='')
        col = col + 1
    print()
    i = i + 1