"""
Project specific exceptions.
"""


class NH3PowerPlantError(Exception):
    """
    Base class for all project specific exceptions.
    """


class ConfigurationError(NH3PowerPlantError):
    """
    Raised for configuration errors.
    """


class ValidationError(NH3PowerPlantError):
    """
    Raised if input data are invalid.
    """


class NotFoundError(NH3PowerPlantError):
    """
    Raised if a requested object cannot be found.
    """


class SimulationError(NH3PowerPlantError):
    """
    Raised if a simulation cannot be completed.
    """
