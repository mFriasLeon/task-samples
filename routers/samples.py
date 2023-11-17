"""Naralabs task: Managing samples.

This file contains APIs (GET,POST) to introduce and get samples

""" 

from genericpath import exists
from fastapi import APIRouter,HTTPException,status
from models.sample import SampleRequest, SampleResponse
from services.sample_service import sample_service
from decorators.exceptions import raise_exception_400,raise_exception_404
from bson import ObjectId

router = APIRouter(prefix="/samples")

#Introduce sample into the system
@router.post("/insert",status_code=201)
@raise_exception_400
async def insert_sample(sample:SampleRequest):
    
    new_sample = dict(sample)
    success = sample_service.insert_sample(new_sample)
    return success

# Fetch all sample given an sample name
@router.get("/get/{monitored_id}/{name}",status_code= 200)
@raise_exception_404
async def get_sample(monitored_id:int,name:str): 

    samples = sample_service.get_samples(monitored_id, name)
    samples_with_id = [{"id": str(sample.pop('_id')), **sample} for sample in samples]
    result = [SampleResponse(**sample) for sample in samples_with_id ]
    return result


@router.put("/update/{id}")
@raise_exception_404
async def update_sample(id: str, sample:SampleRequest):
    obj_id = ObjectId(id)
    sample_dict = dict(sample)
    result = sample_service.update_sample(obj_id,sample_dict)
    return result.modified_count

@router.delete("/delete/{id}", status_code=204)
@raise_exception_404
async def delete_sample(id: str):
    obj_id = ObjectId(id)
    success = sample_service.delete_sample(obj_id)
    return success






