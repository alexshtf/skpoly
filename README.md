# skpoly

`skpoly` provides drop-in polynomial feature generators that integrate with scikit-learn pipelines. The library focuses on smooth orthogonal bases such as Bernstein and Legendre polynomials, letting you capture non-linear structure with well-conditioned numerical behavior.

## Quick start

Create a pipeline that first rescales each input dimension and then expands it with Bernstein features before fitting a linear model:

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Ridge
from skpoly import BernsteinFeatures

pipeline = make_pipeline(
    MinMaxScaler(),
    BernsteinFeatures(degree=8),
    Ridge(alpha=1e-2),
)

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

## Pairwise interaction features

For multivariate inputs you can enable tensor-product features to model pairwise (and higher-order) interactions between coordinates. Setting `tensor_product=True` expands the basis with every combination of the univariate polynomials:

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from skpoly import LegendreFeatures

pipeline = make_pipeline(
    MinMaxScaler(),
    LegendreFeatures(degree=5, tensor_product=True),
    LogisticRegression(),
)
```

## Development

Clone the repository and install dependencies using [uv](https://github.com/astral-sh/uv):

```bash
git clone https://github.com/alexshtf/skpoly.git
cd skpoly
uv venv
source .venv/bin/activate
uv sync
```

Using `uv` keeps dependency resolution fast and reproducible.
