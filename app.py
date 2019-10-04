from Terminal_blog.database import Database
from Terminal_blog.menu import Menu
from Terminal_blog.models.post import Post

Database.initialize()

menu = Menu()
menu.run_menu()