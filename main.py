opcao = -1;
while(opcao != 0):
    opcao = int(input("Digie a conversao desejada: \n"
                      "1-Celsius para Kelvin\n"
                      "2-Celsius para Fahrenheit\n"
                      "3-Kelvin para Fahrenheit\n"
                      "4-Kelvin para Celsius\n"
                      "5-Fahrenheit para Celsius\n"
                      "6-Fahrenheit para Kelvin\n"
                      "0-Sair do Programa\n"
                      "Opcao Desejada:"))
    if opcao == 1:
        print("Voce escolheu Celsius para Kelvin")
        temperaturaEmCelsius = float(input("Digite a temperatura em Celsius: "))
        temperaturaEmKelvin = temperaturaEmCelsius + 273
        print(f"A temperatura em Kelvin é {temperaturaEmKelvin:.2f}")
    elif opcao == 2:
        print("Voce escolheu Celsius para Fahrenheit")
        temperaturaEmCelsius = float(input("Digite a temperatura em Celsius: "))
        temperaturaEmFahrenheit = ((9/5)*temperaturaEmCelsius)+32
        print(f"A tempetura em Fahrenheit é de {temperaturaEmFahrenheit:.2f}")
    elif opcao == 3:
        print("Voce escolheu Kelvin para Fahrenheit")
        temperaturaEmKelvinParaConverterParaFahrenheit = float(input("Digite a temperatura em Kelvin: "))
        temperaturaEmFahrenheitDeKelvin = ((9*(temperaturaEmKelvinParaConverterParaFahrenheit - 273))/5) + 32
        print(f"A temperatura em Fahrenheit é de {temperaturaEmFahrenheitDeKelvin:.2f}")
    elif opcao == 4:
        print("Voce escolheu Kelvin para Celsius")
        temperaturaEmKelvinParaConverterParaCelsius = float(input("Digite a temperatura em Kelvin: "))
        temperaturaEmCelsiusDeKelvin = (temperaturaEmKelvinParaConverterParaCelsius - 273)
        print(f"A temperatura em Celsius é de {temperaturaEmCelsiusDeKelvin:.2f}")
    elif opcao == 5:
        print("Voce escolheu Fahrenheit para Celsius")
        temperaturaEmFahrenheitParaConverterParaCelsius = float(input("Digite a temperatura em Fahrenheit: "))
        temperaturaEmCelsiusDeFahrenheit = (5*(temperaturaEmFahrenheitParaConverterParaCelsius - 32))/9
        print(f"A temperatura em Celsius é de {temperaturaEmCelsiusDeFahrenheit:.2f}")
    elif opcao == 6:
        print("Voce escolheu Fahrenheit para Kelvin")
        temperaturaEmFahrenheitParaConverterParaKelvin = float(input("Digite a temperatura em Fahrenheit: "))
        temperaturaEmKelvinDeFahrenheit = ((5*(temperaturaEmFahrenheitParaConverterParaKelvin - 32))/9) + 273
        print(f"A temperatura em Kelvin é de {temperaturaEmKelvinDeFahrenheit:.2f}")
    elif opcao == 0:
        print("Saindo do programa...")
    else:
        print("Opção Inválida")