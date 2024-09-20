a = 15000
b = "Matt"
c = "Frank"
d = "nasi goreng"
cakap = f"{b}: Hey, {c}! mau beli apa?"
cakap1= f"{c}: Mau beli {d}, {b}!"
cakap2 = f"{b}: Beli berapa kau?"
cakap3 = f"{c}: Aku beli..."
co11 = f"{b}: Oke {c}, ditunggu yaa"
co12 = f"{c}: Siap!"
co21 = f"{b}: Waduh, kurang ini uangnya"
co22 = f"{c}: Alamak, ya sudah beli 3 saja"
co23 = f"{b}: Siap {c}!"
print(cakap)
print(cakap1)
print(cakap2)
print(cakap3)
e = int(input())
jumlah = a * e
def cooking(jumlah):
    if (jumlah <= 45000):
        return True
    else:
        return False
if jumlah <= 45000:
    print(co11)
    print(co12)
else:
    print(co21)
    print(co22)
    print(co23)