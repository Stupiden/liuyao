class Mammals:
    def __init__(self):
        self.members = ['Lion', 'Elephant', 'Cat']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s' % member)