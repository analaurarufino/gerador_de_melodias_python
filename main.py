import create_notes
import create_audio
import dictionary

notes = ['C','C#', 'D', 'D#', 'E', 'F','F#','G','G#', 'A','A#', 'B']

def input_check(inputStr):
    if inputStr not in notes:
        return False
    return True

if __name__=='__main__': 
    print("TONS --> ", notes)
    Note = input("Digite o tom do sem Solo: ")
    Duration =  float(input("Digite a duração de cada nota *(Recomenda-se utilizar valores de 0.1 a 1): "))
    Note = Note.upper()
    if(input_check(Note)):
        
        padrao = create_notes.pattern()
        notasreturn = dictionary.convert(padrao, Note)
        
        create_audio.create_solo(notasreturn, Duration)
        #create_audio.play_audio("audio.wav")
    else:
        print("Entrada inválida")
    #Função que recebe uma string de numeros e o tom e retorna uma string de notas 
    # *pode adicinar tempo entre as notas
    


