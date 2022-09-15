def __init__(self, config={}):
    self.set_default_confi()

    for attr, val in config.items():
        setattr(self, attr, val)
