from flask import Blueprint, Response,json, request
from service.list_se_service import ListService
from util.util import MyEncoder


app_listse=Blueprint("app_listse",__name__)
listse_service=ListService()

@app_listse.route("/listse/all")
def get_all_linked():
    return Response(status=200,
                    response=json.dumps(listse_service.get_all_linked(),cls=MyEncoder),
                    mimetypes="aplication/json")
@app_listse.route("/listse/invert")
def invert_list():
    return Response(status=200,
                    response=json.dumps(listse_service.invert()),
                    mimetypes="aplication/json")

@app_listse.route("/listse",methods=["POST"])
def create_pet_to_start():
    return Response(status=200,
                    response=json.dumps(listse_service.add_to_start(request.jason)),
                    mimetypes="aplication/json")








