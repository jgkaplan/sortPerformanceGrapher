Idea
----
I think different sorting algorithms converge to a sorted array at different rates. If we don't care about a fully sorting, and only want something to be "mostly sorted", can we achieve better performance by cutting algorithms off early? If so, when should we cut them off?

I attempt to roughly measure this convergence rate by counting the inversions in an array (the number of inversions is the number of elements i, j with i < j and arr[i] > arr[j]).

TODO
----
- Currently I'm using a O(n^2) trivial algorithm to count inversions.
I've read that it can be done much faster, in O(n sqrt(log(n))) time, so I'd like to look into that implementation.

- Better determination of where to count an iteration of different algorithms

- Implementing more algorithms