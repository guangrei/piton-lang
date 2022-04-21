__author__  = "guangrei"
__version__ = "V0.0.1"

# builtin function
jarak    = range
keluar   = exit
berhenti = quit
uraian   = enumerate
panjang  = len
masukan  = input
tipe     = type

# exception
BasisSalah   = BaseException
SintaksSalah = SyntaxError
TipeSalah    = TypeError
IsiSalah     = ValueError
ImporSalah   = ImportError
Pengecualian = Exception

# builtin class
Objek = object

# dari module
from time import time as waktu
from time import sleep as tidur

# fungsi terdefinisi

def tulis(*args, pem: str=' ', akhir: str= '\n', file=None) -> None:
    if file is not None:
        print(*args, sep=pem, end=akhir, file=file)
    else:
        print(*args, sep=pem, end=akhir)

def tanggal(*args) -> datetime.datetume:
    from datetime import datetime
    return datetime.now(*args)