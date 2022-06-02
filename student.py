class Student: 
    school="Akirachix"
    def __init__(self,first_name,second_name,age,country):
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
        self.country=country
        
    def full_name(self):
        return f"Hello {self.first_name} {self.second_name} how is{self.country}" 
    
    
    def year_of_birth(self):
        year=2022-self.age
        return f"Hello{self.full_name} you were born in{self.year_of_birth}"
    
    def initials(self):
        initials=""
        full_name=self.name.split()
        for name in full_name:
            initials+=name[0].upper()
            return
    
    


        