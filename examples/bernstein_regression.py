"""Bernstein polynomial features for non-linear regression."""

# %%
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import QuantileTransformer

from skpoly import BernsteinFeatures

# %%
# Create a smooth, non-linear target function on [0, 1]
random_state = np.random.RandomState(0)
X = np.linspace(0, 1, 200)[:, None]
y = (
    np.sin(2 * np.pi * X[:, 0])
    + 0.3 * np.cos(6 * np.pi * X[:, 0])
    + random_state.normal(scale=0.1, size=X.shape[0])
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=random_state)

# %%
n_quantiles = min(100, X_train.shape[0])
pipeline = make_pipeline(
    QuantileTransformer(
        n_quantiles=n_quantiles,
        output_distribution="uniform",
        random_state=random_state,
    ),
    BernsteinFeatures(degree=10, include_bias=True, tensor_product=False),
    Ridge(alpha=1e-2),
)

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(f"MAE on the held-out set: {mean_absolute_error(y_test, y_pred):.3f}")
