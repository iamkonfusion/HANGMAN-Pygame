
def random_word(dico:dict) :
    """
    Cette fonction sélectionne la dernière clé d'un dictionnaire
    et la stocke dans une liste.
    + Créée un tuple contenant cette clé et sa valeur.
    + Créée une liste contenant la dernière valeur de la liste
      et la supprime dans la liste et dans le dictionnaire.

    :entrées: dico <dict> : Dico contenant les clés qu'on veut relever
    :sorties: keys        <liste> : contient tous les elmts du dico, sauf le dernier
              mots_appris <liste> : contient la dernière clé du dico
              (word,trad) <tuple> : contient la dernière clé du dico et sa valeur
    """
    keys = []                                        # liste de keys pour les trouver ds dico
    for key in dico:
        keys.append(key)

    (word,trad) = (keys[-1], dico.get(keys[-1]))     # fin liste pour éliminer elmnt dicos déjà vus

    mots_appris = []
    mots_appris.append((keys.pop(),(word,trad)[1]))  # ajouté à réviser
    dico.pop(mots_appris[-1][0])
    return dico, keys, mots_appris, (word,trad)

def creation_liste_caractere(mot_trad: tuple) -> list:
    '''
    Cette fonction sépare les lettres d'un mot qui sont dans une liste.

    :entrées: mot_trad   <tuple> : tuple de deux éléments (mot_anglais, traduction)
    :sorties: word       <list>  : contient les lettres du mot anglais
              traduction <list>  : contient les lettres de sa traduction
    '''
    word = [mot_trad[0][i] for i in range(len(mot_trad[0]))]
    traduction = [mot_trad[1][i] for i in range(len(mot_trad[1]))]
    return word, traduction

def conversion_tirets(word: list, trad: list) -> list:
    '''
    Transforme 2 listes de caractères en 2 listes de tirets (mm nb de caract.)

    :entrées: word         <list> : 1 caractère par index
              trad         <list> : 1 caractère par index
    :sorties: display_word <list> : tirets
              display_trad <list> : tirets
    '''

    display_word = ["_" for i in range(len(word))]
    display_trad = ["_" for i in range(len(trad))]
    return display_word, display_trad

def entrez_une_lettre(lettres_deja_rentrees:list, lettre):
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
              "n","o","p","q","r","s","t","u","v","w","x","y","z"]
  if lettre in alphabet and lettre not in lettres_deja_rentrees:
    lettres_deja_rentrees.append(lettre)
    return lettre, lettres_deja_rentrees
  else:
    print ("Oops ! Entrez une autre lettre :)")
    return "Oops !Entrez une autre lettre :)"