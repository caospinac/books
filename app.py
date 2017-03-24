from sanic import Sanic
from sanic.response import html, redirect, text, json
from jinja2 import Environment, PackageLoader

# Own
# from server import Server
import utils


env = Environment(
    loader=PackageLoader("app", "templates"),
)

app = Sanic(__name__)
app.static("/static", "./static")

# server = Server()


@app.route("/")
async def root(request):
    return redirect(app.url_for('home'))


@app.route("/home")
async def home(request):
    template = env.get_template("home.html")
    html_content = template.render()
    return html(html_content)


@app.route("/sign-in", methods=["POST"])
async def sign_in(request):
    rq = request.form
    return json(rq)


@app.route("/sign-up", methods=["POST"])
async def sign_up(request):
    rq = request.form

    return json(rq)
    """
    name = rq.get("name")
    lastname = rq.get("lastname")
    email = rq.get("email")
    uname = rq.get("uname")
    pwd = rq.get("pwd")

    res = server.add_us(
        name=name, lastname=lastname,
        email=email, uname=uname, pwd=pwd,
    )
    return res
    """


@app.route("/user", methods=['GET'])
async def sign_in(request):
    uname = request.args["uname"][0] if "uname" in request.args else None
    email = request.args["email"][0] if "email" in request.args else None
    return json(server.us_exist(uname, email))


@app.route("/search", methods=["GET"])
async def search(request):
    q = request.args["s"][0]
    template = env.get_template("search.html")
    result = utils.search(q)
    html_content = template.render(
        data=result if result["items"] else 0
    )
    return html(html_content)


@app.route("/book", methods=["GET"])
async def book(self):
    return json(utils.book(request.args["id"][0]))


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000
    )
