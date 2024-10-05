
def check_rijbewijsleeftijd():
    leeftijd = int(input("Hoe oud ben je?"))
    if leeftijd < 18:
        print("Je moet 18 zijn om met de auto te mogen rijden")
    elif leeftijd >= 18:
        print("Ik zou je aanraden om je rijbewijs te gaan halen, je leven is dan veel vrijer.")

check_rijbewijsleeftijd()