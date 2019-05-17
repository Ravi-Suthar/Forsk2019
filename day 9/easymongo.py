import pymongo

client = pymongo.MongoClient("mongodb://udaanravi:Ravi%401999@cluster0-shard-00-00-o7jg0.mongodb.net:27017,cluster0-shard-00-01-o7jg0.mongodb.net:27017,cluster0-shard-00-02-o7jg0.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.get_database('dbone')
records = db.collone
new_student = {
    'name': 'ram',
    'roll_no': 321,
    'branch': 'it'
}
records.insert_one(new_student)
print(list(records.find()))
