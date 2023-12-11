import umbridge
import time
import os

class MyModel(umbridge.Model):
    def __init__(self):
        super().__init__("forward")

    def get_input_sizes(self, config):
        return [1]

    def get_output_sizes(self, config):
        return [1]

    def __call__(self, parameters, config):
        posterior = 5*parameters[0][0]
        return [[posterior]]

    def supports_evaluate(self):
        return True

    def gradient(self,out_wrt, in_wrt, parameters, sens, config):
        raise NotImplementedError("Gradient computation is not implemented")

    def supports_gradient(self):
        return False

mymodel = MyModel()

port = 4242
print(f"Serving model on port {port}")
umbridge.serve_models([mymodel], port)
