

def main():
    loop = True
    while loop:
        x=input('''
Complex? Calculator Made by Monte!
1 = Simple Stuff (add/subtract/multiply/divide/exponents)
2 = Sqr Root/Cube Root/Sqr

1, 2 or 3: ''')

        if x=='1': simple_math()
        if x=='2': sqr_stuff()

main()
