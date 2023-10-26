# function mengira purata
def kira_purata(jumlah, bilangan):
    purata = jumlah / bilangan
    return purata

# atur cara utama
def main():
    senaraiNo = [] # menggunakan list[10, 20, 30, 40] (sebagai contoh)
    cont = True # Boolean ; cont = continue
    while cont: # struktur kawalan ulangan "selagi"
        try: # cuba dan tangkap value error
            nom = float(input("Masukkan nombor [X utk berhenti]: "))
            senaraiNo.append(nom)
        except ValueError:
            cont = False

    bilangan = len(senaraiNo) # kira bilangan nombor yang dimasukkan; len( ) = built-in function
    if bilangan > 0: # Pembetulan ralat di baris ini
        jumlah = sum(senaraiNo) # jumlahkan semua nombor; sum( ) = built-in function
        print(f"Purata = {kira_purata(jumlah, bilangan)}")
    print("Tamat")

if __name__ == "__main__":
    main()
