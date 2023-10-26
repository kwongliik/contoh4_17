# function mengira purata
def kira_purata(x, y):
    purata = jumlah / bilangan
    return purata

# atur cara utama
def main():
    senaraiNo = []
    cont = True
    while cont:
        try:
            nom = float(input("Masukkan nombor [X utk berhenti]: "))
            senaraiNo.append(nom)
        except ValueError:
            cont = False

    bilangan = len(senaraiNo)
    
    jumlah = sum(senaraiNo)
    print(f"Purata = {kira_purata(jumlah, bilangan)}")
    print("Tamat")

# JANGAN ubah kod di bawah!

if __name__ == "__main__":
    main()
