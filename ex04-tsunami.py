# Using local model of tsunami
# To start a model, use docker
import umbridge

model = umbridge.HTTPModel("http://localhost:4242", "forward")

config = {"level": 0, "vtk_output": True}

print(f"Working with model {model.name}")
print(f"Input size: {model.get_input_sizes(config)}")
print(f"Output size: {model.get_output_sizes(config)}")
print("==Checking supported features")
print(f"Supports evaluate: {model.supports_evaluate()}")
print(f"Supports apply_jacobian: {model.supports_apply_jacobian()}")
print(f"Supports apply_hessian: {model.supports_apply_hessian()}")
print(f"Supports gradient: {model.supports_gradient()}")

print("Model call results:")
print(model([[100.0, 60.0]], config))
