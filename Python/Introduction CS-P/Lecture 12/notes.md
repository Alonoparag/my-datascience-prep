## searching algorithm
* linear:
  * list doesn't have to be sorted
* bisectian:
  * list has to be sorted
* When SORT+O(log n) > O(len(n))? never
* in some cases, may **sort a list once** then do **many searches**
* **AMORTIZE cost**of the sort over many searches
* SORT+K*(log n) < k*O(n)
  * for large *k* **SORT time becomes irrelevant**, if cost of sorting is small enough
## permutation sort
* sort elemnts randomly every time the set is unsorted
## bubble sort
* complexity is O(n)
* sort items in pairs consecutively
  * swap elements in pair in such way that the smaller is first
  * when reached end of list, start over again
  * stop when no more swaps have been made
  * largest unsorted element always at end after pass, so at most N passes
## selection sort
* complexity is O(n)
* first step
  * extract minimum element
  * swap it with element at index 0
* subsequent step
  * in remaining sublist, extract minimum element
  * swap it with the element at index 1
* keep the left portion of the list sorted
  * at i'th step, first i elements in list are sorted
  * all other elements are bigger than first i elements
* loop invariant:
  * given prefot of list L[0:i] and suffix L[i+1:len(L)],  then prefix is sorted an no element in prefix is larger than smallest element in suffix
    1. base case: prefix empty, suffix whole list - invariant true
    2. induction step: move minimum element from suffix to end of prefix. since invariant true before move, prefix sorted after append.
    3. when exit, prefix is entire list, suffix empty, so sorted
## merge-sort
* complexity is O(n*log(n))
* use a divide-and-conquier approach:
  1. if list is of length 0 or 1, already sorted
  2. if list has more than one element, split into two lists, and sort each
  3. merge sorted sublists
     1. look at first element of each, move smaller to end of the result
     2. when one list empty, just copy rest of other list