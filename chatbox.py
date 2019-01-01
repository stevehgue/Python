#chatbox
print("Vous êtes connecté à notre chatbox, commencez par dire bonjour, if you want to quit it, say: bye.")
while 1:
    reponse = input()
    if reponse == "Bonjour":
        print("Bonjour utilisateur, je suis le chatbot, est-ce que ça va?")
        reponse = input()
        if reponse == "Oui":
            print("Je suis content que tu ailles bien.")
        elif reponse == "Non":
            print("J'espere que ça ira mieux peut importe ce que tu traverse.")
        reponse = input()
        if reponse == "Bye":
            print("Ce fut un plaisir de parler avec toi, au revoir.")
            break
    else:
        print("Vous devez déjà dire bonjour.")
