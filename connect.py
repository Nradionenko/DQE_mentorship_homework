import pyodbc
from os.path import dirname, join, normcase

# from exec_utils.configloader import Config
# from results.logging import Log

# cnf = Config()
# log = Log()

driver = '/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so'

class DB_CONNECT:
    @staticmethod
    def connect():
        try:
#             server_name = cnf.get_val("DB", "server")
#             db_name = cnf.get_val("DB", "db_name")
            with pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost, 1433;DATABASE=TRN;UID=test;') as conn:
                curs = conn.cursor()
#             log.connected(server_name, db_name)
            return curs
        except pyodbc.Error as e:
            print(e)
#             log.log_error(e)

#     def read_query(self, query_file):
#         main_dir = normcase(dirname(__file__))
#         query_file_path = join(main_dir, query_file)
#         try:
#             with open(query_file_path, "r") as f:
#                 log.query_start(query_file)
#                 return f.read()
#         except FileNotFoundError as e:
#             log.log_error(e)

#     def run_query(self, query_file):
#         try:
#             curs = self.connect()
#             query = self.read_query(query_file)
#             curs.execute(query)
#             result = curs.fetchall()[0][0]
#             for i in result:
#                 print(i)
#             log.query_finish(query_file)
#             curs.close()
#             return result
#         except AttributeError:
#             log.log_error("Couldn't connect to the server")
#         except pyodbc.ProgrammingError as p:
#             log.log_error(p)


d = DB_CONNECT()
curs = d.connect()
curs.execute('select * from hr.regions')
result = curs.fetchall()
for i in result:
    print(i)
