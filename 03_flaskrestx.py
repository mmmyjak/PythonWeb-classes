from flask import Flask, request
from flask_restx import Resource, Api, fields, reqparse, Model, marshal_with

app = Flask(__name__)
api = Api(app, doc='/docs')

parser = reqparse.RequestParser()
parser.add_argument('data', type=str, location='form')

todos = {
    "1": 'cos ciekawego',
}

model = Model('Model', {
    'data': fields.String
})

@api.route('/app')
class ToDoList(Resource):
    def get(self):
        return todos

    @marshal_with(model)
    @api.expect(parser)
    def post(self):
        todo_id = 100 + len(todos)
        arg = parser.parse_args()
        todos[todo_id] = arg['data']
        return {todo_id: todos[todo_id]}

@api.route('/<string:todo_id>')
class ToDoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        todos.pop(todo_id, None)
        return "deleted if existed"


if __name__ == '__main__':
    app.run(debug=True)