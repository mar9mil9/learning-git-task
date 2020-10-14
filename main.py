#Program "Lista Zakupów" do nauki git'a

lists = {
    "Piekarnia": ["Chleb", "Pączek", "Bułki"],
    "Warzywniak": ["Marchew", "Seler", "Rukola"],
    "Papiernik": ["Zeszyt A4", "Pióro", "Atrament", "Kałamarz" #Zmiany do pierwszego commit'a na github'a
}
amount = 0
for list in lists:
    print("Idę do ",list,", kupuję tu następujące rzeczy:",lists[list])
    amount = amount + len(lists[list])
    print("W sumie kupuję",amount,"produktów.")
    
    
