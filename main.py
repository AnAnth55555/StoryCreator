import random
traits = []
names = []
jobs = []
with open('traits.txt', 'r') as f:
    traits = f.read().split("\n")
with open('names.txt', 'r') as f:
    names = f.read().split("\n")
with open('jobs.txt', 'r') as f:
    jobs = f.read().split("\n\n")
    
    
class Character:
    def __init__(self):
        self.name = random.choice(names)
        self.trait1 = random.choice(traits)
        self.trait2 = random.choice(traits)
        self.job = random.choice(jobs)
        self.known_people = {}
    def __str__(self):
        return f'{self.name}, {self.trait1} and {self.trait2}, {self.job}, {self.print_known_people()} '
        
    def meet(self, c):
        # adds person to a known person list and randomly generates a score from -10 to 10 of how much the person is liked
        self.known_people[c] = random.randint(-10,10)
        return self
        
    def print_known_people(self):
        sum = ""
        for p in list(self.known_people.keys()):
            sum+=p.name+"("+self.scale(self.known_people[p]) + "), "
        return "Knows: "+ sum
        
    def scale(self,i):
        match i:
            case -10:
                return "Absolutley Hate"
            case -9:
                return "Cannot Stand"
            case -8:
                return "Loath"
            case -7:
                return "Detest"
            case -6:
                return "Hate"
            case -5:
                return "Resents"
            case -4:
                return "Strongly Dislike"
            case -3:
                return "Avoids"
            case -2:
                return "Tolerates"
            case -1:
                return "Dislikes a little"
            case 0:
                return "Doesn't Know"
            case 1:
                return "Seen"
            case 2:
                return "Acquaintance"
            case 3:
                return "Hangs Out With"
            case 4:
                return "Likes"
            case 5:
                return "Friends"
            case 6:
                return "Understands"
            case 7:
                return "Close Friends"
            case 8:
                return "Best Friends"
            case 9:
                return "Deeply Cares About"
            case 10:
                return "Solemates"
            case _:
                return str(i)
def main():
    people = []
    for i in range(50):
        people.append(Character())
    
    for j in range(len(people)):
        for k in range(len(people)):
            people[k].meet(people[j])
        
    for l in people:
        print(f'{l.name} the {l.job}, {l.trait1} {l.trait2}')
        for c in list(l.known_people.keys()):
            print(f'Why does {l.name} {l.scale(l.known_people[c])} {c.name}?')
        print()

if __name__ == '__main__':
    main()


