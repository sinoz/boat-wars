import psycopg2

# The url for each connection
url = "host='localhost' dbname='boat_wars' user='postgres' password='sqlpass'"

# Establishes a new connection to execute the given query. Returns nothing.
def execute(query):
    establishedConnection = psycopg2.connect(url)
    connCursor = establishedConnection.cursor()
    connCursor.execute(query)
    establishedConnection.commit()
    establishedConnection.close()

# Establishes a new connection to execute the given query. Returns the
# results from the given query. This should not be used for queries that
# return no result such as INSERT or UPDATE queries. Prefer execute() for
# INSERT and UPDATE queries.
def query(query):
    establishedConnection = psycopg2.connect(url)
    connCursor = establishedConnection.cursor()

    connCursor.execute(query)
    results = connCursor.fetchall()

    establishedConnection.close()
    return results