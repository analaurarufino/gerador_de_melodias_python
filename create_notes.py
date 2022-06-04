def pattern(Chord):
    chords_patter = ["S32", "2S65", "S735", "1"] 
    auxString = Chord
    print(auxString)
    i = 0
    while(not auxString.isnumeric()):
        # index = auxString.find(Chord)
        auxString = auxString.replace(Chord, chords_patter[i])
        i += 1
    print(auxString)
    
if __name__ == '__main__':
    pattern('S')