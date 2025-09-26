"""Legendre polynomial features for non-linear classification."""

# %%
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler

from skpoly import LegendreFeatures

# %%
X, y = make_moons(noise=0.25, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=0
)

# %%
pipeline = make_pipeline(
    MinMaxScaler(),
    LegendreFeatures(degree=5, include_bias=False, tensor_product=True),
    LogisticRegression(max_iter=2000),
)

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(f"Accuracy on the held-out set: {accuracy_score(y_test, y_pred):.3f}")
