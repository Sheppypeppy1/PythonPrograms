class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

    def marketing_boost(self,followers):
        self.followers += followers

user_1 = User("001","person1")
user_1.marketing_boost(100)

print(user_1.id,user_1.username,user_1.followers)