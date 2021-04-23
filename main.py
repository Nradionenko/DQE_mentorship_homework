import pytest

from os.path import dirname, join, normcase
from pytest_jsonreport.plugin import JSONReport

from exec_utils.configloader import Config

cnf = Config()

plugin = JSONReport()
tests_folder = join(normcase(dirname(__file__)), 'tests')
results_path = join(normcase(dirname(__file__)), cnf.get_val("PATHS", "results_json"))

pytest_args = [tests_folder,
               "--disable-pytest-warnings",
               "-vv",
               "--json-report",
               f"--json-report-file={results_path}",
               "--json-report-indent=4"]

pytest.main(pytest_args)
