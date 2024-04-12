print ("=============Calc 3000==============")

for (str repeat, repeat != "Sair" or "sair", repeat = str(input("\nDigite \"Sair\" para finalizar."))) :
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    option = str(input("\nOperador: "))

    if (option == "+") :
        print ("\nResultado: \"", num1+num2, "\".")

    if (option == "-") :
        print ("\nResultado: \"", num1-num2, "\".")

    if (option == "*") :
        print ("\nResultado: \"", num1*num2, "\".")

    if (option == "/") :
        print ("\nResultado: \"", num1/num2, "\".")

    repeat = str(input("==================================\n\nDigite \"Sair\" para finalizar."))
