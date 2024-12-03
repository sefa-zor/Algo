"""
# Job01

def draw_rectangle(width, height):
    # Dessiner la première ligne (haut du rectangle)
    print("|" + "-" * (width - 2) + "|")

    # Dessiner les lignes intermédiaires (les côtés du rectangle)
    for _ in range(height - 2):
        print("|" + " " * (width - 2) + "|")

    # Dessiner la dernière ligne (bas du rectangle)
    if height > 1:
        print("|" + "-" * (width - 2) + "|")

# Exemple d'utilisation
draw_rectangle(10, 3)


# job02

def draw_triangle(height):
    for i in range(height):
        # Espaces avant les barres pour centrer
        spaces = " " * (height - i - 1)
        # Barres inclinées et espace au milieu
        slashes = "/" + " " * (2 * i) + "\\"
        # Affiche la ligne
        print(spaces + slashes)

    # Dessiner la base du triangle
    base = "_" * (2 * height)
    print(base)

# Exemple d'utilisation
height = int(input("Veuillez entrer la hauteur du triangle : "))
draw_triangle(height)


# job03

def draw_tapis(n):
    for i in range(n + 1):  # Satırları temsil eder
        line = ""  # Bu satırın içeriği
        for j in range(n + 1):  # Sütunları temsil eder
            if i == j:  # Eğer satır ve sütun aynıysa, çapraz üzerinde
                line += " "
            else:  # Diğer durumlar
                line += "*"
        print(line)  # Satırı ekrana yazdır

# Örnek kullanım
draw_tapis(10)


# 2.yontem

def draw_tapis_symmetry(n):
    for i in range(n + 1):  # Satırları temsil eder
        line = ""  # Bu satırın içeriği
        for j in range(n + 1):  # Sütunları temsil eder
            if i + j == n:  # Eğer i + j == n ise, çaprazın üzerinde
                line += " "
            else:  # Diğer durumlar
                line += "*"
        print(line)  # Satırı ekrana yazdır

# Örnek kullanım
draw_tapis_symmetry(10)


# job04

def cesar_cipher(message, shift):
    result = ""  # Chaîne pour stocker le message chiffré

    for char in message:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            # Détermine l'offset pour gérer les majuscules et les minuscules séparément
            offset = 65 if char.isupper() else 97
            
            # Calcule la nouvelle position avec décalage
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += new_char
        else:
            # Si ce n'est pas une lettre, on l'ajoute sans modification
            result += char

    return result

# Exemple d'utilisation
message = "il fait beau!"
shift = 3
chiffre = cesar_cipher(message, shift)
print("Message chiffré :", chiffre)

# Exemple de déchiffrement
dechiffre = cesar_cipher(chiffre, -shift)
print("Message déchiffré :", dechiffre)

# job05
def calcul_distance_par_semaine(nombre_marches, hauteur_marche_cm):
    # Convertir la hauteur des marches de cm à m
    hauteur_marche_m = hauteur_marche_cm / 100
    
    # Calculer la distance parcourue pour un aller-retour (monter et descendre)
    distance_par_aller_retour = 2 * nombre_marches * hauteur_marche_m
    
    # Calculer la distance quotidienne (5 fois par jour)
    distance_par_jour = 5 * distance_par_aller_retour
    
    # Calculer la distance hebdomadaire (7 jours dans une semaine)
    distance_par_semaine = 7 * distance_par_jour
    
    # Retourner la distance en mètres
    return round(distance_par_semaine, 2)

# Demander les valeurs à l'utilisateur
nombre_marches = int(input("Entrez le nombre de marches (x): "))
hauteur_marche_cm = int(input("Entrez la hauteur d'une marche en cm (y): "))

# Calculer et afficher le résultat
distance = calcul_distance_par_semaine(nombre_marches, hauteur_marche_cm)
print(f"Pour {nombre_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance:.2f} m par semaine.")

"""
# job06
def arrondir_notes(notes):
    notes_arrondies = []
    
    for note in notes:
        # Vérifier si l'étudiant a réussi le test (note >= 40)
        if note >= 40:
            # Trouver le prochain multiple de 5
            prochain_multiple = ((note // 5) + 1) * 5
            
            # Vérifier si la note est à moins de 3 points du prochain multiple
            if prochain_multiple - note < 3:
                notes_arrondies.append(prochain_multiple)
            else:
                notes_arrondies.append(note)
        else:
            # Notes en dessous de 40 ne sont pas modifiées
            notes_arrondies.append(note)
    
    return notes_arrondies

# Exemple d'utilisation
notes_etudiants = [73, 67, 38, 82, 45, 99, 43]
notes_finales = arrondir_notes(notes_etudiants)

# Affichage des résultats
print("Notes originales :", notes_etudiants)
print("Notes arrondies :", notes_finales)


exit()
