from amnay.rules.base import Rule


class ConcurrencyRule(Rule):

    id = "concurrency"

    severity = "medium"

    def validate(self, workflow):

        if workflow.provider != "github":
            return []

        concurrency = workflow.raw.get("concurrency")

        if not concurrency:

            return [self.issue("workflow: missing concurrency")]

        return []
