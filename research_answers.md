# Research Answers
**Hashem Barudi**
---
## Question 1
### Conduct research to understand how HTTP applications preserve the state of an application across multiple request-response cycles, especially concerning user authentication and session management. Write a paragraph describing your findings.

**HTTP is inherently a "stateless" protocol, meaning each request from a browser to a server is independent and has no memory of previous interactions. To preserve state (such as knowing a user is logged in), applications use **Sessions** and **Cookies**. When a user logs in, the server generates a unique "Session ID" and sends it to the browser as a Cookie. The browser automatically stores this cookie and sends it back to the server with every new request. The server then uses this ID to look up the user's specific data in its database or memory, effectively "remembering" the user across the session without requiring them to log in for every single page click.**

---
## Question 2
### Investigate and document the procedures for performing Django database migrations to a server-based relational database like MariaDB. Write a paragraph describing your findings.

**Migrating a Django project from SQLite to a server-based database like MariaDB involves three main steps: installation, configuration, and migration. First, the necessary database driver (usually `mysqlclient`) must be installed in the virtual environment so Python can talk to MariaDB. Second, the `DATABASES` setting in `settings.py` must be updated to change the `ENGINE` to `'django.db.backends.mysql'` and provide the connection details (Name, User, Password, Host, and Port) of the MariaDB server. Finally, running the command `python manage.py migrate` will connect to the new MariaDB server and generate all the necessary tables defined in the project's migration files, effectively recreating the schema in the new production database.**
