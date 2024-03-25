def baca_angka_dari_file(nama_file):
        with open(nama_file, 'r') as file:
            angka = [int(line.strip()) for line in file]
            return angka

def main():
    angka = baca_angka_dari_file("input.txt")
    if angka:
        total_penjumlahan = sum(angka)
        hasil_terformat = "{:,}".format(total_penjumlahan)
        print("Hasil penjumlahan angka:", hasil_terformat)

if __name__ == "__main__":
    main()
