class Customer:
    def __init__(self, full_name, birthday, age, opccupation):
        self.name = full_name
        self.birthday = birthday
        self.age = age
        self.opccupation = opccupation



customer1 = Customer('Dave Small','19731025','50','Data scientist')
customer2 = Customer('Sandy Poole', '19930825', '30', 'Data engineer')
customer3 = Customer('Divya Patterson', '19780428', '45', 'Data analyst')
customer4 = Customer('Ash Wild', '19980105','35','Teacher')
customer5 = Customer('Andrea White', '20000320', '23','Dentist')

print(customer1.name)

customerList = [customer1, customer2, customer3, customer4, customer5]

for customer in customerList:
    print(customer.name)
    print(customer.birthday)
    print(customer.age)
    print(customer.opccupation)
