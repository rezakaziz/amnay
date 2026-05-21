from amnay.providers.github.provider import GitHubProvider

from amnay.rules.core.reliability.timeout import TimeoutRule

from amnay.rules.core.reliability.concurrency import ConcurrencyRule

from amnay.rules.core.security.pinned_actions import (
    PinnedActionsRule,
)

from amnay.rules.core.security.dangerous_commands import (
    DangerousCommandsRule,
)

from amnay.rules.core.security.least_privilege import (
    LeastPrivilegeRule,
)

PROVIDERS = {
    "github": GitHubProvider(),
}


# règles obligatoires
CORE_RULES = [
    DangerousCommandsRule(),
]


# règles configurables
RULE_REGISTRY = {
    "timeout": TimeoutRule,
    "concurrency": ConcurrencyRule,
    "pinned_actions": PinnedActionsRule,
    "least_privilege": LeastPrivilegeRule,
}
