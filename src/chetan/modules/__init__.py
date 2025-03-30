class AgentModule():
    """Extends agent's functionality by modifying the agent loop.
    """
    NAME: str
    DESCRIPTION: str

    @classmethod
    def get_prologues(cls):
        prologues = set()
        for name in dir(cls):
            method = getattr(cls, name)
            if hasattr(method, "_is_prologue") and method._is_prologue:
                prologues.add(method)
        return prologues

    @classmethod
    def get_epilogues(cls):
        epilogues = set()
        for name in dir(cls):
            method = getattr(cls, name)
            if hasattr(method, "_is_epilogue") and method._is_epilogue:
                epilogues.add(method)
        return epilogues

    @classmethod
    def get_tools(cls):
        tools = set()
        for name in dir(cls):
            method = getattr(cls, name)
            if hasattr(method, "_is_tool") and method._is_tool:
                tools.add(method)
        return tools


def tool_method(func):
    func._is_tool = True
    return func


def prologue(func):
    func._is_prologue = True
    return func


def epilogue(func):
    func._is_epilogue = True
    return func
