Getting started
===============

Install
-------

``skpoly`` is published on PyPI. Install it with ``uv``:

.. code-block:: console

   uv pip install skpoly

Quick example
-------------

Create Bernstein features for regression:

.. code-block:: python

   import numpy as np
   from sklearn.linear_model import LinearRegression

   from skpoly import BernsteinFeatures

   X = np.linspace(0.0, 1.0, num=20)[:, None]
   y = np.sin(2.0 * np.pi * X).ravel()

   transformer = BernsteinFeatures(degree=5)
   model = LinearRegression().fit(transformer.fit_transform(X), y)

   X_test = np.linspace(0.0, 1.0, num=100)[:, None]
   y_pred = model.predict(transformer.transform(X_test))

Next steps
----------

- See :doc:`api` for the full reference.
- Explore :doc:`examples` for end-to-end workflows.

