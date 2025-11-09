import basic as bc

text = "Aldiansyah Ombi F1G124036"
key = 3

enkripsi = bc.caesar_chiper.enkripsi(text,key)
print(enkripsi)

dekripsi = bc.caesar_chiper.dekripsi(enkripsi, key)
print(dekripsi)