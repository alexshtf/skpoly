"""Visualize a Bernstein polynomial regression fit on a 1D function."""

# %%
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler

from skpoly import BernsteinFeatures


# %%
def target_function(x: np.ndarray) -> np.ndarray:
    """Smooth ground-truth signal defined on [-1, 1]."""

    return np.sin(np.pi * x) + 0.3 * np.cos(4 * np.pi * x)


random_state = np.random.RandomState(0)
X = np.linspace(-1.0, 1.0, 200)[:, None]
y = target_function(X[:, 0]) + random_state.normal(scale=0.1, size=X.shape[0])


# %%
pipeline = make_pipeline(
    MinMaxScaler(),
    BernsteinFeatures(degree=12, include_bias=True, tensor_product=False),
    LinearRegression(),
)

pipeline.fit(X, y)


# %%
X_plot = np.linspace(-1.0, 1.0, 400)[:, None]
y_true = target_function(X_plot[:, 0])
y_pred = pipeline.predict(X_plot)
print(f"MAE on the dense grid: {mean_absolute_error(y_true, y_pred):.3f}")

plt.figure(figsize=(7, 4))
plt.scatter(X[:, 0], y, color="#4c72b0", alpha=0.5, s=20, label="Noisy samples")
plt.plot(X_plot[:, 0], y_true, color="#55a868", linewidth=2, label="True function")
plt.plot(
    X_plot[:, 0],
    y_pred,
    color="#c44e52",
    linewidth=2,
    label="Bernstein approximation",
)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Bernstein polynomial regression with feature scaling")
plt.legend()
plt.tight_layout()
plt.show()
