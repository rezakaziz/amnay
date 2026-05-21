import re

from amnay.rules.base import Rule

SHA_PATTERN = re.compile(r"@[a-f0-9]{40}$")


class PinnedActionsRule(Rule):

    id = "pinned-actions"

    name = "Pinned Actions"

    severity = "critical"

    def validate(self, workflow):

        if workflow.provider != "github":
            return []

        issues = []

        for job in workflow.jobs:

            for action in job.actions:

                if not SHA_PATTERN.search(action):

                    issues.append(
                        self.issue(
                            f"{job.name}: "
                            f"action not pinned "
                            f"to immutable SHA: "
                            f"{action}"
                        )
                    )

        return issues
