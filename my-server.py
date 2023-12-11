import umbridge
import time
import os

class TestModel(umbridge.Model):

    def __init__(self):
        super().__init__("forward")

    def get_input_sizes(self, config):
        return [1]

    def get_output_sizes(self, config):
        return [1]

    def __call__(self, parameters, config):
        posterior = 4*parameters[0][0]
        return [[posterior]]

    def supports_evaluate(self):
        return True

    def gradient(self,out_wrt, in_wrt, parameters, sens, config):
        raise NotImplementedError("Gradient computation is not implemented")

    def supports_gradient(self):
        return False

testmodel = TestModel()

umbridge.serve_models([testmodel], 4242)
