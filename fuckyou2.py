def menyatakan_perasaan():
    print("Halo, [indira latifani]!")
    print("Aku punya sesuatu untukmu...")
    print("Aku bukan tukang pos, tapi aku punya surat cinta untukmu!")
    print("Apakah kamu mau menjadi 'variable' istimewaku? (Ya/Tidak)")

    jawaban = input()

    if jawaban.lower() == "ya":
        print("Kamu adalah 'constant' yang membuat hidupku stabil!")
        print("Kita seperti program yang berjalan bersama-sama. 😊")
    else:
        print("Mungkin suatu saat 'variable' kita akan sesuai. Keep coding!")

if __name__ == "__main__":
    menyatakan_perasaan()
