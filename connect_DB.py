#db연결
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:1234@cluster0.uibxg7e.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

#db 저장
doc = {
	'name':'bobby',
	'age':21
	}
db.users.insert_one(doc)

#db 꺼내기(한 개)
user = db.users.find_one({'name':'bobby'})

#db 꺼내기(리스트)
user_ilst = list(db.users.find({},{'_id':False}))


# 바꾸기
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기
db.users.delete_one({'name':'bobby'})
