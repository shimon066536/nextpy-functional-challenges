class UnderAge(Exception):
    def __init__(self, age):
        self.age = age
    def __str__(self):
        return "Hi there your age %s and in (18 - %s) you can to invite the party" %self.age
    def get_age(self):
        return self.age

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print("Function Expected positive integer, and instead got %s." %str(e.get_age()))
    else:
        print("You should send an invite to " + name)

send_invitation("name", 17)
print(str(send_invitation("name", 17)))
send_invitation("name", 20)
print(send_invitation("name", 20))
