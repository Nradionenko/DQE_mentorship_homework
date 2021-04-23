from pytest_jsonreport.plugin import JSONReport

plugin = JSONReport()


def pytest_json_modifyreport(json_report):
    """Exclude extra fields from json-report, leaving key properties only"""
    del json_report['environment']
    del json_report['collectors']
    del json_report['warnings']
    for property in json_report['tests']:
        del property['keywords']
        del property['call']
        del property['setup']
        del property['teardown']
