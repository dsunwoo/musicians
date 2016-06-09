class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Bang", "Bong", "Clink"])
    
    def count(self):
        for n in range (1,5):
            if n==1:
                print()
                print("All right!")
                print()
                print(n)
            else:
                print()
                print(n)
            
    def combust(self):
        print("Your drummer has spontaneously combusted!")
        
class Band(object):
    def __init__(self):
        self.bandmates={}
    
    def hire(self):
        hiring=True
        hired=input("Enter name of new bandmate: ")
        print()
        while hiring:
            instrument=input("What do they play? 1) Guitar  2) Drums  3) Bass :     ")
            print()
            if int(instrument)==1:
                self.bandmates[hired]=Guitarist()
                hiring=False
            elif int(instrument)==2:
                self.bandmates[hired]=Drummer()
                hiring=False
            elif int(instrument)==3:
                self.bandmates[hired]=Bassist()
                hiring=False
            else:
                print("Please enter 1,2, or 3!")
                print()
        
    def fire(self):
        print("Current members of your band: ")
        for k,v in self.bandmates.items():   # This needs to be cleaned up
            print(k + " is a " + str(v))
            print()
        if input("Do you want to fire any members? ")[0].lower() in ["y"]:
            print()
            fired=input("Who do you want to fire? ")
            print()
            del self.bandmates[fired]
            print(fired + " has been fired! Your band now consists of: ")
            print()
            for k in self.bandmates.keys():
                print(k)
            print()
            # The above line needs to be cleaned up
            
    def bandsolos(self, length):
        drumcheck="Drummer" in self.bandmates.values()
        print(drumcheck)
        for n in range (1,5):
            if n==1:
                print()
                print("All right!")
                print()
                print(n)
            else:
                print()
                print(n)
        
def main():
    bandname=input("What is the name of your band? ")
    print()
    bandname=Band()
    #hirenum=input("How many musicians do you want to hire? ")
    #try:
    #    int(hirenum)/1
    #except TypeError:
    #    print("Please enter an integer value")
    bandname.hire()
    bandname.hire()
    bandname.hire()
    bandname.fire()
    print("Let's start playing!!")
    bandname.bandsolos(6)

if __name__ == "__main__":
    main()