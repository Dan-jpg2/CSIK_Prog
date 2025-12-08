
def parse_dansk_int(text: str) -> int:
    text = text.lower().replace("-", " ").replace("  ", " ").strip()
    units = {
        'nul' : 0, 'en': 1, 'et': 1, 'én': 1,
        'to': 2, "tre": 3, 'fire': 4, 'fem': 5,
        'seks': 6, 'syv': 7, 'otte': 8, 'ni': 9
    }
    teens = {
        "ti": 10, "elleve": 11, "tolv": 12, "tretten": 13, "fjorten": 14,
        "femten": 15, "seksten": 16, "sytten": 17, "atten": 18, "nitten": 19
    }
    tens = {
        "tyve": 20, "tredive": 30, "fyrre": 40,
        "halvtreds": 50, "tres": 60, "halvfjerds": 70,
        "firs": 80, "halvfems": 90
    }
    multipliers = {
        "hundrede": 100,
        "hundred": 100,
        "tusind": 1000,
        "million": 1_000_000,
        "millioner": 1_000_000,
        "milliard": 1_000_000_000,
        "milliarder": 1_000_000_000,
    }
    # første forsøg, måske input er et tal
    try:
        return int(text)
    except ValueError:
        pass
    
    #Sammensatte ord etc "femogtredive"
    def parse_compound(word):
        for u in units:
            if word.startswith(u + 'og') and word[len(u)+2:] in tens:
                return units[u] + teens[word[len(u)+2:]]
        return None
    
    words = text.split()
    total = 0
    current = 0
    
    for word in words:
        # Ignorer og som binde ord
        if word == 'og':
            continue
        
        #sammensatte talord
        compound = parse_compound(word)
        if compound is not None:
            current += compound
            continue
        
        # units
        if word in units:
            current += units[word]
            continue
            
        #teens
        if word in teens:
            current += teens[word]
            continue
        
        #tens
        if word in tens:
            current += tens[word]
            continue
        
        #multipliers
        if word in multipliers:
            factor = multipliers[word]
            if current == 0:
                current = 1
            current *= factor
            total += current
            current = 0
            continue
        
        raise ValueError(f'Kan ikke forstå talordet: {word}')
    return total + current

print('Hello! Jeg skal bruge dit navn: ')

name = input("Skriv dit navn her: ")
count_str = input("Hvor mange gange skal jeg skrive dit navn? ")

count = parse_dansk_int(count_str)

for _ in range(count):
    print(name)
            

