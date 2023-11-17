
from database.connection import db_connection, naralabs_db
from bson import ObjectId

class SampleService():

    def __init__(self,db_connection):
        self.db = db_connection

    
    def insert_sample(self,new_sample:dict) -> bool:
        result_insert = naralabs_db.samples.insert_one(new_sample)
        return result_insert.acknowledged

    def get_samples(self,monitored_id:int, sample_name:str):
        samples = naralabs_db.samples.find({"monitored_id": monitored_id,"sample_name": sample_name })
        return samples

    def delete_sample(self,id:ObjectId)->bool:
        sample_deleted = naralabs_db.samples.delete_one({"_id": id})
        return sample_deleted.acknowledged

    def update_sample(self,id:ObjectId,sample:dict):
        result = naralabs_db.samples.update_one(
        {"_id": id},
        {"$set": sample}
        )
        return result


sample_service = SampleService(naralabs_db)