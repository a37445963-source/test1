from services import UserService
from utils import format_user


def main():
    service = UserService()  
    user = service.get_user(42)
    print(format_user(user))


if __name__ == "__main__":
    main()
