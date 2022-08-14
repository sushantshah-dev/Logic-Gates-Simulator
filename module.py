class Module():
    def __init__(self, inputs=()):
        self.inputs = inputs
        self.outputs = ()

    def __call__(self, *args):
        return self.outputs