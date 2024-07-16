def hello(name,language):

    greeting={
        "English":'Hello',
        "Tamil":"Vanakam",
        "Spanish":"Hola"
    }

    msg=f'{greeting[language]}{name}!'
    print(msg)
if __name__=="__main__":    
    import argparse

    parser = argparse.ArgumentParser(description='Provide a personal greeting')

    parser.add_argument("-n", "--name", metavar='name', required=True, help='The name of the person to greeting.')

    parser.add_argument("-l", "--language", metavar='language', choices=['English','tamil','Spanish'] ,help='the language og greeting')

    args = parser.parse_args()

    hello(args.name,args.language)
