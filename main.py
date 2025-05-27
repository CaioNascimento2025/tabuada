try:
    tabuada = int(input('a tabuada de qual número você quer ver'))
    for número in range(1,11):
        print('-' * 15)
        print(f'{tabuada} x {número} = {tabuada * número}')
    print('-' * 15)
        
except:
    print(f'{tabuada} não é um número válido')

