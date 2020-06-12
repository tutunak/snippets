import loggin
import ConfigParser


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
    :return: opt
    """
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