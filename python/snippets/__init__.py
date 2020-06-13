import loggin
import ConfigParser
import requests  # pip3 install requests


def simple_logger():
    """
    :return: logger
    """
    conf = {
        'logging': {
            'version': 1,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s %(levelname)s %(module)s  %(message)s'
                }
            },
            'handlers': {
                'stream': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'standard'
                },
            },
            'loggers': {
                '': {
                    'handlers': ['stream'],
                    'level': 'DEBUG'
                }
            }

        }
    }

    logging.config.dictConfig(conf)
    logger = logging.getLogger(__name__)

    return logger


def ini_parse_exceptions():
    """
    Parsing INI and exceptions
    :return: out
    """
    out = None
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(io.BytesIO(ini_file))
        out = config.get(section, option)
    except ConfigParser.NoSectionError:
        logging.error('No section {0} in file'.format(section))
    except ConfigParser.MissingSectionHeaderError:
        logging.error('No valid ini file')
    except ConfigParser.NoOptionError:
        logging.error('Option "{0}" not found in section {1}'.format(option, section))
    except Exception as e:
        logging.error('Unexpected error {0} {1} '.format(e.message, e.args))

    return out


def get_page(url, timeout):
    """
    Universal method for returning content of page
    :param url: url
    :param timeout: timeout
    :return: response if return code 200 or fail
    """
    result = {'data': None}
    exception_happened = True
    try:
        resp = requests.get(url, timeout=timeout)
    except Exception as e:
        logging.error('{}'.format(e))
    else:
        if resp.status_code != 200:
            logging.error('Http code not 200: {}'.format(resp.status_code))
        else:
            exception_happened = False
            result['result'] = 'ok'
            result['data'] = resp
    finally:
        if exception_happened:
            result['result'] = 'fail'
            logging.info('Function get_page params {}'.format(url))
    return result

def get_xml(xml_doc):
    """
    universal method that return xmltree object or error
    :param xml_doc: xml document
    :return:  xml object or error
    """
    result = {'data': None}
    exception_happened = True
    try:
        root = xml.etree.ElementTree.fromstring(xml_doc)
    except Exception as e:
        logging.error('{}'.format(e))
    else:
        exception_happened = False
        result['result'] = 'ok'
        result['data'] = root
    finally:
        if exception_happened:
            result['result'] = 'fail'
            logging.info('Function get_xml params {}'.format(xml_doc))
    return result
