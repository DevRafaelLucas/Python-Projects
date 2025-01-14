print("==================")
print("Apresente-se")
print("==================")

nome = input("Qual o seu nome?\n ")
idade = input("Qual a sua idade?\n ")
print("Então o seu nome é " + nome + " e você tem ", idade, " anos")

verdade = input("Está correto? digite (S) para sim e (N) para não: ")
if (verdade == "S" or "s"):
    print("Prazer em conhecer você! " + nome)
elif (verdade == "N" or "n"):
    print("Recomece o programa e tente novamente")
else:
    print("Erro, tente novamente")
