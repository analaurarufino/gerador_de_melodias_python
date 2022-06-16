import random

def pattern():
    stringChords = "S"
    chords_patter = [
        "S321", 
        "2S65", 
        "S357653", 
        "S514131", 
        "4321765S", 
        "1235665S", 
        "61123S", 
        "12343S",
        "312352S",
        "6712176S"
    ]  
    random.shuffle(chords_patter)

    while(not stringChords.isnumeric() and len(stringChords) < 43):
        if(len(chords_patter) != 0):
            stringChords = stringChords.replace("S", chords_patter.pop())
        else:
            stringChords = stringChords.replace("S", "1")
    if "S" in stringChords:
        stringChords = stringChords.replace("S", "1")
    stringChords = stringChords + "1"
    return stringChords
    
if __name__ == '__main__':
    pattern()