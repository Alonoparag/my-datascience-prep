# Aggregation Framework

    db.<collection>.aggregate([
                <operator> {[<operator>]<field>:<value>},
                <operator> {[<operator>]<field>:<value>},
                ...
    ])
* order of actions in the pipeline matters
* Non- filtering stages do not modify the original data. Instead they work with the data in the cursor
## Operators
* **$group**
  * takes incoming stream of data and siphons it into multiple distinct reservoirs.
  * syntax:

    { $group:
        {
            _id: <expression>, //Group By Expression
            <field1>: {<accumulator1>: <expression1>},
            ...
        }
    }
****
# Cursor Methods
* Applied to the results that live in the cursor
* **sort()**
  * can use int increasing or decresing `-1` order
* **limit()**
  * always exectured after sort, regardless of location
****
# Indexes
* special data structure that stores a small portion of the collection's data set in an easy to traverse form
* helps to improve sorting significantly
* can have a single or compound index(on multiple fields) `createIndex({<field>: 1,...})`
# Data Modeling
* a way to organize fields in a document to support your application performance and querying capabilities
* **Data is stored in the way that it is used**
# Upsert
* `db.collection.updateOne({<query to locate>}, {<update>}, {upsert:true})`
* does an update if there's an document that matches the query criteria. the insert will happen otherwise
* be mindful about the updated document
  * is `{<update>}` enough to create a new document?
  * Will the document have the same or similar form to other documents in the collection
  * when using upsert, make sure that the passed values will be enough to create a new document in similar form to other documents in the collection