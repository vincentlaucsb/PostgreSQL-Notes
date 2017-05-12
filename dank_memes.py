import psycopg2

import pg_password  # Your connection settings

def get_cursor():
    '''
    Connect to a PostgreSQL database and return a cursor with which 
    you can execute SQL queries
    '''
    
    with psycopg2.connect(dbname=PG_DATABASE, user=PG_USERNAME,
        host=PG_HOST, password=PG_PASSWORD) as \
            dank_memes_cant_melt_steel_beams:
        
        return dank_memes_cant_melt_steel_beams.cursor()
        
fux_with_me = get_cursor()

fux_with_me.execute('''SELECT AND_AMIL FROM THANK_YOU_THANK_YOU
                       WHERE ITS_LIT IS TRUE''')