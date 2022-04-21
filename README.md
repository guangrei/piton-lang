Piton adalah bahasa pemrogaman berbahasa Indonesia yang di transpiler ke python.

## Sintaks

Sintaks `piton` dan `python` tidak berbeda jauh.

kamu bisa mengimport module python apa saja, menggunakan python built in seperti function, class, dan variabel kecuali python keyword harus menggunakan yang sudah berbahasa indonesia.

untuk melihat sintaks piton, silahkan cek `grammar/piton.gram` dan `bahasa/Bahasa.py`.

## mini interpreter

sebelum code kamu sepenuhnya di transpiler ke python, piton akan menjalankan mini interpreter dan menghasilkan pesan error (jika terdapat kesalahan pada code) yang mudah dimengerti.

## Deklarasi dan Strict type

Piton mengadopsi `mypy` untuk mengecek type hints, oleh karena itu type hints dalam piton tidak hanya sekedar komentar.

kamu bisa dengan mudah mendeklarasikan type variabel dengan sintaks `Deklarasi` yang hanya dimiliki piton.

Deklarasi dapat ditempatkan dimana saja (global scope, function scope atau kelas scope).

`Deklarasi` dapat mendeklarasikan satu atau lebih variabel sekaligus, dengan pemisah koma.

contoh:
```python
Deklarasi test1: str, test2: int
```

kamu juga bisa mendeklarasikan variabel berbeda dengan type yang sama, seperti:
```python
Deklarasi test1: str, test2: int, test3 test4: float
```

untuk lebih banyak type hints, silahkan baca https://docs.python.org/3/library/typing.html

## Compile

agar file piton kamu dapat di import dari file piton lainnya atau dari python normal, kamu dapat mengcompilenya menjadi C extension, menggunakan perintah `piton file.py --compile`.

**"code yang di berikan type hints berjalan 10x lebih cepat dari yang tidak memiliki type hints setelah di compile menjadi C extension."**

## Install

untuk mennginstall piton kamu harus terlebih dulu sudah menginstal docker, lalu buat `alias` di env.

Linux/Mac
```
alias piton="docker run -it -v $(pwd):/piton --rm cumi/piton piton"
```

kemudian jalankan perintah `piton`
```
$ piton
Piton v.0.0.1 (default, Apr 13, 2022 14:37:23 WIB, https://github.com/guangrei/piton-lang)

Cara pakai: piton [file] [opsi]

OPSI (opsional)
---------------
-c, --compile         : mengcompile code menjadi C extension.
-n, --naturalisasi    : menaturalisasi sintaks non indonesia.
-d, --de-naturalisasi : me-denaturalisasi sintaks indonesia ke inggris.
-r, --raw             : menampilkan parsed raw sintaks daripada menginterpretasinya.

NB: hanya bisa menggunakan satu opsi.
```
buat file `test.py`
```python
Deklarasi test: str

test = "hello piton"
tulis(test)
```
lalu jalankan
```
$ piton test.py
hello piton
```

> lihat juga contoh script lainnya pada folder `contoh'

full interaksi dengan piton docker
```
docker run -it -v $(pwd):/piton --name piton cumi/piton bash
```
extend piton pada `Dockerfile`
```
FROM cumi/piton
...
```
## Kontribusi

piton saat ini masih dalam tahap awal pengembangan, kamu bisa berkontribusi dengan melaporkan bug, mengajakukan ide dll