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
        #6112312343212356654321765132165357653514131
        create_audio.create_solo("A-C-C-D-E-C-D-E-F-E-D-A-D-E-G-A-A-G-F-E-D-C-B-A-G-C-E-D-C-A-G-E-G-B-A-G-E-G-C-F-C-E-C")
        #create_audio.play_audio("audio.wav")
    else:
        print("Entrada inválida")
    #Função que recebe uma string de numeros e o tom e retorna uma string de notas 
    # *pode adicinar tempo entre as notas
    


