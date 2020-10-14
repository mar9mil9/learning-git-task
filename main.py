#Program "Lista Zakupów" do nauki git'a

lists = {
    "Piekarnia": ["Chleb", "Pączek", "Bułki"],
    "Warzywniak": ["Marchew", "Seler", "Rukola"],
}
amount = 0
for list in lists:
    print("Idę do ",list,", kupuję tu następujące rzeczy:",lists[list])
    amount = amount + len(lists[list])
    print("W sumie kupuję",amount,"produktów.")
