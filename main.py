import time


def afficher_heure(heure):
    if len(heure) != 3:
        print("Format d'heure invalide.")
        return

    heures, minutes, secondes = heure
    if heures < 0 or heures > 23 or minutes < 0 or minutes > 59 or secondes < 0 or secondes > 59:
        print("Heure invalide.")
        return

    while True:
        heure_actuelle = time.localtime()
        heure_str = time.strftime("%H:%M:%S", heure_actuelle)
        print(heure_str, end='\r')
        time.sleep(1)

        if heure_actuelle.tm_hour == heures and heure_actuelle.tm_min == minutes and heure_actuelle.tm_sec == secondes:
            print("\nRéveil ! L'heure de l'alarme est atteinte.")
            break


def regler_alarme(heure):
    global alarme
    alarme = heure


def mode_affichage(mode):
    global format_heure
    if mode == 12:
        format_heure = "%I:%M:%S %p"
    elif mode == 24:
        format_heure = "%H:%M:%S"


def affichage_heure():
    while True:
        heure_actuelle = time.localtime()
        heure_str = time.strftime(format_heure, heure_actuelle)
        print(heure_str, end='\r')
        time.sleep(1)

        if heure_actuelle[:3] == alarme:
            print("Réveil ! Tut Tut Tut .")
            break



alarme = None
format_heure = "%H:%M:%S"


regler_alarme((17, 56, 20))
mode_affichage(24)

afficher_heure((17, 56, 20))

