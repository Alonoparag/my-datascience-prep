# Mongodb URI
* **URI** **U**niform **R**esource **I**dentifier
  * used to define the connections between applications and databases, telling a driver the hostname and port of a database, also username and passwords.
  * examples:

      mongodb://username:password@
      cluster0-shard-00-00-m220-lessons-mcxlm.mongodb.net:27017,
      cluster0-shard-00-01-m220-lessons-mcxlm.mongodb.net:27017,
      cluster0-shard-00-02-m220-lessons-mcxlm.mongodb.net:27017/mflix

  * must be explicit of the hostname of each of the clusters
  * could also be an srv string:
    * `mongodb+srv://<username>:<password>@<host>/<database>`
    * `<prefix srv record>://<authentication records>@<host>/<database>`
    * the advantage of srv is that it keeps track of servers in the cluster
    * the database part contains the authenticaion of the user
    * options could be specified with a query `?<option>=<value>` string after the database
****
# Setting up A
* 
****