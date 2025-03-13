### Blog Management System
A simple command-line-based blog management system built with Python and SQLAlchemy. This application allows users to create and manage blog posts and authors.

Features
Create Users: Add new authors to the system.

Create Posts: Add blog posts associated with a specific user.

View Users: List all users in the system.

View Posts: List all blog posts in the system.

Prerequisites
Before running the application, ensure you have the following installed:

Python 3.7 or higher

SQLAlchemy (pip install sqlalchemy)

Copy
pip install sqlalchemy
Usage
Run the application:

## python cli.py
Follow the on-screen menu to interact with the system:

1. Create User: Add a new user (author).

2. Create Post: Add a new blog post (requires a valid user ID).

3. View Users: List all users.

4. View Posts: List all posts.

5. Exit: Quit the application.

## File Structure
Copy
blog-management-system/
│
├── models.py          # Database models and setup
├── cli.py             # Command-line interface and application logic
└── blog.db            # SQLite database (created automatically)
Example Workflow
Create a User:

Copy
Select an option: 1
Enter username: JohnDoe
User JohnDoe created successfully!
Create a Post:

Copy
Select an option: 2
Enter user ID: 1
Enter post title: My First Post
Enter post content: This is the content of my first post.
Post created successfully!
View Users:

Copy
Select an option: 3
<User(id=1, name=JohnDoe)>
View Posts:

Copy
Select an option: 4
<Post(id=1, title=My First Post, author=1)>


