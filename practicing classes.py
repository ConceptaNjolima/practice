class student():
    def __init__(self,first_name,last_name,B_number):
        self.first_name=first_name
        self.dorm=last_name
        self.B_number=B_number
    def __str__(self):
        """
        Converts to string
        :return: The fisrt and last names and the B_number of student
        """
        return "{0},{1},{2}".format(self.first_name, self.dorm, self.B_number)
    def enter_dorm(self,dorm):
        if self.dorm=="Pearson":
            return self.dorm

concepta=student("Njolima","Pearson","B00759099")
print(concepta)
