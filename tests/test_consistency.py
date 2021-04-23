from ntpath import basename

from connect import DB_CONNECT
from exec_utils.configloader import Config
from results.logging import Log

db = DB_CONNECT()
log = Log()
cnf = Config()

test_query = cnf.get_val("QUERIES", 'query_02')
expected_result = 'President'


def test_consistency():
    log.start_test(basename(__file__))
    try:
        actual_result = db.run_query(test_query)
        assert actual_result == expected_result
        log.finish_test(basename(__file__))
    except Exception as e:
        log.log_error(e)

