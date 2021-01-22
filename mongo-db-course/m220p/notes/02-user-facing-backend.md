# Cursor methods and Aggregation Methods
**COUNTING IN THE CURSOR IS DEPRECATED, COUNTING SHOULD BE PREFORMED INSIDE A PIPELINE**
* **Limiting**
  * limit() ("$limit" in pipeline)
    * Limit the number of results, int argument is required
* **Sorting**
  * sort(<field>:ASCENDING\DESCENDING(1,-1)) or `$sort:{<field>:1,-1}`
  * sorting on mulltiple keys takes an array of tuples
  * sorting on multiple keys in the pipeline takes a set of items
* **Skpping**
  * better done after sorting
  * cursor:
    * `skip(int)`
  * pipeline:
    * `{"$skip": int}`
****
# Aggregation Methods
* pipepline, an array of operators
* "$limit"
*** **
# Aggregation
* Aggregation is a pipeline
  * Pipelines are comnposed of stages, broad units of work.
  * Within stages, expressions are used to specify individual units of work.
* Expressions are functions
* Add:
  * `{"\$add":["\$a","\$b",...]}`

****
# Write Concerns
* `w: 0\int\'majority'`
* write_concern
* 1 is defualt
****
# Updates
* update_one
  * 
* update_many
* ****
# Joins
* Join two collections of data
  * movies and comments
  * use new expressive `$lookup`
  * Build aggregation in Compass, and then export to language
* in pipeline:

    {
        from: <collection>
        let: {'id':'$_id'}, #the collection to join from
        pipeline: [ #has access to fields inside the 'from' value collection. doesn't has access to the movies (collection on which the pipeline is applied), unless specified in let($$variable)
            {'$match':
                {'\$expr': {'\$eq':['\$movie_id','$$id']}}
            }
        ]
    }