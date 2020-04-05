import argparse
#this helps in executing python from terminal
# this is awesome

# this is not so awesome
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', action='store_true', help='shows_output')

##args = parser.parse_args()
####print(args)
##if args.output:
##    print('nonsense')

##parser.add_argument('--name', required=True)

parser.add_argument('name')
parser.add_argument('age')
args = parser.parse_args()
print(f'Hello {args.name}, you are {args.age}')
