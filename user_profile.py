class UserProfile:

    def __init__(self, id, name, email):
        self.user_id = id
        self.user_name = name
        self.user_email = email

    def to_string(self):
        return self.user_id, self.user_name, self.user_email