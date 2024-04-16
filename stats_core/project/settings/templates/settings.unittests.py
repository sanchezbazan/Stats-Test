DEBUG = True

LOGGING['formatters']['colored'] = {  # type: ignore # noqa: F821
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_green)s%(message)s',
}
LOGGING['loggers']['stats_core']['level'] = 'DEBUG'  # type: ignore # noqa: F821
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore # noqa: F821
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore # noqa: F821
