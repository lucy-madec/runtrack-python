print ("Entrez un message:")
message= input()
print ("Combien de rangs de décalage ?")
x= int(input())

def décalage(message, x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    jc = ""

    for i in message:
        if i in alphabet:
            initial = alphabet.index(i)
            deplacement = (initial + x) % 26
            jc += alphabet[deplacement]
        else:
            jc += i

    print(jc)

décalage(message, x)