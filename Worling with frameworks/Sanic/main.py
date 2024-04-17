from sanic import Sanic
from sanic import response


app = Sanic("My_first_Sanic_App")


@app.route('/')
def index(request):
    return response.text("Hi World")


app.run(host="0.0.0.0", port=8000, debug=True)
