s/\tO;O;/\t/g
s/\tO;O$/\tO/g
s/\tO;\([^O][^;]*\)\(;O.*\|$\)/\t\1/g
s/\tB|\([^;]*\);.*/\tB-\1/g
s/\tI|\([^;]*\);.*/\tI-\1/g
s/\tB|/\tB-/g
s/\tI|/\tI-/g
