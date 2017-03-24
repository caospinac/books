import os

from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import html, redirect, text, json
import pony.orm as P


DB_dir = os.path.abspath(os.path.dirname(__file__))
DB_uri = os.path.join(DB_dir, 'database.db')

DB = P.Database()

DB.bind(
    'postgres',
    user='postgres', password='pgsql',
    host='localhost', database='books'
)


class Us(DB.Entity):
    name = P.Required(str)
    lastname = P.Required(str)
    uname = P.PrimaryKey(str, 32)  # id
    email = P.Required(str, 60, unique=True)
    pwd = P.Required(str)
    books = P.Set('Book')


class Book(DB.Entity):
    book_id = P.PrimaryKey(str)
    users = P.Set(Us)


P.sql_debug(True)
DB.generate_mapping(create_tables=True)



class Server():
    """docstring for Server"""
    def __init__(self):
        pass

    @P.db_session
    def add_us(self, **kw):
        try:
            new = Us(**kw)
            P.flush()
            return new
        except Exception as e:
            raise e

    def auth_user(self, uname, pwd):
        in_pwd = DB.select(u.pwd for u in Us if u.uname == uname)
        return in_pwd is pwd

    @P.db_session
    def us_exist(self, uname=None, email=None):
        return bool(
            P.select(
                u for u in Us if u.uname == uname or u.email == email
            ).first()
        )

    def __del__(self):
        DB.disconnect()
