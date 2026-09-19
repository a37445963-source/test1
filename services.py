from database import Database


class UserService:
    def __init__(self):
        self.db = Database()

    def get_user(self, user_id):
        return self.db.fetch_user(user_id)

    def create_user(self, name):
        return self.db.insert_user(name)
