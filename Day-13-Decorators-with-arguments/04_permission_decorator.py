def require_role(required_role):
    def decorator(func):
        def wrapper(actual_role):
            if required_role.lower() == actual_role.lower():
                func()
            else:
                print("Access denied")

        return wrapper
    return decorator


@require_role("admin")
def delete_user():
    print("User deleted")


role = input("Enter role: ")
delete_user(role)