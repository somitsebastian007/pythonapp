# app.py
def greet(name):
    return f"Hello, {name}! Welcome to DevOps Training"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))