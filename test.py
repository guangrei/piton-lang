Impor unittest

Kelas Testing(unittest.TestCase):
    
    fungsi test_ting(self) -> None:
        Deklarasi angka i: int
        angka = 1
        untuk i pada jarak(1,4):
            self.assertTrue(angka==i)
            angka = angka+1

jika __name__=="__main__":
	unittest.main()
	