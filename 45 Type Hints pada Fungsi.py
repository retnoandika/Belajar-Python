'''Type hints untuk fungsi'''

# bentuk standard fungsi yg telah dipelajari
'''
def fungsi(parameter):
    print(parameter)

fungsi(1)
fungsi("Ucup")
fungsi(True)
Type hints
'''

# penggunaan type hints
import string


def sepuluh_pangkat(argument:int) -> int:
    '''Fungsi dengan hint'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument:string):
    print(argument)

display("retno")