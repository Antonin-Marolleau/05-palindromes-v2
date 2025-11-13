''' Ce code utilise le code de @Antonin-Marolleau dans son intégralité
# et est soumis aux restrictions du
# plagiat sur @Antonin-Marolleau dans son intégralité ainsi
# que du copyright ©2024-2025 pour son
# auteur @Antonin-Marolleau
 Il suit le modèle de @Daniel-Courivaud
'''
import unicodedata
import re
#### Fonction secondaire


def sans_accents(chaine): #source : https://stackoverflow.com/questions/517923/
    #what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
    '''
    OoO
    '''
    out = ''.join(c for c in unicodedata.normalize('NFD', chaine)
                  if unicodedata.category(c) != 'Mn')
    return out

def ispalindrome(p):
    '''
    OoO
    '''
    # votre code ici
    p = sans_accents(p) #les accents
    p = re.sub(r'[^a-zA-Z0-9]', '', p).lower().lower() #il y a des espaces -_-
    a = p[::-1] #Cas particulier : la syntaxe s[::-1] permet
    #de renverser la chaine de caractère en une seule opération:

    return p==a



#### Fonction principale


def main():
    '''
    OoO
    '''
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kàyak", "level", "rotor", "civique", "déifiè"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
