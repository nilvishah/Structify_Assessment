def intersectingChords(chordRadians, chordPoints):
    #dictionaries to store the indices of "s" and "e" labels in chordPoints
    startPointDict = {}
    endPointDict = {}

    for index, label in enumerate(chordPoints):
        if 's' in label:
            startPointDict[label] = index
        elif 'e' in label:
            endPointDict[label] = index
            
    # Sort the dictionaries based on keys
    sortedStartPoints = sorted(startPointDict.items())
    sortedEndPoints = sorted(endPointDict.items())

    # Create a new list 'sortedChords'
    sortedChords = [0] * len(chordRadians)
    ptr = 0

    for _, val in sortedStartPoints:
        sortedChords[ptr] = chordRadians[val]
        ptr += 2

    ptr = 1

    for _, val in sortedEndPoints:
        sortedChords[ptr] = chordRadians[val]
        ptr += 2

    remembered = set()
    output = 0

    # Count the number of intersecting chords
    for i in range(0, len(sortedChords), 2):
        for j in range(0, len(sortedChords), 2):
            if i == j:
                continue

            if (sortedChords[i] >= sortedChords[j] and sortedChords[i] <= sortedChords[j+1]) or (sortedChords[i+1] >= sortedChords[j] and sortedChords[i+1] <= sortedChords[j+1]):
                intersectingChords = str(sortedChords[i] + sortedChords[i+1] + sortedChords[j] + sortedChords[j+1])

                if (intersectingChords not in remembered):
                    output += 1
                    remembered.add(intersectingChords)

    return output

#Output
print("[0.78, 1.47, 1.77, 3.92] has", intersectingChords([0.78, 1.47, 1.77, 3.92], ["s_1", "s_2", "e_1", "e_2"]), "intersections")
print("[0.9, 1.3, 1.70, 2.92] has", intersectingChords([0.9, 1.3, 1.70, 2.92], ["s1", "e1", "s2", "e2"]), "intersections")
