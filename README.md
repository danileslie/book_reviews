# Reviews
## Video Demo:  https://www.youtube.com/watch?v=9NQwy-oIqvg
### Description

<p>This was made as my CS50 final project, a book review site.</p>

<p>You are able to register, with the information being stored in a database. You can log in, make edits within your account, and log out.</p>

<p>In the application, you are free to search up books, add them to your booklist, and add a review. Once complete, the review is visible on the review page.
The review can be deleted from the account, without deleting the book. If the book entry is deleted from the account, any reviews associated with the review is also deleted from the account.</p>

<p>The app.py page contains all of the major functions, tied to logging in, logging out, registering a book, deleting a review, etc.</p>

<p>The information is stored in a database, reviews.db, which records the registered users, their booklist, and their reviews.</p>

### Pages

#### Register

<p>The register screen is simple, with fields for the username, password, and password confirmation. The site will throw an error if the username already exists. It will also throw an error if the passwords don't match.
On success, the information is stored in a databse, with a hashed password in place of the plaintext one.</p>

#### Login

<p>The login page let's you log in with the credentials made during the registration stage, and the redirect will take you to the homepage, which will either be empty, or contain your booklist.</p>

<p>I considered making the home page the one that had the reviews on it, or the lookup page, but opted for the page that let the user know what they already had tied to their account.</p>

#### Lookup

<p>The lookup page lets you look up books, displaying their name, title, and the option to add it to the booklist.</p>

#### Booklist

<p>The booklist page lets you do a few things: add a review, edit an axisting review, delete the review, and delete the book entry from the account entirely. You can only have one review per book at a time. Adding any more will overwrite the review.</p>

#### Reviews

The reviews page lets you view the reviews

#### Things To Improve

* Let users delete their account
* Update layout 
* Show currently submitted review before editing (on booklist page)
* Add fuzzy search 
* Book lookup includes descriptions and updated images





**Written with HTML, Javascript, and Python.**