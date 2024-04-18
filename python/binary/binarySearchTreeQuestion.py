# QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure
# to manage profile information (username, name and email) for 100 million users. It should allow the following
# operations to be performed efficiently:
#
# Insert the profile information for a new user.
# Find the profile information of a user, given their username
# Update the profile information of a user, given their username
# List all the users of the platform, sorted by username
# You can assume that usernames are unique.


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)



aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
copy = User('vishal', 'Siddhant Mike', 'mikes@doe.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(copy)

user = database.find('copy')
print(user)






























