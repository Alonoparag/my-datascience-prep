# #MongoClient
* class from pymongo
* .stats attribute return the stats of the specific object
* requires a uri string to instantiate, may recieve additional keywords
* after instantiating databases handles can be created via property or dictionary accessors on the client object
* collections handles are referened from the database object
* Collection specific operations like querying or updating documents are preformed on the collection object

# Basic Read operations
* find_one()
* find()
  * **iterating through cursors**
* Field projection and filtering
****
# Adding field projections
****
# Hnalding different query predicates