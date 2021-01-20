# Inserting Document AtlasUI
* click `Insert Document`
* evry mongodb document must have a unique_id value
* keep every document consistent as other documents in a collection by name and data type
* ****
## Inserting Documents using Shell
* use --drop in order to avoid duplicate id error
* findOne() returns a document, could also be queried
* `db.<collection>.insert(<document>)` inserts a document, could be dispatched with multiple values `db.<collection>.insert([<document1>, <document2>,...])`, adding `{"ordered": false}` as an argument will insert all of the documents with unique ids in an unordered way
****
# Updatin document using AtlasUI
* use edit(pencil)
* you can choose to nest an item into another mutable sequence
****
# Updating document using shell
* `updateOne()` updates one document that matches a given query
* `db.<collection>.updateOne(query, field)`
* `db.<collection>.updateOne(query, {"$inc": {"name": int, "name2": value2,...}})` increments value
* `db.<collection>.updateOne(query, {"$set": {"name": int, "name2": value2,...}})` set values
* `db.<collection>.updateOne(query, {"$push": {"name": int, "name2": value2,...}})` pushes an item to an array
* `updateMany()` upates all of the documents that matches a given query
****
# Deleting documents and collections
* `deleteOne(<query>)` - use only when given query is an _id
* `deleteMany(<query>)`
* `.drop()` removes a collection