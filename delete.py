import mysql.connector

class delete:
    def __init__(self):
        self.conn=mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "ROOT",
                database = "bank"
                )      

    def delete_data(self,table_name,cusid):
        cur=self.conn.cursor()
        print(table_name,cusid)
        cur.execute(f'delete from {table_name} where customerid={cusid}')  
        self.conn.commit()
        print('-----Data Deleted successfully-----')

        
