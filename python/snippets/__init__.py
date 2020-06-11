import loggin


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