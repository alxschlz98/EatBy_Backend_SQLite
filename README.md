# EatBy_Backend_SQLite

The Backend for the EatBy project. Currently, this is using SQLite, which will be changed to MySQL soon.

URLS:
[domain]/items/ - returns every item in the database.
[domain]/items/<item-id>/ - returns the item corresponding to that ID
  
For each item, the name, category, time until expiration in days, and item ID are all returned by the GET method
