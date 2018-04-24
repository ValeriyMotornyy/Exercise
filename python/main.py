import sys

from sort   import bubbleSort
from sort   import selectionSort
from sort   import insertionSort
from sort   import mergeSort
from sort   import quickSort
from sort   import headSort
from sort   import sortingAlgorithms

from search import binarySearch
from search import searchingAlgorithms

from common import fisherYatesShuffle
from common import numberArray

""" Main """
def main(searches, sorts, array):
    """ Sorting algorithms """
    for key, value in sorts:
        print key
        fisherYatesShuffle(array)
        getattr(sys.modules[__name__], value)(array)
        print array
        print "\n"

    for key, value in searches:
        print key
        getattr(sys.modules[__name__], value)(array, array[5])
        print "%s %s" % ("Searching for 6th element:", array[5])
        print array
        print "\n"

main(searchingAlgorithms(), sortingAlgorithms(), numberArray())
