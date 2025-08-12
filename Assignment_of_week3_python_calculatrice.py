def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2 :
     definitive_price = price - (price* discount_percent)
     
    else:
        definitive_price = price
        
    return definitive_price

price = float(input(" veuillez renseigner le prix de l'article: "))
discount_percent = float(input("veuillez indiquer le pourcentage de ma remise sur une echelle de 0% à 100%: "));
discount_percent  = discount_percent / 100
result = calculate_discount(price, discount_percent );
print("Le prix final est", result)
