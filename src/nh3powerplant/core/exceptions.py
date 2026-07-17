"""
Project specific exceptions.
"""


class NH3PowerPlantError(Exception):
    """
    Base exception.
    """


class ConfigurationError(NH3PowerPlantError):
    pass


class ValidationError(NH3PowerPlantError):
    pass


class SimulationError(NH3PowerPlantError):
    pass
