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
                print("\nAll right!\n")
                print(n)
            else:
                print("\n" + str(n))
            
    def combust(self):
        print("Your drummer has spontaneously combusted!")
        
class Band(object):
    def __init__(self):
        self.bandmates={}
    
    def hire(self):
        hiring=True
        hired=input("\nEnter name of new bandmate: ")
        while hiring:
            instrument=input("\nWhat do they play? 1) Guitar  2) Drums  3) Bass :     ")
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
                print("\nPlease enter 1,2, or 3!\n")
        
    def fire(self):
        print("\nCurrent members of your band: ")
        for k,v in self.bandmates.items():   # This needs to be cleaned up
            print(k + " is a " + str(v) + "\n")
        if input("Do you want to fire any members? ")[0].lower() in ["y"]:
            fired=input("\nWho do you want to fire? ")
            del self.bandmates[fired]
            print("\n" + fired + " has been fired! Your band now consists of: \n")
            for k in self.bandmates.keys():
                print(k)
            # The above line needs to be cleaned up
            
    def bandsolos(self, length):
        c=0
        d=0
        for v in self.bandmates.values():
            c+=1
            if isinstance(v,Drummer):
                d=1
                v.count()
                v.solo(length)
                v.combust()
            if c==len(self.bandmates) and d==0:
                print("\nYour band does not contain a drummer.  Musicians will start performing solos now!\n")
        for bname, instvalue in self.bandmates.items():
            if not isinstance(instvalue,Drummer):
                print("\nSolo for " + bname + ": ")
                instvalue.solo(length)
        
def main():
    bandname=input("What is the name of your band? ")
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
    print("\nLet's start playing!!")
    bandname.bandsolos(6)

if __name__ == "__main__":
    main()