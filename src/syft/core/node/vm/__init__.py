from .vm import VirtualMachine
from .client import VirtualMachineClient

from ..common.service.node_service import NodeService  # noqa: F401
from typing import Dict  # noqa: F401

message_service_mapping: Dict[str, NodeService] = {}