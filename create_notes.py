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
    ]  
    random.shuffle(chords_patter)

    while(not stringChords.isnumeric()):
        if(len(chords_patter) != 0):
            stringChords = stringChords.replace("S", chords_patter.pop())
        else:
            stringChords = stringChords.replace("S", "1")
    return stringChords
    
if __name__ == '__main__':
    pattern()