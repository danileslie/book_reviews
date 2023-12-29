# Reviews
## Video Demo:  https://www.youtube.com/watch?v=9NQwy-oIqvg
### Description

This was made as my CS50 final project, a book review site.

You are able to register, with the information being stored in a database. You can log in, make edits within your account, and log out.

In the application, you are free to search up books, add them to your booklist, and add a review. Once complete, the review is visible on the review page.
The review can be deleted from the account, without deleting the book. If the book entry is deleted from the account, any reviews associated with the review is also deleted from the account.

The app.py page contains all of the major functions, tied to logging in, logging out, registering a book, deleting a review, etc.

The information is stored in a database, reviews.db, which records the registered users, their booklist, and their reviews.
 The users table stores only the username and the hashed password, along with a user_id that is used throughout the other tables

### Pages

#### Register

The register screen is simple, with fields for the username, password, and password confirmation. The site will throw an error if the username already exists. It will also throw an error if the passwords don't match.
On success, the information is stored in a databse, with a hashed password in place of the plaintext one.

#### Login

The login page let's you log in with the credentials made during the registration stage, and the redirect will take you to the homepage, which will either be empty, or contain your booklist.

I considered making the home page the one that had the reviews on it, or the lookup page, but opted for the page that let the user know what they already had tied to their account.

#### Lookup

The lookup page lets you look up books, displaying their name, title, and the option to add it to the booklist.

#### Booklist

The booklist page lets you do a few things: add a review, edit an axisting review, delete the review, and delete the book entry from the account entirely. You can only have one review per book at a time. Adding any more will overwrite the review.

#### Reviews

The reviews page lets you view the reviews

#### Things To Improve

* Let users delete their account
* Update layout 
* Show currently submitted review before editing (on booklist page)
* Add fuzzy search to lookup page
* Book lookup includes descriptions and updated images
* Book lookup includes author on the page
* Review textbox includes title of book being reviewed

## About CS50
CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.

- Where I get CS50 course?
https://cs50.harvard.edu/x/2023/



**Written with HTML, Javascript, and Python.**