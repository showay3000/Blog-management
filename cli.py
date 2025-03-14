
# cli
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

def delete_user():
    user_id = input("Enter user ID to delete: ")
    user = session.get(User, int(user_id))

    if not user:
        print("User not found!")
        return

    session.delete(user)
    session.commit()
    print(f"User {user.name} and all their posts deleted successfully!")

def delete_post():
    post_id = input("Enter post ID to delete: ")
    post = session.get(Post, int(post_id))

    if not post:
        print("Post not found!")
        return

    session.delete(post)
    session.commit()
    print(f"Post '{post.title}' deleted successfully!")

def update_post():
    post_id = input("Enter post ID to update: ")
    post = session.get(Post, int(post_id))

    if not post:
        print("Post not found!")
        return

    print(f"Current title: {post.title}")
    new_title = input("Enter new title (leave blank to keep current): ")
    print(f"Current content: {post.content}")
    new_content = input("Enter new content (leave blank to keep current): ")

    if new_title:
        post.title = new_title
    if new_content:
        post.content = new_content

    session.commit()
    print("Post updated successfully!")

def search_posts_by_user():
    user_id = input("Enter user ID to search posts: ")
    user = session.get(User, int(user_id))

    if not user:
        print("User not found!")
        return

    posts = user.posts
    if not posts:
        print(f"No posts found for user {user.name}.")
    else:
        print(f"Posts by {user.name}:")
        for post in posts:
            print(post)

def main():
    while True:
        print("\nBlog Management System")
        print("1. Create User")
        print("2. Create Post")
        print("3. View Users")
        print("4. View Posts")
        print("5. Delete User")
        print("6. Delete Post")
        print("7. Update Post")
        print("8. Search Posts by User")
        print("9. Exit")
        
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
            delete_user()
        elif choice == '6':
            delete_post()
        elif choice == '7':
            update_post()
        elif choice == '8':
            search_posts_by_user()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

# Entry point
if __name__ == "__main__":
    main()
