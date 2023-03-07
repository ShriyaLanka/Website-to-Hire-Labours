from sqlite3 import connect
from data import tables

def select(table_name):
    return run_query(f'SELECT * FROM {table_name};')

def insert(table_name, dict):
    keys = tables[table_name]['keys']
    values = [dict[key] for key in keys]
        
    return run_query(f"INSERT INTO {table_name} VALUES('" + "','".join(values) + "');")
    
def delete(table_name):
    run_query(f"DELETE FROM {table_name};")
        
def run_query(cmd):
    with connect('database.db') as con:
        cur = con.cursor()
        cur.execute(cmd)
        con.commit()
        return cur.fetchall()
    