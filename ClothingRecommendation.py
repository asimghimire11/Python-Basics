def recommend_clothes(weather, temperature):
    if weather == "sunny":
        if temperature >= 25:
            return "Wear shorts and a t-shirt."
        elif temperature >= 15:
            return "Wear shorts and a light shirt."
        else:
            return "Wear shorts and a long-sleeve shirt."
    elif weather == "rainy":
        if temperature >= 15:
            return "Wear a raincoat and waterproof shoes."
        else:
            return "Wear a raincoat, waterproof shoes, and a sweater."
    elif weather == "snowy":
        if temperature >= 0:
            return "Wear a jacket, gloves, and boots."
        else:
            return "Wear a heavy jacket, gloves, boots, and scarf."
    else:
        return "Sorry, I can't provide a recommendation for this weather condition."

weather = input("Enter the current weather condition (sunny, rainy, snowy): ").lower()
temperature = float(input("Enter the temperature in Celsius: "))

recommendation = recommend_clothes(weather, temperature)
print("Recommendation:", recommendation)
