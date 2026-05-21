from amnay.core.models import Workflow, Job
from amnay.providers.base import CIProvider
from amnay.providers.github.parser import GitHubParser


class GitHubProvider(CIProvider):

    def load(self, path: str) -> Workflow:

        data = GitHubParser.load(path)

        jobs = []

        for name, config in data.get("jobs", {}).items():

            commands = []
            actions = []

            for step in config.get("steps", []):

                if "run" in step:
                    commands.append(step["run"])

                if "uses" in step:
                    actions.append(step["uses"])

            jobs.append(
                Job(
                    name=name,
                    timeout=config.get("timeout-minutes"),
                    commands=commands,
                    actions=actions,
                    permissions=config.get("permissions"),
                )
            )

        return Workflow(
            name=data.get("name", "github-workflow"),
            provider="github",
            jobs=jobs,
            raw=data,
        )
