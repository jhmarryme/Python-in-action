# Evaluate tutorial package marker
from .agent import root_agent  # re-export for CLI/pytest convenience
from . import agent  # ensure 'agent' module is discoverable under this package
