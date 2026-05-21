import yaml


class PolicyLoader:

    @staticmethod
    def load(path: str):

        with open(path) as f:
            return yaml.safe_load(f)
