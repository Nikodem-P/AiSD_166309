from typing import Any


class Vertex:
    data: Any
    # unused?
    index: int

    def __init__(self, data: Any):
        self.data = data
