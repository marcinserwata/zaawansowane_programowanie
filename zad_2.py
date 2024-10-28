class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, {self.marks}"

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}, {self.open_hours}, {self.phone}"

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name}, {self.last_name}, {self.hire_date}, {self.birth_date}, {self.city}, {self.street}, {self.zip_code}, {self.phone}"

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.library}, {self.publication_date}, {self.author_name}, {self.author_surname}, {self.number_of_pages}"

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Order: {self.employee}, {self.student}, {self.books}, {self.order_date}"

library1 = Library("Warsaw", "Marszalkowska", "00-001", "8:00-20:00", "123456789")
library2 = Library("Krakow", "Krakowska", "00-002", "9:00-21:00", "987654321")

book1 = Book(library1, "2020-01-01", "John", "Doe", 100)
book2 = Book(library1, "2020-02-01", "Jane", "Doe", 200)
book3 = Book(library1, "2020-03-01", "Jack", "Smith", 300)
book4 = Book(library2, "2020-04-01", "Jill", "Smith", 400)
book5 = Book(library2, "2020-05-01", "Jim", "Brown", 500)

employee1 = Employee("John", "Doe", "2020-01-01", "1990-01-01", "Warsaw", "Marszalkowska", "00-001", "123456789")
employee2 = Employee("Jane", "Doe", "2020-02-01", "1991-01-01", "Krakow", "Krakowska", "00-002", "987654321")
employee3 = Employee("Jack", "Smith", "2020-03-01", "1992-01-01", "Warsaw", "Marszalkowska", "00-001", "123456789")

student1 = Student("Student1", [50, 60, 70])
student2 = Student("Student2", [30, 40, 50])
student3 = Student("Student3", [10, 20, 30])

order1 = Order(employee1, student1, [book1, book2], "2020-01-01")
order2 = Order(employee2, student2, [book3, book4], "2020-02-01")

print(order1)
print(order2)


