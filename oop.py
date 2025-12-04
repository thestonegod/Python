#3rd Dec, 2025 Wednesday
#INHERITANCE
class person:
    def __init__(self,name,gender):
       self.name = name
       self.gen = gender

class student (person):
    def __init__(self, name, gender,guardian, programme):
        super().__init__(name, gender)
        self.guardian = guardian
        self.programme = programme

    def study(self):
        print(f"{self.name} is studying.")    

person1 = student(name="EL-SHADDAI", gender="Female", guardian="Miss Akomea")   
print(person1)     

# ENCAPSULATION
# ABSTRACTION
#POLYMORPHISM: Making objects respond to the same method call
