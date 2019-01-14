import json
from datetime import datetime

from flask import request, Response
from flask_restplus import Resource, Namespace

from .main import db
from .models.transaction import TxHist

ns_app = Namespace("app")


def json_render(data:dict) -> Response:
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, status=200, mimetype='application/json')


@ns_app.route("/hello")
class Hello(Resource):
    def get(self):
        result = {}
        result['message'] = 'Hello'
        return json_render(result)


@ns_app.route("/txinfo")
class TransactionInfo(Resource):
    def get(self):
        rows = db.session.query(TxHist).limit(100)
        res = []
        for row in rows:
            res.append(row.to_json())
        return json_render(res)


    def post(self):
        print("Request data: {}".format(request.data))

        trans = TxHist()
        trans.method = getattr(request, "method")
        trans.resource = getattr(request, "url")
        trans.tx_date = datetime.utcnow()
        trans.remote_addr = getattr(request, "remote_addr")
        trans.agent = request.headers.get('User-Agent')

        # data = getattr(request, "data")
        # json = data.decode("utf-8")
        # if json is not None and len(json) > 0:
        #     trans.data = json

        db.session.add(trans)
        db.session.commit()
        result = {}
        result['message'] = 'Success.'
        result['id'] = trans.id
        return json_render(result)



@ns_app.route("/txinfo/<int:id>")
class TransactionInfoSearch(Resource):
    def get(self, id):
        res = db.session.query(TxHist).filter(TxHist.id == id).first()
        print(res)
        if res is not None:
            print(res, " is not none")
            return json_render(res.to_json())
