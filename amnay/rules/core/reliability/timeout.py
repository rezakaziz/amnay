from amnay.rules.base import Rule


class TimeoutRule(Rule):

    id = "timeout"

    severity = "high"

    DEFAULT_MAX_TIMEOUT = 30

    def __init__(
        self,
        max_timeout=30,
    ):

        self.max_timeout = max_timeout

    def validate(self, workflow):

        issues = []

        for job in workflow.jobs:

            if not job.timeout:

                issues.append(self.issue(f"{job.name}: missing timeout"))

            elif job.timeout > self.max_timeout:

                issues.append(
                    self.issue(
                        f"{job.name}: timeout exceeds " f"{self.max_timeout} minutes"
                    )
                )

        return issues
