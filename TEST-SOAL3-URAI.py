#FUNGSI URAI
def urai(yourString):                # sebuah function dengan nama urai dengan satu parameter yaitu yourString
    uraiString = ''                  # empty string
    for char in list(yourString):    # looping char in list(yourString)
        print (uraiString, end='')   # me-ngeprint setiap uraiString ke kanan
        uraiString+=char             # uraiString akan ditambah dengan char baru sesuai dengan looping
    return uraiString                # return nilai uraiString
print(urai('Code'))                  # print(urai('Code'))  
print(urai('Python'))                # print(urai('Python')) 
print(urai('Purwadhika'))            # print(urai('Purwadhika'))