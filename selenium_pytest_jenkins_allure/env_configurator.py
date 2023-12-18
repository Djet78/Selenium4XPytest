from .utils import singleton


@singleton
class EnvConfigurator:
    def __init__(self, desired_env: str = 'dev'):
        self.env = desired_env.lower()
        # Do some env. related computations.
        #   Predefine DB connectors, get and store correct creds for the env., etc.
