from typing import Callable, Self, Tuple
from functools import wraps
from enum import Enum

import time
import random
import pendulum

from chetan.modules import AgentModule


class StopCode(Enum):
    EXITED = 0
    ERROR = 1
    MAX_ITER = 2


class AgentLoop:
    def __init__(self):
        self.execution_times = []
        self.ctx = None
        self.seq_executor = None
        self._stages = {}  # Add this to store stages

        # Initialize the stages dictionary if not already done
        if not self._stages:
            for stage_name, methods in self.get_stages().items():
                self._stages[stage_name] = methods
                
    def use(self, *modules: Tuple[AgentModule]) -> Self:
        """Uses the given modules in the agent loop.
        
        Args: 
            modules (tuple): The modules to be used.
        """
        
        for module in list(modules):
            
            # 1. register actions
            # 2. register prologue items
            # 3. register epilogue items
            
            pass 
        
        return self

    @staticmethod
    def stage(name: str):
        def decorator(func: Callable):
            func._is_stage = True
            func._stage_name = name

            @wraps(func)
            def wrapper(self_instance: "AgentLoop", *args, **kwargs):
                start_time = time.time()
                result = func(self_instance, *args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time

                # Store the execution time in the instance's list
                self_instance.execution_times.append(
                    {
                        "stage": name,
                        "execution_time": execution_time,
                        "timestamp": pendulum.now().isoformat(),
                    }
                )

                return result

            wrapper._is_stage = True
            wrapper._stage_name = name
            return wrapper

        return decorator

    @classmethod
    def get_stages(cls):
        stages = {}
        for name in dir(cls):
            method = getattr(cls, name)
            if hasattr(method, "_is_stage") and method._is_stage:
                stages[method._stage_name] = method
        return stages

    @stage("prologue")
    def stage_prologue(self):
        # TODO: Execute prologue items sequentially, or parallel
        pass

    @stage("process")
    def stage_process(self):
        # TODO: Pass through the process
        pass

    @stage("epilogue")
    def stage_epilogue(self):
        # TODO: Execute epilogue items sequentially, or parallel
        pass
    
    def _execute(self) -> bool:
        # Execute each stage
        for stage in self._stages:
            self._stages[stage](self)

        return True  # Assuming no exit condition by default

    def run(self, max_iter=100):
        for iteration in range(max_iter):

            # Increment the iteration count in the context
            self.ctx.iterate(iteration)

            try:
                # Try a forward pass of sequential executor, getting the result and checking if it exited
                exited = self._execute()

                # If exited, return the exit code
                if exited:
                    return StopCode.EXITED, None

            except Exception as e:
                # ! TODO: Handle 'some' known exceptions to continue abruptions
                return StopCode.ERROR, e

        # If max iterations reached, return the max iteration code
        return StopCode.MAX_ITER, None

class Agent:
    pass