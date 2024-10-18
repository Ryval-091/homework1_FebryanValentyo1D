#PROGRAM INI UNTUK MENGECEK JADWAL MATA KULIAH
print('-------- INI PROGRAM PENGECEK JADWAL MATA KULIAH --------')
print()

print('NAMA : FEBRYAN VALENTYO')
print('NIM  : 24090124')

print('')

print ('Selamat Datang ')
print('')
print('program ini hanya menerima input berupa angka integer')

print('')

print('Silahkan Pilih Opsi : ')
print('1.cari berdasarkan hari')
print('2.informasi mata kuliah')


opsi_pilihan = (1, 2)
opsiPilihan = int(input(''))

if opsiPilihan in opsi_pilihan:
        print('')
else : 
        print('Opsi Tidak Tersedia, Coba Lagi')
        print('input harus 1 atau 2')

if opsiPilihan ==1 :
    
    opsiHari = (1, 2, 3, 4, 5, 6, 7)
    print('Silahkan Pilih Opsi dari :')
    print('1. senin          5. jumat')
    print('2. selasa         6. sabtu')
    print('3. rabu           7. minggu')
   
    inputanHari = int(input(''))

    if inputanHari in opsi_pilihan:
        print('')
        if inputanHari == 1:
            print('---jadwal hari senin---')
            print(' 08.00-09.40 : kalkulus') 
            print(' 09.40-12.20 : konsep teknolgi informatika' )

        elif inputanHari == 2:
            print('---jadwal hari selasa---')
            print('hari ini tidak ada matkul') 

        elif inputanHari == 3:
            print('---jadwal hari rabu---')
            print(' 08.00 - 09.40 : Logika informatika')
            print(' 09.40 - 11.20 : bahasa inggris')
            print(' 11.20 - 13.00 : bahasa indonesia') 

        elif inputanHari == 4:
            print('---jadwal hari kamis---')
            print(' 10.30 - 12.10 : pendidikan agama') 
            print(' 13.50 - 16.20 : organisasi & arsitektur komputer')

        elif inputanHari == 5:
            print('---jadwal hari jumat---')
            print(' 09.40 - 11.20 : sistem operasi') 
            print(' 13.00 - 15.30 : algoritma dan struktur data 1')

        elif inputanHari == 6:
            print('---jadwal hari sabtu---')
            print(' ini hari libur')     

        elif inputanHari == 7:
            print('---jadwal hari minggu---')
            print(' ini hari libur')     
        
    else : 
        print('Opsi Tidak Tersedia')
        print('input harus angka diantara 1-7')
        
    
if opsiPilihan == 2 :

    opsiMatkul = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    print('Silahkan Pilih Opsi dari matkul berikut : ')
    print('1. kalkulus                          4. bahasa inggris               7. organisasi dan arsitektur komputer')
    print('2. konsep teknologi informasi        5. bahasa indonesia             8. sistem operasi')
    print('3. logika informatika                6. pendidikan agama             9. algoritma dan struktur data 1')

    inputMatkul = int(input(''))

    if inputMatkul in opsiMatkul :
        print('')
        if inputMatkul == 1:
            print('---------KALKULUS-------')
            print('Hari     : Senin')
            print('Jam      : 08.00 - 09.40')
            print('Tempat   : D4-3')
            print('Dosen    : Dairoh, M.Sc.')
    
        elif inputMatkul == 2:
            print('---------konsep teknologi informasi-------')
            print('Hari     : Kamis')
            print('Jam      : 09.40 - 11.20')
            print('Tempat   : D4-2')
            print('Dosen    : Ir. Ginanjar Wiro Sasmito, M.Kom')

        elif inputMatkul == 3:
            print('---------logika informatika-------')
            print('Hari     : Rabu')
            print('Jam      : 08.00 - 09.40')
            print('Tempat   : D4-2')
            print('Dosen    : Ardi Susanto, S.Kom, M.Cs.')

        elif inputMatkul == 4:
            print('---------bahasa inggris-------')
            print('Hari     : Rabu')
            print('Jam      : 08.00 - 09.40')
            print('Tempat   : D4-6')
            print('Dosen    : Lin Indrayanti, M.Pd.')

        elif inputMatkul == 5:
            print('---------bahasa indonesia-------')
            print('Hari     : Rabu')
            print('Jam      : 11.20 - 13.00')
            print('Tempat   : D4-8')
            print('Dosen    : Ratri Wikaningtyas, M.Pd.')

        elif inputMatkul == 6:
            print('---------pendidikan agama-------')
            print('Hari     : Kamis')
            print('Jam      : 10.30 - 12.10')
            print('Tempat   : D4-7')
            print('Dosen    : Alvin Qodri Lazuardy, S.Ag., M.Pd.')

        elif inputMatkul == 7:
            print('---------organisasi dan arsitektur komputer-------')
            print('Hari     : Kamis')
            print('Jam      : 13.50 - 16.20')
            print('Tempat   : D4-2')
            print('Dosen    : Romi Muharyono, S.Ag.')
            
        elif inputMatkul == 8:
            print('---------sistem operasi-------')
            print('Hari     : Jumat')
            print('Jam      : 09.40 - 11.20')
            print('Tempat   : D4-2')
            print('Dosen    : Taufiq Abidin, S.Pd., M.kom.')

        elif inputMatkul == 9:
            print('---------algoritma dan struktur data 1-------')
            print('Hari     : Jumat')
            print('Jam      : 13.00 - 15.30')
            print('Tempat   : D4-4')
            print('Dosen    : Achmad Miftahudin, S.Tr.kom.')
        


    else : 
        print('Opsi Tidak Tersedia')
        print('input harus angka diantara 1-9')
