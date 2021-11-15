listBaju=["Kaos","Kemeja","Kaos lengan panjang","Kemeja Jeans"]
listCelana=["Celana Panjang","Celana Jeans","Leggings","Kulot"]
listSepatu=["Nike air jordan v2","Nike air jordan v1","Nike air jordan v3","Nike air jordan v4"]
Total=[]

while True: 
    print("--- Daftar List Pakaian ---")
    print("-----------------")
    print(" 1. | Baju   | ")
    print(" 2. | Celana | ")
    print(" 3. | Sepatu | ")
    print("-----------------")
    pilihBarang=(input("masukkan list 1-3 : "))
    if pilihBarang== "1" :
        print("Pilih Baju")
        for baju in range(0,len(listBaju)):
            print(f"{baju+1} {listBaju[baju]}")
        ulangi= True
        while ulangi:
            pilihBaju=int(input(f"pilih list baju 1-4 : "))
            if pilihBaju <=0 or pilihBaju > len(listBaju):
                print("masukan list baju")
                for baju in range(0, len(listBaju)):
                    print(f"{baju+1} {listBaju[baju]}")
                continue
            else:
                Total.append(listBaju[pilihBaju-1])
                print("Pesanan")
                for list_total in range(0,len(Total)):
                    print(f"{list_total +1} {Total[list_total]}")
                ulangi= False
            continue
    elif pilihBarang == "2":
        print("Pilih Celana")
        for celana in range(0,len(listCelana)):
            print(f"{celana+1} {listCelana[celana]}")
        ulangi= True
        while ulangi:
            pilihcelana=int(input(f"pilih list celana 1-4 : "))
            if pilihcelana <=0 or pilihcelana > len(listCelana):
                print("masukan list celana")
                for celana in range(0, len(listCelana)):
                    print(f"{celana+1} {listCelana[celana]}")
                continue
            else:
                Total.append(listCelana[pilihcelana-1])
                print("Pesanan")
                for list_total in range(0,len(Total)):
                    print(f"{list_total +1} {Total[list_total]}")
                ulangi= False
            continue
    elif pilihBarang=="3":
        print("Pilih sepatu")
        for sepatu in range(0,len(listSepatu)):
            print(f"{sepatu+1} {listSepatu[sepatu]}")
        ulangi= True
        while ulangi:
            pilihsepatu=int(input(f"pilih list sepatu 1-4 : "))
            if pilihsepatu <=0 or pilihsepatu > len(listSepatu):
                print("masukan list sepatu")
                for sepatu in range(0, len(listSepatu)):
                    print(f"{sepatu+1} {listSepatu[sepatu]}")
                continue
            else:
                Total.append(listSepatu[pilihsepatu-1])
                print("Pesanan")
                for list_total in range(0,len(Total)):
                    print(f"{list_total +1} {Total[list_total]}")
                ulangi= False
    else:
        print("list tidak sesuai mohon isi kembali")
        continue
    tanya=""
    while tanya != "N":
        tanya= input("Tambah barang ? Y/N : ")
        print("====  List Pesanan ====")
        for list_total in range(0, len(Total)):
            print(f"{list_total +1}  {Total[list_total]} 1x")
        break