import logging


class ProLogRecord(logging.LogRecord):
    """
    This class is used to create a custom log record, which can be used to store additional information.
    The ProLogRecord class inherits from the LogRecord class in the logging module.
    The reason for using a custom log record is so that it can automatically provide information for the
    log filters, which are used to determine if a log record should be processed by a handler.
    """

    def __init__(self, *args, **kwargs):
        super(ProLogRecord, self).__init__(*args, **kwargs)
        self.context = None


def record_factory(*args, **kwargs) -> ProLogRecord:
    """
    This function is called by the logging module to create a ProLogRecord instance,
    and it replaces the built-in log record factory of the logging module

    :param args: The positional arguments passed to the logging module.
    :param kwargs: The keyword arguments passed to the logging module.
    :return: A ProLogRecord instance.
    """
    return ProLogRecord(*args, **kwargs)


class FrameworkFilter(logging.Filter):
    """
    This class is used to filter log records, which are created by the logging module.
    The filter is used to determine if a log record should be processed by a handler.
    """

    def __init__(self):
        """
        This method initializes the filter with the context, which is used to determine if a log record should be
        processed by a handler.

        :param context: The context, which is used to determine if a log record should be processed by a handler.
        """
        super(FrameworkFilter, self).__init__()
        self.context = 'framework'

    def filter(self, record: ProLogRecord) -> bool:
        """
        This method is used to determine if a log record should be processed by a handler.
        The method returns True if the log record should be processed by a handler, and False otherwise.

        :param record: The log record, which is used to determine if it should be processed by a handler.
        :return: True if the log record should be processed by a handler, and False otherwise.
        """
        return record.context == self.context


class TestFilter(logging.Filter):
    """
    This class is used to filter log records, which are created by the logging module.
    The filter is used to determine if a log record should be processed by a handler.
    """

    def __init__(self, context: str):
        """
        This method initializes the filter with the context, which is used to determine if a log record should be
        processed by a handler.

        :param context: The context, which is used to determine if a log record should be processed by a handler.
        """
        super(TestFilter, self).__init__()
        self.context = 'test'

    def filter(self, record: ProLogRecord) -> bool:
        """
        This method is used to determine if a log record should be processed by a handler.
        The method returns True if the log record should be processed by a handler, and False otherwise.

        :param record: The log record, which is used to determine if it should be processed by a handler.
        :return: True if the log record should be processed by a handler, and False otherwise.
        """
        return record.context == self.context


logging.setLogRecordFactory(record_factory)
