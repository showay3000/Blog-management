### Blog Management System
A simple command-line-based blog management system built with Python and SQLAlchemy. This application allows users to create and manage blog posts and authors.

Features
Create Users: Add new authors to the system.

Create Posts: Add blog posts associated with a specific user.

View Users: List all users in the system.

View Posts: List all blog posts in the system.

Delete User: Delete a user and all their associated posts.

Delete Post: Delete a specific post by its ID.

Update Post: Update the title or content of an existing post.

Search Posts by User: View all posts by a specific user.

Prerequisites
Before running the application, ensure you have the following installed:

Python 3.7 or higher

SQLAlchemy: Install it using pip:

Run
pip install sqlalchemy
Installation

Run
pip install sqlalchemy
Usage
Run the application:

## python cli.py
Follow the on-screen menu to interact with the system:

1. Create User: Add a new user (author).

2. Create Post: Add a new blog post (requires a valid user ID).

3. View Users: List all users.

4. View Posts: List all posts.

5. Delete User: Delete a user and all their posts.

6. Delete Post: Delete a specific post by its ID.

7. Update Post: Update the title or content of a post.

8. Search Posts by User: View all posts by a specific user.

9. Exit: Quit the application.

File Structure
blog-management-system/
│
├── models.py          # Database models and setup
├── cli.py             # Command-line interface and application logic
├── README.md          # Project documentation (this file)
└── blog.db            # SQLite database (created automatically)
Example Workflow
Create a User:

option:1
Select an option: 1
Enter username: JohnDoe
User JohnDoe created successfully!
Create a Post:

option:2
Select an option: 2
Enter user ID: 1
Enter post title: My First Post
Enter post content: This is the content of my first post.
Post created successfully!
Update a Post:

option:7
Select an option: 7
Enter post ID to update: 1
Current title: My First Post
Enter new title (leave blank to keep current): Updated Title
Current content: This is the content of my first post.
Enter new content (leave blank to keep current): Updated content.
Post updated successfully!
Search Posts by User:

option:8
Select an option: 8
Enter user ID to search posts: 1
Posts by JohnDoe:
<Post(id=1, title=Updated Title, author=1)>
