"""
State definitions for the coffee machine FSM.
"""

class State:
    """Base state class."""
    pass

class IdleState(State):
    """Idle state."""
    pass

class BrewingState(State):
    """Brewing state."""
    pass

class ErrorState(State):
    """Error state."""
    pass