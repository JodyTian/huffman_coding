1)Building frequency dictionary

2)Select 2 minimum frequency symbols and merge them repeatedly: Used Min Heap

3)Build a tree of the above process: Created a HeapNode class and used objects to maintain tree structure

4)Assign code to characters: Recursively traversed the tree and assigned the corresponding codes

5)Encode the input text. Added padding to the encoded text, if it’s not of a length of multiple of 8. Stored this padding information, in 8 bits, in the beginning of the resultant code.

6)Write the result to an output binary file, which will be our compressed file.
