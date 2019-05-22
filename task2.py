import mysql.connector
import numpy as np


class List:

    def __init__ (self):
        self.numbers = np.array([])
        self.mydb = mysql.connector.connect(
                host="localhost",
                user = "root",
                passwd = "darya2310",
                database = "numbers_db")
        self.found_numbers = np.array([])
    
    def initialize_from_database(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM numbers")
        myresult = mycursor.fetchall()
        i=0
        for row in myresult:
            self.numbers = np.append(self.numbers,myresult[i][1])
            i=i+1      
        
    def add_number(self, phone_number):
        self.numbers = np.append(self.numbers,phone_number)
    
    def print_numbers_from_database(self):
        print("Phone numbers fom database:")
        print(self.numbers,end = " ")
    
    def find_numbers(self,input_number):    
        for i in self.numbers:
            if i[0:len(input_number)] == input_number:
                self.found_numbers = np.append(self.found_numbers,i)
    
    def print_found_numbers(self):
        print("\nFound numbers:")
        i = 0
        n = 10
        if(len(self.found_numbers) < n):
            n = len(self.found_numbers)
        while i < n:
            print(self.found_numbers[i], end=" ")
            i = i + 1


list_numbers = List()
list_numbers.__init__()
list_numbers.initialize_from_database()
list_numbers.print_numbers_from_database()

input_number  = input("\nPlease enter digits, from which the number starts:")

list_numbers.find_numbers(input_number)
list_numbers.print_found_numbers()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
