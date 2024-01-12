def do_fizzbuzz():

    for i in range(1,15+1):
        if i%3==0:
            print('fizz')
        elif i%6==0:
            print('buzz')
        else:
            print(f'{i}')

do_fizzbuzz()
