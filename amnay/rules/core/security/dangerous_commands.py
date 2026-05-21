import re

from amnay.rules.base import Rule

PATTERNS = [
    r"curl\s+.*\|\s*(sh|bash)",
    r"wget\s+.*\|\s*(sh|bash)",
    r"sudo\s+rm\s+-rf",
]


class DangerousCommandsRule(Rule):

    id = "dangerous-commands"

    name = "Dangerous Commands"

    severity = "critical"

    def validate(self, workflow):

        issues = []

        for job in workflow.jobs:

            for command in job.commands:

                for pattern in PATTERNS:

                    if re.search(pattern, command):

                        issues.append(
                            self.issue(
                                f"{job.name}: " f"dangerous command " f"detected"
                            )
                        )

        return issues
