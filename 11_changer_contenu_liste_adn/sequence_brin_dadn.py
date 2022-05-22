
def sequence():
    """Une fonction qui remplace toutes
    les lettes contenues dans une liste
    avec les lettres a,c,g,t

    Returns:
        list: liste des lettres changées
    """
    seq_adn = ["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
    new_seq = []

    for seq in seq_adn:
        if seq == "A":
            seq = "T"
        elif seq == "T":
            seq = "A"
        elif seq == "C":
            seq = "G"
        elif seq == "G":
            seq = "C"
        new_seq.append(seq)

    return new_seq


print(sequence())
