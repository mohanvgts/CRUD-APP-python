from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from . import db
from bson.json_util import dumps
from bson.objectid import ObjectId
database = db.client['CRUD']
collection = database['user']

@csrf_exempt
#createuser
def createUser(req):
    data = json.loads(req.body)
    user = collection.insert_one(data)
    return JsonResponse({'message': 'User created successfully'})
#get all user list
def getUser(req):
    user = list(collection.find({}))
    return JsonResponse(json.loads(dumps(user)),safe=False)

@csrf_exempt
#get user by ID
def getuserByID(req,pk):
    user = collection.find_one({'_id':ObjectId(pk)})
    return JsonResponse(json.loads(dumps(user)),safe=False)


@csrf_exempt
#update user details
def updateUser(req,pk):
    data = json.loads(req.body)
    collection.update_one({'_id':ObjectId(pk)},{'$set':data})
    return JsonResponse({'message':'user details updated successfully'})

@csrf_exempt
#Delete user
def deleteUser(req,pk):
    collection.delete_one({'_id':ObjectId(pk)})
    return JsonResponse({'message':'user deleted....!!!'})