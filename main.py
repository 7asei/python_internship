class Fields:
    employees = 0
    departments = 0


class Employee(Fields):
    def __init__(self, name, surname, age, job, salary, bonus):
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total_salary = salary + bonus
        Fields.employees += 1

    def apply_bonus(self, bonus):
        self.bonus = bonus
        print(self.name + " received: " + str(bonus) + "PLN bonus.")

    def total_salary(self):
        print(self.name + " received: " + str(self.total_salary) + "PLN.")


class Department(Fields):
    def __init__(self, name, users):
        self.name = name
        self.users = users
        Fields.departments += 1

    def emp_in_dep(self):
        print("Number of people in " + self.name + " department: " + str(self.users))

    def display_deps(self):
        print(dep1.name, dep2.name, dep3.name)


# data


emp1 = Employee("Janek", "Groszewski", 23, "Electrician", 4200, 0)
emp2 = Employee("Michał", "Zielonek", 21, "IT Specialist", 2700, 0)
emp3 = Employee("Roman", "Rak", 33, "Mechanic", 3800, 0)
emp4 = Employee("Ola", "Tracz", 50, "Receptionist", 3400, 0)
emp5 = Employee("Ewelina", "Mroczkowska", 21, "Recruiter", 4000, 0)

dep1 = Department("IT", 1)
dep2 = Department("HR", 2)
dep3 = Department("Workers", 2)


# tests


Employee.apply_bonus(emp3, 150)
Employee.apply_bonus(emp1, 300)
Employee.total_salary(emp1)
Department.emp_in_dep(dep1)
Department.display_deps(dep1)
print(vars(emp1))
print(vars(emp3))
print(vars(Fields))
