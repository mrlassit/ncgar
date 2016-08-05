import os
import sys

from pymongo import MongoClient

# add root directory to python path
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))

from config.config import Config
from dao import Dao

DATABASE_NAME = config.get_db_name()
TOURNAMENTS_COLLECTION_NAME = 'tournaments'
PENDING_TOURNAMENTS_COLLECTION_NAME = 'pending_tournaments'
mongo_client = MongoClient(host=config.get_mongo_url())

tournaments_col = mongo_client[DATABASE_NAME][TOURNAMENTS_COLLECTION_NAME]
pending_tournaments_col = mongo_client[DATABASE_NAME][PENDING_TOURNAMENTS_COLLECTION_NAME]

tournaments = tournaments_col.find()
pending_tournaments = pending_tournaments_col.find()

tournaments_col.update({},{"$set": {"url": None}})
pending_tournaments_col.update({}, {"$set": {"url": None}})
	
for t in tournaments:	
	if(t['type'] =='challonge' and t['raw'] != ""):
		print t['type'], t['name'], "yes"
		tournaments_col.update({"_id": t["_id"]},{"$set": {"url": t['raw']['tournament']['tournament']['full_challonge_url']}})
	else:
		print t['type'], t['name']
		tournaments_col.update({"_id": t["_id"]},{"$set": {"url": None}})

for pt in pending_tournaments:	
	if(pt['type'] == 'challonge' and pt['raw'] != ""):
		tournaments_col.update({"_id": pt["_id"]},{"$set": {"url": pt['raw']['tournament']['tournament']['full_challonge_url']}})
	else:	
		pending_tournaments_col.update({"_id": pt["_id"]},{"$set": {"url": None}})