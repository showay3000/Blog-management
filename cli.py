# cli.py

from models import session, User, Post

def create_user():
    name = input("Enter username: ")
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User {name} created successfully!")

def create_post():
    user_id = input("Enter user ID: ")
    user = session.get(User, int(user_id))

    if not user:
        print("User not found!")
        return

    title = input("Enter post title: ")
    content = input("Enter post content: ")

    post = Post(title=title, content=content, author=user)
    session.add(post)
    session.commit()
    print("Post created successfully!")

def view_users():
    users = session.query(User).all()
    for user in users:
        print(user)

def view_posts():
    posts = session.query(Post).all()
    for post in posts:
        print(post)

def main():
    while True:
        print("\nBlog Management System")
        print("1. Create User")
        print("2. Create Post")
        print("3. View Users")
        print("4. View Posts")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            create_post()
        elif choice == '3':
            view_users()
        elif choice == '4':
            view_posts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

# Entry point
if __name__ == "__main__":
    main()