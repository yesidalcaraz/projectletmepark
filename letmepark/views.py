from django.http import HttpResponse
from pymongo import MongoClient


#MONGO_URI = 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false'
MONGO_URI = 'mongodb+srv://students_lanave:WrABgK5ruEZFpazG@mongodb-cluster-us-east-1-yuln1.mongodb.net/'

client = MongoClient(MONGO_URI)


#db= client['letmepark']
coleccion= db['parkings']
coleccion= db['bookingslite']

    