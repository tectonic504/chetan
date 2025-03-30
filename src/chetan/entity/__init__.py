from typing import Dict, List
from pydantic import BaseModel

from chetan.align import Rule

from chetan.agent import Agent
from chetan.entity.human import Human

class Entity:
    pass

class Persona(BaseModel):
    id: str
    role: str
    description: str
    rules: List[Rule]
    
class SystemEntities():
    agents: Dict[str, Agent] = {}
    humans: Dict[str, Human] = {}