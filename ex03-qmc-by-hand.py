import argparse
import qmcpy as qp
from qmcpy.integrand.um_bridge_wrapper import UMBridgeWrapper
import numpy as np
import umbridge

# Read URL from command line argument
parser = argparse.ArgumentParser(description='QMCPy with UM-Bridge model demo.')
parser.add_argument('url', metavar='url', type=str,
                    help='the URL at which the model is running, for example http://localhost:4242')
args = parser.parse_args()
print(f"Connecting to host URL {args.url}")

# Set up umbridge model and model config
model = umbridge.HTTPModel(args.url, "forward")
config = {}

# Get input dimension from model
d = model.get_input_sizes(config)[0]

# Choose a distribution to sample via QMC
dnb2 = qp.DigitalNetB2(d)
gauss_sobol = qp.Uniform(dnb2, lower_bound=[1]*d, upper_bound=[1.05]*d)

sample = gauss_sobol.gen_samples()

n = len(sample)
qoi_list = []
for s in sample:
    qoi_list.append(model([list(s)]))

qoi_est = np.mean(qoi_list)
print("Expectation: ", qoi_est)
