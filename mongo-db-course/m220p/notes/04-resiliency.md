# Pooling
* Connection pool is the cache of database connections, maintains that could be used when future requests to the database is required.
* helps to reduce the overhead of creating database connections. by default there are 100 connections in a pool, could be changed
****
# Robust Client Configuration
## Write Timeout
* wTimeout - Always use when using Write-Concern = 'Majority'
* Specific length according to system and requirements
* **ALWAYS HANDLE AND CONFIGURE serverSelectionTimeout ERRORS!!!**
  * monitors the health of the application stack
  * be aware of application recovery
****
# Writes with Error Handling
* Catch and handle errors, only fail what the app can't handle by itself, such as bad user input
****
# Principle of Least Privilege
* Engineer systems with the principle of least privilege in mind
* consider what kinds of users and what permission they will have
  * application users that log into the application itself
  * database users
    * administrative database users that can create indexes, import data and so on
    * application database users that only have privileges they require
****
# Change Stream
* Report changes at the collection level
* Accept pipelines to transform change events