class Student:
    amount_of_student = 0
    print("Hi")

    def __init__(self, scholarship=50):
        self.height = 170
        print("I am alive!")
        Student.amount_of_student += 1
        self.scholarship = scholarship
        self.scholarship += 100

print("*" * 10 + "Tom" + "_" * 10, sep="")
tom = Student(scholarship=100)
print(tom.amount_of_student)
print(f"scholarship Tom - {tom.scholarship}")

print("*" * 10 + "Bill" + "_" * 10, sep="")
bill = Student()
print(bill.amount_of_student)
print(f"scholarship Bill - {bill.scholarship}")

print(f"height Tom - {tom.height}")
print(f"height Bill - {bill.height}")
tom.height += 10
print('-' * 30)
print(f"height Tom - {tom.height}")
print(f"height Bill - {bill.height}")
