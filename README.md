# Structify_Assessment

**Code Explanation**
Created two dictionaries, "startPointsdict1" and "endPointsdict2" with indices corresponding to "s" and "e" labels in "chordPoints".
Sorted the dictionaries based on their keys.
Created a new list "sortedChords" by interleaving values from "chordRadians" based on the sorted arrangement of "s" and "e" labels.
Iterate over pairs of the given chords in "SortedChords" and count the number of intersecting chords.
Created a set "remembered" to save the previous intersecting chords so that now two same points get calculated in the final output.
Print the number of intersection points

**Time Complexity breakdown**
For creating dictionaries, time complexity will be O(n)
Sorting the dictionaries - O(n*log(n))
"sortedChords" takes O(n) time.
To count the number of intersections, it hs time complexity of O(n^2)
Hence, the overall time complexity of this algorithm is O(n^2)
