import numpy as np
import pytest

from skpoly import BernsteinFeatures, LegendreFeatures


@pytest.mark.parametrize(
    "kwargs, message",
    [
        ({"degree": -1}, "degree must be a non-negative integer"),
        ({"feature_range": (0.0,)}, "feature_range must be a tuple of two floats"),
        ({"feature_range": (0.0, np.inf)}, "feature_range values must be finite"),
        ({"feature_range": (1.0, 0.0)}, "feature_range must satisfy a < b"),
        ({"include_bias": "yes"}, "include_bias must be a boolean"),
        ({"tensor_product": 1}, "tensor_product must be a boolean"),
    ],
)
def test_legendre_constructor_validates_parameters(kwargs, message):
    transformer = LegendreFeatures(**kwargs)
    X = np.zeros((2, 1), dtype=float)
    with pytest.raises(ValueError, match=message):
        transformer.fit(X)


def test_missing_values_produce_zero_features_legendre():
    transformer = LegendreFeatures(degree=2, include_bias=True)
    training_data = np.array([[0.0], [1.0]], dtype=float)
    transformer.fit(training_data)

    test_data = np.array([[np.nan], [0.5]], dtype=float)
    transformed = transformer.transform(test_data)

    expected_second_row = np.array([1.0, 0.0, -0.5])
    expected = np.vstack(
        [
            np.zeros_like(expected_second_row),
            expected_second_row,
        ]
    )
    np.testing.assert_allclose(transformed, expected)


def test_tensor_products_vanish_when_a_column_is_missing():
    transformer = LegendreFeatures(degree=1, include_bias=True, tensor_product=True)
    training_data = np.array(
        [
            [0.0, 0.0],
            [1.0, 1.0],
        ],
        dtype=float,
    )
    transformer.fit(training_data)

    test_data = np.array([[np.nan, 0.5]], dtype=float)
    transformed = transformer.transform(test_data)

    expected = np.array([[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]])
    np.testing.assert_allclose(transformed, expected)


def test_multi_column_transform_matches_single_column_concatenation():
    params = {"degree": 2, "include_bias": True, "tensor_product": False}
    training_data = np.array(
        [
            [0.0, 0.25],
            [1.0, 0.75],
        ],
        dtype=float,
    )
    multi_column = LegendreFeatures(**params).fit(training_data)

    test_sample = np.array([[0.5, 0.25]], dtype=float)
    combined = multi_column.transform(test_sample)

    single_column_features = []
    for column in range(training_data.shape[1]):
        column_transformer = LegendreFeatures(**params).fit(training_data[:, [column]])
        single_column_features.append(column_transformer.transform(test_sample[:, [column]]))
    stacked = np.concatenate(single_column_features, axis=1)

    np.testing.assert_allclose(combined, stacked)


def test_bernstein_basis_matches_known_values():
    transformer = BernsteinFeatures(degree=2, include_bias=True)
    training_data = np.array([[0.0], [1.0]], dtype=float)
    transformer.fit(training_data)

    midpoint = np.array([[0.5]], dtype=float)
    transformed = transformer.transform(midpoint)

    expected = np.array([[0.25, 0.5, 0.25]])
    np.testing.assert_allclose(transformed, expected)
