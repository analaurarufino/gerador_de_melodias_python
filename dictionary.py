


def convert(string, note):
    if note == 'C':
        notes = [{ 
            1: '-C',
            2: '-D',
            3: '-E',
            4: '-F',
            5: '-G',
            6: '-A',
            7: '-B',
            }]
    if note == 'C#':
        notes = [{ 
            1: '-c',
            2: '-d',
            3: '-F',
            4: '-f',
            5: '-g',
            6: '-a',
            7: '-C',
            }]
    if note == 'D':
        notes = [{ 
            1: '-D',
            2: '-E',
            3: '-f',
            4: '-G',
            5: '-A',
            6: '-B',
            7: '-c',
            }]
    if note == 'D#':
        notes = [{ 
        1: '-d',
        2: '-F',
        3: '-G',
        4: '-g',
        5: '-a',
        6: '-C',
        7: '-D',
        }]
    
    if note == 'E':
        notes = [{ 
            1: '-E',
            2: '-f',
            3: '-g',
            4: '-A',
            5: '-B',
            6: '-c',
            7: '-d',
            }]
    if note == 'F':
        notes = [{ 
            1: '-F',
            2: '-G',
            3: '-A',
            4: '-a',
            5: '-C',
            6: '-D',
            7: '-E',
            }]
    if note == 'F#':
        notes = [{ 
            1: '-f',
            2: '-g',
            3: '-a',
            4: '-B',
            5: '-c',
            6: '-d',
            7: '-F',
            }]
    if note == 'G':
        notes = [{ 
            1: '-G',
            2: '-A',
            3: '-B',
            4: '-C',
            5: '-D',
            6: '-E',
            7: '-f',
            }]
    if note == 'G#':
        notes = [{ 
        1: '-g',
        2: '-a',
        3: '-C',
        4: '-c',
        5: '-d',
        6: '-F',
        7: '-G',
        }]
    if note == 'A':
        notes = [{ 
            1: '-A',
            2: '-B',
            3: '-c',
            4: '-D',
            5: '-E',
            6: '-f',
            7: '-g',
            }]
    if note == 'A#':
        notes = [{ 
            1: '-a',
            2: '-C',
            3: '-D',
            4: '-d',
            5: '-F',
            6: '-G',
            7: '-A',
            }]
    if note == 'B':
        notes = [{ 
            1: '-B',
            2: '-c',
            3: '-d',
            4: '-E',
            5: '-f',
            6: '-g',
            7: '-a',
            }]
    for i in string: 
        string = string.replace(i,notes[0][int(i)])
    string = string + notes[0][1]
       # print(notes[0][int(i)])
    #print(string)
    return string

#dar um jeito de por aletaoriamente mais de um tracinho na string
#convert('123456', 'F')

#convert('123456', 'C')
