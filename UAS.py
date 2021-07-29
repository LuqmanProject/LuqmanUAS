print('1. Sequential Search')
print('2. Binary Search')

menu = input("Masukkan Menu Anda :")

if (menu == '1'):
    # Function
    def seq(data, nilai):
        mulai = 0
        temp = False
        while mulai < len(data) and not temp:
            if data[mulai] == nilai:
                temp = True
                print (" Nilai",nilai,"berada pada indeks ke-",mulai)
            else:
                mulai += 1
        return temp

    # JSON
    import json
    myjson = open('uas.json')
    datajson = myjson.read()
    isijson = json.loads(datajson)
        # Konversi dari STR ke INT
    nilai = int(input("Masukkan Data Yang Akan Anda Cari (Kelipatan 10) :"))
    
    # Pemanggilan
    seq(isijson['sequential'],nilai)

elif (menu == '2'):
    # Function
    def bin(data, nilai):
        mulai = 0
        akhir = len(data)-1
        temp = False
        while mulai <= akhir and not temp:
            tengah = (mulai+akhir)//2
            #computation
            if (data[tengah] == nilai):
                temp = True
                print("Nilai",nilai,"Ditemukan Pada Indeks ke-",tengah)
            else:
                # nilai < tengah
                if (nilai<data[tengah]):
                    akhir = tengah -1
                # nilai > tengah
                else:
                    mulai = tengah +1

    
    # JSON
    import json
    myjson = open('uas.json')
    datajson = myjson.read()
    isijson = json.loads(datajson)
        # Konversi dari STR ke INT
    nilai = int(input("Masukkan Data Yang Akan Anda Cari (Kelipatan 10) :"))
    
    isijson['biner'].sort()

    # Pemanggilan
    bin(isijson['biner'],nilai)

else:
    print('Menu tidak tersedia')