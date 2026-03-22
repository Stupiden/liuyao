import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

# Load data
exp_data = np.load("I_q_IPA_exp.npy")
model_data = np.load("I_q_IPA_model.npy")

# Extract columns
q_exp = exp_data[:, 0]
I_exp = exp_data[:, 1]

q_model = model_data[:, 0]
I_model = model_data[:, 1]

# Interpolate model onto experimental q-grid
interp_model = interp1d(
    q_model,
    I_model,
    kind="linear",
    bounds_error=False,
    fill_value="extrapolate"
)

I_model_interp = interp_model(q_exp)

# Objective function: sum of squared errors
def objective(scale):
    residual = I_exp - scale * I_model_interp
    return np.sum(residual**2)

# Find optimal scaling factor
result = minimize_scalar(objective)
best_scale = result.x

print(f"Best scale factor: {best_scale}")
print(f"Minimum SSE: {result.fun}")

# Scaled model
I_fit = best_scale * I_model_interp

plt.figure(figsize=(8, 5))
plt.plot(q_exp, I_exp, "o", markersize=4, label="Experimental data")
plt.plot(q_exp, I_fit, "-", linewidth=2, label=f"Scaled model (scale={best_scale:.4f})")
plt.xlabel("Scattering vector q")
plt.ylabel("Scattering strength I(q)")
plt.legend()
plt.tight_layout()