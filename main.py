import create_notes
import create_audio

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def input_check(inputStr):
    if inputStr not in notes:
        return False
    return True

if __name__=='__main__': 
    print("TONS --> C D E F G A B")
    Note = input("Digite o tom do sem Solo:")
    if(input_check(Note)):
        create_notes.pattern()
        create_audio.create_solo("D-C-B-E-G-G-C-C-E-C-E-D-A-G-D-F-E-C-A-G")
        create_audio.play_audio("audio.wav")
    else:
        print("Entrada inválida")
    #Função que recebe uma string de numeros e o tom e retorna uma string de notas 
    # *pode adicinar tempo entre as notas
    


