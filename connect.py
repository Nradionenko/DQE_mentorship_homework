import pyodbc
from os.path import dirname, join, normcase

from exec_utils.configloader import Config
from results.logging import Log

cnf = Config()
log = Log()


class DB_CONNECT:
    @staticmethod
    def connect():
        try:
            server_name = cnf.get_val("DB", "server")
            db_name = cnf.get_val("DB", "db_name")
            with pyodbc.connect('Driver={SQL Server};'
                                  f'Server={server_name};'
                                  f'Database={db_name};'
                                  'Trusted_Connection=no;') as conn:
                curs = conn.cursor()
            log.connected(server_name, db_name)
            return curs
        except pyodbc.Error as e:
            log.log_error(e)

    def read_query(self, query_file):
        main_dir = normcase(dirname(__file__))
        query_file_path = join(main_dir, query_file)
        try:
            with open(query_file_path, "r") as f:
                log.query_start(query_file)
                return f.read()
        except FileNotFoundError as e:
            log.log_error(e)

    def run_query(self, query_file):
        try:
            curs = self.connect()
            query = self.read_query(query_file)
            curs.execute(query)
            result = curs.fetchall()[0][0]
            log.query_finish(query_file)
            curs.close()
            return result
        except AttributeError:
            log.log_error("Couldn't connect to the server")
        except pyodbc.ProgrammingError as p:
            log.log_error(p)


# d = DB_CONNECT()
# d.connect()
# d.run_query(cnf.get_val("QUERIES", 'query_01'))
