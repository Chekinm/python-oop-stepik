class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, route_cls):
        self.path = path
        self.route_cls = route_cls

    def __call__(self, func):
        self.route_cls.add_callback(self.path, func)


@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'

@Callback('/add_post', Router)
def add_post():
    return '<h1>Add post</h1>'

route = Router.get('/')
add_post = Router.get('/add_post')
res = add_post()
print(res)
if route:
    ret = route()
    print(ret)


