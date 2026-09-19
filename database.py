class Database:
    def fetch_user(self, user_id):
        return {
            "id": user_id,
            "name": "Test User",
        }

    def insert_user(self, name):
        return {
            "id": 100,
            "name": name,
        }
