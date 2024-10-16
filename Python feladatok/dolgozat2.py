from datetime import datetime

eletkorok = []

evszam = int(input("Add meg a születési évedet: "))

aktualis_ev = datetime.now().year

eletkor = aktualis_ev - evszam

eletkorok.append(eletkor)

print(f"A legnagyobb életkor: {max(eletkorok)}")
print(f"Összesen {len(eletkorok)} életkor van a listában.")