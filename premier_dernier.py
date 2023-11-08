def debut_fin():
    sequence = input("Entre une lise, texte ou mot: ")
    if isinstance(sequence, str):
        return sequence[0] + sequence[-1]
    elif isinstance(sequence, list):
        return [sequence[0], sequence[-1]]
    elif isinstance(sequence, tuple):
        return sequence[0], sequence[-1]
    else:
        return "Type non pris en charge"

print(debut_fin())
