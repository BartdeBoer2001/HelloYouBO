print("Dit is mijn eindproject: de tetztzbased applicatie in Python.")
print("Dit keuzeverhaal gaat over Wahhab, uit Irak.")
print("Door spanningen in Irak is er een oorlog uitgebroken, en kon Wahhab zichzelf nietmeer zijn.")
print("Het verhaal start vlak voordat hij gaat vluchten.")
print("Nog belangrijk: als er geen geldig antwoord word gegeven, gaat het programma altijd uit van de tweede keuze. Let dus op dat je het goed invult.")

print("Wahhab wordt wakker, en gaat op zijn tempo naar beneden om wat te gaan drinken en om TV te kijken.")
print("Tijdens het nieuws hoort hij dat in zijn woonplaats de politie is binnengevallen om Jezidi's te zoeken.") 
print("Wat deed hij nadat hij dat hoorde?")
print("A - Wahhab ging naar zijn buren toe, om te vragen of zij er meer vanaf wisten.")
print("B - Wahhab ging snel zijn spullen pakken om te vluchten, om enige confrontatie te voorkomen.")
vraag1 = input("A of B? ")
if vraag1 == ("A") or ("a"):
    print("Wahhab besloot om naar zijn buren te gaan en om te vragen of zij meer wisten.")
    print("Jammer genoeg wisten ze er zelf redelijk weinig van., al vertrouwde Wahhab het niet helemaal.")
    print("A - Wahhab bleef doorvragen.")
    print("B - Wahhab ging terug naar zijn huis, om spullen te pakken en te vluchten.")
    vraag2 = input("A of B? ")
    if vraag2 == ("A") or ("a"):
        print("Wahhab bleef doorvragen")
        print("Het blijkt dus dat zijn buren hem hadden verraden, voor een grote som geld.")
        print("Ze hadden ook een lijn openstaan voor contact met de politie.")
        print("Toen Wahhab snel wou wegrennen, stond de politie al voor de deur.")
        print("Dit is dus het einde van het verhaal. Wahhab zit vast in de cel en kan er voorlopig ook niet uitkomen.")
    else:
        print("Wahhab ging snel naar huis. Hij kon veel spullen pakken, maar hij hoorde de sirenes, dus het was een slimmer idee om op de voet te gaan.")
        print("Waar ging Wahhab eerst heen?")
        print("A - Wahhab ")
else:
    print("Wahhab pakte gauw alle spullen die hij nodig had: tandenborstel, kleding, portemonee, etc")
    print("Wahhab stapte in zijn auto en reed snel weg")
    print("Reed hij eerst langs zijn broer om hem mee te nemen of ging hij alleen?")
    print("A - Hij nam zijn broer mee")
    print("B - Hij ging alleen")
    vraag3 = input("A of B? ")
    