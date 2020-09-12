from __future__ import annotations

from typing import TYPE_CHECKING


class CrispValueCalculatorError(ValueError):
    pass


class NoTermMembershipsError(CrispValueCalculatorError):
    def __init__(self, var: FuzzyVariable):
        super().__init__("None of the terms for the fuzzy variable"
                         " '%s' have membership. Make sure that you"
                         " have at least one rule connected to this variable"
                         " and have run the rules calculation." % var.label)


class DefuzzifyError(CrispValueCalculatorError):
    def __init__(self, var: FuzzyVariable, reason: str):
        super().__init__("Cannot defuzzify the fuzzy variable '%s'.  %s"
                         % (var.label, reason))


class EmptyMembershipError(DefuzzifyError):
    def __init__(self, var: FuzzyVariable):
        reason = ("The membership area is empty. Probably the rule system is"
                  " too sparse. Check to make sure the given input values will"
                  " activate at least one connected term in each antecedent"
                  " via the current set of rules.")
        super().__init__(var, reason)


if TYPE_CHECKING:
    from .fuzzyvariable import FuzzyVariable
