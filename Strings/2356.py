while True:
    try:
        dna = input()
        cod = input()
        if cod in dna:
            print("Resistente")
        else:
            print("Nao resistente")
    except EOFError:
        break