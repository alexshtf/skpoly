Getting started
===============

This guide walks through installing ``skpoly`` and fitting your first model with it.

Installation
------------

``skpoly`` is published on PyPI, so you can install it with your preferred package manager:

.. code-block:: bash

   pip install skpoly

If you manage environments with `uv <https://docs.astral.sh/uv/>`_, add the dependency to your project and
sync your environment in one step:

.. code-block:: bash

   uv add skpoly

   # or, inside an existing environment
   uv pip install skpoly

Quick start
-----------

The transformers in ``skpoly`` interoperate with scikit-learn pipelines. The example below rescales input
features, expands them with Bernstein polynomials, and fits a ridge regressor:

.. code-block:: python

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

Next steps
----------

- Browse the :doc:`API reference <api/index>` for detailed documentation on each transformer.
- Explore the :doc:`examples <examples/index>` to see how Bernstein and Legendre features behave in practice.
- Pair ``skpoly`` with scikit-learn model selection utilities such as grid search to tune the polynomial degree
  and regularization strength for your task.
