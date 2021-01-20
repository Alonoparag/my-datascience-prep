# MQL Operators
* preceded by $
* is usd for:
  * MQL operators
  * precedes Aggregation pipeline stages
  * Allows Access to Field Values
* **Update Operators**:
  * $inc
  * $set
  * $unset
* **Query Operators**
  * comparison
    * $eq and $neq
    * $gt
    * $lt
    * $gte
    * *lte
  * used in `{"field": <operator>:<value>}`
* **Logic Operators**
  * $or `{"field": {<operator>: [<value1>,<value2>,<value3>,<value4>]}}`
  * $nor `{"field": {<operator>: [<value1>,<value2>,<value3>,<value4>]}}`
  * $not
  * `$and` `{<operator>: [<value1>,<value2>,<value3>,<value4>]}}` also `{"field":{"$gt":value, "$lt": value}}` use when you need to inclue the same operator more than once in a query
* **Expressive Query Operator**
  * `$expr` - allows the use of aggregation expressions within the query language. allows us to use variables and conditional statements
  * allows to compare fields within the same document
    * `{$expr:{<expression>}}`
  * `$`(dollar sign):
    * denotes the use of an operator
    * addressses the field value
* **Array match**
  * `$elemMatch :{<field>:[<operator>]<value}`
****
# Operating on arrays:
* `<array>: {"$all": [<item1>, <item2>,...]}` return all arrays that contain given items 
* `<array>: {"$size": <int>}` return all arrays that list exactly given *int* items
****
# projection
* `{<query>}, {<projection>}` `{<field>:bool [1, 0]}`
* projection could only specify inclusion or exclusion

****
# Array Operators and sub-documents
* `.` lets access nested document fields, or array elements
* **$regex** allows regex operators