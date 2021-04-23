from ntpath import basename
import pytest

from connect import DB_CONNECT
from exec_utils.configloader import Config
from results.logging import Log

db = DB_CONNECT()
log = Log()
cnf = Config()

test_query = cnf.get_val("QUERIES", 'query_01')
expected_result = 10


def test_completeness():
    log.start_test(basename(__file__))
    try:
        actual_result = db.run_query(test_query)
        log.finish_test(basename(__file__))
        assert actual_result == expected_result
    except Exception as e:
        log.log_error(e)

