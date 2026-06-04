from database.pymongo_db import job_collection
from bson import ObjectId

def create_job(company_name,role,status,priority,notes,application_date,job_link,location):
   job = {
    "company_name": company_name,
    "role": role,
    "status": status,
    "priority": priority,
    "notes": notes,
    "application_date": str(application_date),
    "job_link": job_link,
    "location": location
   }
   result = job_collection.insert_one(job)
   return result.inserted_id

def get_all_jobs():
   jobs = list(job_collection.find())
   return jobs

def get_job_stats():

    jobs = list(job_collection.find())

    total = len(jobs)

    applied = sum(
        1 for job in jobs
        if job.get("status") == "Applied"
    )

    interview = sum(
        1 for job in jobs
        if job.get("status") == "Interview"
    )

    accepted = sum(
        1 for job in jobs
        if job.get("status") == "Accepted"
    )

    return {
        "total": total,
        "applied": applied,
        "interview": interview,
        "accepted": accepted
    }
def update_job_status(job_id,new_status):
   job_collection.update_one(
      {"_id":ObjectId(job_id)},
      {
         "$set":{
            "status":new_status

         }
      }
   )

def delete_job(job_id):
   job_collection.delete_one(
      {"_id":ObjectId(job_id)}
   )
def search_job(search_text):
   return list(
      job_collection.find(
         {"company_name":{
            "$regex":search_text,
            "$options":"i"
         }}
      )
   )
