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

# Row Count
i = 1
while i <= n:

    # Print Spaces
    spaces = n - i
    for _ in range(spaces):
        print(" ", end='')

    # part 1 of pattern (Left Side)
    j1 = 2
    count1 = i
    while j1 <= (i):
        print(count1, end="")
        count1 = count1 - 1
        j1 = j1 + 1

    print("1", end="")

    # Part 2 of the pattern (Right side)
    j2 = 2
    while j2 <= (i):
        print(j2, end="")
        j2 = j2 + 1

    # Print New line
    print()

    # Add New row
    i = i + 1