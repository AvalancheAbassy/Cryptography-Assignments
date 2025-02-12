"""Brute force decrypts a given ciphertext with all 26 possible ceaser shifts"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(ciphertext, shiftamount):
    plaintext = ""
    for L in ciphertext:
        position = alphabet.index(L)
        newposition = position - shiftamount
        plaintext += alphabet[newposition]
    return plaintext

ciphertext="ycvejqwvhqtdtwvwu"

for i in range(26):
    print(decrypt(ciphertext, i))

#This function returns this for the given ciphertext:

#ycvejqwvhqtdtwvwu
#xbudipvugpscsvuvt
#watchoutforbrutus **
#vzsbgntsenqaqtstr
#uyrafmsrdmpzpsrsq
#txqzelrqcloyorqrp
#swpydkqpbknxnqpqo
#rvoxcjpoajmwmpopn
#qunwbionzilvlonom
#ptmvahnmyhkuknmnl
#osluzgmlxgjtjmlmk
#nrktyflkwfisilklj
#mqjsxekjvehrhkjki
#lpirwdjiudgqgjijh
#kohqvcihtcfpfihig
#jngpubhgsbeoehghf
#imfotagfradndgfge
#hlenszfeqzcmcfefd
#gkdmryedpyblbedec
#fjclqxdcoxakadcdb
#eibkpwcbnwzjzcbca
#dhajovbamvyiybabz
#cgzinuazluxhxazay
#bfyhmtzyktwgwzyzx
#aexglsyxjsvfvyxyw
#zdwfkrxwirueuxwxv

# In the context of this decryption, the most likely plaintext is watchoutforbrutus, where the ciphertext is shifted by 2
