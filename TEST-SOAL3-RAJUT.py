#FUNGSI RAJUT
def rajut(yourUrai):                               # sebuah function dengan nama rajut dengan satu parameter yaitu yourUrai
    getRajut = []                                  # sebuah list kosong
    index_awal = yourUrai.rindex(yourUrai[0])      # variabel index_awal berisi index ke berapa yourUrai[0] itu ditemukan tetapi dari belakang, misalnya ketika yourUrai='CCoCodCode' maka dia akan mencari yourUrai[0] yaitu 'C' dari belakang string sehingga ditemukan index ke-6
    for i in range(len(yourUrai)):                 # looping i di didalam range(len(yourUrai)), misalkan yourUrai = 'CCoCodCode' maka akan berada pada range(0,10)
        if i in range(index_awal, len(yourUrai)):  # jika i berada dalam range(index_awal, len(yourUrai)) yaitu (6,10)
            getRajut.append(yourUrai[i])           # yourUrai ke-i akan ditambahkan ke dalam list getRajut
    return ''.join(getRajut)                       # return getRajut dengan menggabungkan char yang ada didalamnya
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))