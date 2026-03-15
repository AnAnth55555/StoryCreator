import random
traits = []
names = []
jobs = []
settings = []
with open('traits.txt', 'r') as f:
    traits = f.read().split("\n")
with open('names.txt', 'r') as f:
    names = f.read().split("\n")
with open('jobs.txt', 'r') as f:
    jobs = f.read().split("\n\n")
with open('settings.txt', 'r') as f:
    settings = f.read().split("\n")

    
def randomize_chart(people,f):
    c = random.choice(people)
    match random.randint(0,4):
        case 0:
            c.means = not c.means
            f.write(input(f'What caused this change in {c.name} means from {not c.means} to {c.means}'))
        case 1:
            c.motive = not c.motive
            f.write(input(f'What caused this change in {c.name} motive from {not c.motive} to {c.motive}'))
        case 2:
            c.opportunity = not c.opportunity
            f.write(input(f'What caused this change in {c.name} opportunity from {not c.opportunity} to {c.opportunity}?'))
        case 3:
            c.evidence = not c.evidence
            f.write(input(f'What caused this change in {c.name} evidence from {not c.evidence} to {c.evidence}?'))



def print_chart(people,f):
    f.write("Suspects|Means|Motive|Opportunity|Evidence\n")
    for h in people:
        f.write(f'{h.name:<20}|{h.means}|{h.motive}|{h.opportunity}|{h.evidence}\n')    
        
class Character:
    def __init__(self):
        self.name = random.choice(names)
        self.trait1 = random.choice(traits)
        self.trait2 = random.choice(traits)
        self.job = random.choice(jobs)
        self.known_people = {}
        self.motive = bool(random.getrandbits(1))
        self.means = bool(random.getrandbits(1))
        self.opportunity = bool(random.getrandbits(1))
        self.evidence = bool(random.getrandbits(1))
    def __str__(self):
        return f'{self.name}, {self.trait1} and {self.trait2}, {self.job}'
        
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
    for i in range(5):
        people.append(Character())
    
    for j in range(len(people)):
        for k in range(len(people)):
            people[k].meet(people[j])
        
    with open('cast.txt', 'w') as f:
        f.write(f'Story takes place in {random.choice(settings)} with \n')
        for r in people:
            f.write(f'{r}\n')
        f.write(f'{random.choice(people).name} was murdered by whom and how?')
        f.write(input(f'{random.choice(people).name} was murdered by whom and how?'))
    with open('relationships.txt', 'w') as f:
    	for l in people:
        	f.write(f'\n{l.name} the {l.job}, {l.trait1} {l.trait2}\n')
        	for c in list(l.known_people.keys()):
                    f.write(f'Why does {l.name} {l.scale(l.known_people[c])} {c.name}?\n')
                    f.write(input(f'Why does {l.name} {l.scale(l.known_people[c])} {c.name}?\n'))

    with open('chart.txt.', 'w') as f:
        print_chart(people,f)
        for h in range(len(people)):
            randomize_chart(people,f)
            print_chart(people,f)

if __name__ == '__main__':
    main()


