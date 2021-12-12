LOGGING = {
    'version': 1,
    'handlers': {
        'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'bookstore.log',
            'maxBytes': 4194304,  # 4 MB
            'backupCount': 10,
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'werkzeug': {
            'level': 'DEBUG',
            'handlers': ['file.handler'],
        },
    },
}





# import logging
# LOGGING = {
#     'version': 1,
#     'formatters': {
#         'default': {
#             'format': "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
#         },
#     },
#
#     'handlers': {
#         'file': {
#             'class': 'logging.FileHandler',
#             'formatter': 'default',
#             'filename': 'bookstore.log',
#         },
#     },
#     'loggers': {
#         'bookstore': {
#             'handlers': ['file', ],
#             'level': logging.DEBUG
#         },
#     },
# }


