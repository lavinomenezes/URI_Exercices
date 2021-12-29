txt = "úabí"
X = ''
for i in txt:
    if i.isascii() == True:
        txt.replace(i,'')
print(txt)