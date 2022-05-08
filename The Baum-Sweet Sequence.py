'''
Wikipedia: The Baum–Sweet sequence is an infinite automatic sequence of 0s and 1s defined by the rule:

bn = 1 if the binary representation of n contains no block of consecutive 0s of odd length;
bn = 0 otherwise;

for n ≥ 0.

Define a generator function baum_sweet that sequentially generates the values of this sequence.

It will be tested for up to 1 000 000 values.

Note that the binary representation of 0 used here is not 0 but the empty string ( which does not contain any blocks of consecutive 0s ).
'''
import math

import numpy as np


def baum_sweet(n):
    binRep = [[0]]
    for i in range(1, n):
        lastRep = binRep[-1]
        nextRep = lastRep

        # Iter over all elements from last binary representation
        for j in range(int(math.log2(i)), -1, -1):

            # If all Number of the representation are 1
            if j == (0) and lastRep[0] == 1:
                nextRep = [[1]]
                for k in range(int(math.log2(i)) + 1):
                    nextRep.append([0])
                binRep.append(nextRep)
                break

            elif lastRep[j] == 0:
                nextRep[j] = 1
                binRep.append(nextRep)
                break

            else:
                nextRep[j] = 1



    # Get binaray Repräsentation

    # your code here (yield values)
