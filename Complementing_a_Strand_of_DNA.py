t="AAAACCCGGT"
r=""
for x in t:
   if x=="A":
        r += "T"
   if x=="T":
        r += "A"
   if x=="G":
        r += "C"
   if x=="C":
        r += "G"
print(r[::-1])