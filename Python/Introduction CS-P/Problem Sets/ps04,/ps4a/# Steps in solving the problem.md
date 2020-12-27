PS4A
# Steps in solving the problem:
1. Searching for a string permutator online and getting output for l = 3(abc) and l = 4(abcd)
2. Creating a graphic representation for the algorithm and outlining the change of the positions, see relevant ps4a-graphic
3. While examining the graphic representation of the change of positions in ps4a-graphic-abc.png:
    a. I could outline a pattern, in which the 1st poistion changes for ever 2nd repetition, I call this behavior a cycle
    b. In the first change of every cycle, the change of positions between the 2nd and the 3rd position is identical
    c. At the course of the procedure, the 1st position is changed twice: once it changes to the 2nd position, and in the next change it changes to the 3rd position.
4. While examining the graphic representation of the change of positions in ps4a-graphic-abcd.png:
    a. I could outline a pattern, in which the 1st position changes every 6th iteration, I call this behavior a cycle
    b. during the procedure, the 1st position is changed 3 times: once to the 2nd position, then to the 3rd position and finally to the 4th position
    c. Every cycle contains the same behavior for positions 2-4 as in the procedure for l=3 charachters
5. I'm starting to write a pseudocode in ps4a_pseudocode.txt, it's evolution could be tracked in ps4a_pseudocode_evolution.ipynb
6. Reaching a dead end. Need to figure out a mechanism to store only the top string to return,
