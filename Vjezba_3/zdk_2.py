

def jedna_trecina(N):
    pet=5
    for i in range(N):
        pet = pet + 1./3.
    print(pet)
   # print(pet)
    for i in range(N):
        pet=pet-1./3.
    print(pet)



jedna_trecina(200)
jedna_trecina(2000)
jedna_trecina(20000)
#Rezultat se ne bi trebao podudarati s matematicki tocnim rezultatom, no nama se podudara, pretpostavka je da drukcija verzija pythona(i windowsa) odgovorna za to 