# Document
* a way to organize data as a set of field-value pairs.
* collection an organized store of documents in MongoDB, usually with common fields between documents
# Atlas
* fully managed database with mongo db at core
* can deploy clusters
* replica set - set of connected mongo db datasets used to store data
* instance a single machine used to store data
* Manage cluster creation
* Run and maintain database deployment
* Use cloud service provider
******
# Storing Data
* json notation
* may also contain sub-documents
* stores in bson.
***
# Import Export
* mongodump - export in bson, needs uri
* mongoexport - export in jason, needs uri, collection and output name
* mongorestore - opposite to mongodump- needs uri and drop removes existing database
* mongoimport, needs uri, and drop drop removes existing dataset
***
# Data Exploration
* namespace - concatenation of database name and collectio name
* filter with a json formatted {"name":"value"}
## Data Exploration in shell
* find()
* Admin - default database:
  * keeps track of existing users
* query data with `show dbs`
* `use <database>` is indicating which database should be used
* `show collections` will show collection
* `find({"key":"value"})` is used to query for a specific item as `db.<collections>.find({"key":value})`
* `it` allow to iterate through a cursor (a pointer to a result set of a query). a pointer is a direct address to a memory location
* `db.<collections>.find({"key":value}).count()` counts the number of similar items inside a collection
* `db.<collections>.find({"key":value}).pretty()` returns the document that match the given query formatted for ease of reading
* `db.<collections>.find()` returns the first 20 documents from a collection