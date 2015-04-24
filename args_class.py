import argparse

class Passyourcliargstome(object):

    def __init__(self):
        #here's how I got my args here
        self.foo = args.foo
        self.bar = args.bar
    def otherfunctionsthatdothings(self):
        print ("args inside of the main class:")
        print (self.foo)
        print (self.bar)

if __name__ == '__main__':
    #grab the arguments when the script is ran
    parser = argparse.ArgumentParser(description='Make things happen.')
    parser.add_argument('-f', '--foo', action='store_true', default=False, help='here be dragons')
    parser.add_argument('-b', '--bar', action='store_true', default=False, help='here be more dragons')

    args = parser.parse_args()
    print ("args outside of main:")
    print (args.foo)
    print (args.bar)

    #this was the part that I wasn't doing, creating an instance of my class.
    shell = Passyourcliargstome()
    shell.otherfunctionsthatdothings()
