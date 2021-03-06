from discord.ext import commands


class NabError(Exception):
    """Base exception for all NabBot related errors."""
    pass


class UnathorizedUser(commands.CheckFailure, NabError):
    pass


class CannotEmbed(commands.CheckFailure, NabError):
    pass


class NetworkError(NabError):
    """Exception raised when a network call fails after the set reattempts."""
    pass


class CannotPaginate(NabError):
    """Exception raised when a context doesn't meet all the requirements for pagination."""
    pass


class NotTracking(NabError, commands.CheckFailure):
    """Exception raised when a command is used from a server that is not tracking any worlds."""
    pass
