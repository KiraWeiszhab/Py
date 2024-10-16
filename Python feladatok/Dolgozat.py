#1.Feladat
#Készíts egy programot amivel a megadott listából ki kell választani melyek azok a szavak,
#amelyek hosszúságának az értéke 5 és ki kell íratni a konzolra melyek ezek a szavak és hány darab van belőlük.

szavak = [
    "alma", "asztal", "doboz", "ceruza", "egér", "fotel",  
    "szék", "pohár", "táblázat", "könyv", "kulcs", "karkötő",
    "mobiltelefon", "számítógép", "egérpad", "monitor", "hangszóró", "szék",
    "asztalterítő", "függöny", "szőnyeg", "párna", "papucs", "cipőfűző",
    "naptár", "hűtőszekrény", "mosogatógép", "főzőlap", "mikrohullámú",
    "nyomtató", "scanner", "projektor", "távirányító", "szendvics",
    "tolltartó", "jegyzetfüzet", "irattartó", "mappa", "papír",
    "töltőtoll", "hegyező", "ragasztószalag", "füzet", "kapocs",
    "toll", "filctoll", "színesceruza", "vonalzó", "radír"
]

    
ötkarakteres_szavak= [szo for szo in szavak if len(szo)== 5]

print("A 5 karakter hosszú szavak:")

for szo in ötkarakteres_szavak:
    print(szo)
    
print(f"Összesen{len(ötkarakteres_szavak)} darab 5 karakter hosszú szó található.")


