#Exercise 8-3 and 8-4

def make_shirt(size = 'L', text = 'I love Python'):
    print(f"Your shirt's size is {size}, and its text is {text}")

make_shirt('M', 'Training to beat Goku')
make_shirt(text = 'Training to beat Vegeta', size = 'L')
make_shirt()
make_shirt(size = 'M')