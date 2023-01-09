class Error(Exception):
    """base class for other exceptions"""
    pass


class TooManyColumns(Error):
    """Triggered when the number of columns is too large"""
    pass


class NotEnoughColumns(Error):
    """Triggered when the number of columns is too small"""
    pass
