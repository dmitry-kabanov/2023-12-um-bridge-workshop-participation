# Using local model
# To start a model, in another terminal window: $ python minimal-server.py
import umbridge

model = umbridge.HTTPModel("http://localhost:4242", "forward")


print(f"Working with model {model.name}")
print(f"Input size: {model.get_input_sizes()}")
print(f"Output size: {model.get_output_sizes()}")
print("==Checking supported features")
print(f"Supports evaluate: {model.supports_evaluate()}")
print(f"Supports apply_jacobian: {model.supports_apply_jacobian()}")
print(f"Supports apply_hessian: {model.supports_apply_hessian()}")
print(f"Supports gradient: {model.supports_gradient()}")

print("Model call results:")
print(model([[55.0]]))
