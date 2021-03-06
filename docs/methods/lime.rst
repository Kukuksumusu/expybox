===================================
LIME
===================================

.. automethod:: expybox.ExpyBox.lime

Method parameters
===================================

* Number of features
    Maximum number of features present in explanation

* Number of samples
    Size of the neighborhood to learn the surrogate linear model

* Kernel width
    Kernel width for the exponential kernel. Actual value used will be the
    :code:`inputted value * sqrt(train_data.shape[1])`.

* Feature selection
    Feature selection method for choosing the best features for surrogate model. There are following options:

    *   forward_selection: iteratively add features to the model (costly when num_features is high)
    *   highest_weights: selects the features that have the highest product of
        absolute weight * original data point when learning with all the features
    *   lasso_path: choose features based on the lasso regularization path
    *   none: use all features, ignore :code:`Number of features` option
    *   auto: use forward_selection if :code:`Number of features` <= 6, and highest_weights otherwise

* Discretize continuous
    Whether to discretize all non-categorical features

* Discretizer
    Which discretizer to use when discretizing continuous features. Only matters if discretize continuous is True.

* Distance metric
    What distance metric to use for calculating weights of perturbed instances.

    It's used as an :code:`distance_metric` argument for :code:`sklearn.metrics.pairwise_distances()`.
    Documentation of the function (with options for metric): `sklearn.metrics.pairwise_distances <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html>`_

* Variable with model regressor
    If you want to use a different regressor than `Ridge regressor <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html?highlight=ridge%20regression#sklearn.linear_model.ridge_regression>`_
    you can specify a variable in provided :code:`kernel_globals` dictionary with the regressor.

    It must have :code:`model_regressor.coef_` and "sample_weight" as a parameter to :code:`model_regressor.fit()`

Resources
===================================
* `LIME (lime-ml/lime_tabular) documentation <https://lime-ml.readthedocs.io/en/latest/lime.html#module-lime.lime_tabular>`_,
* `LIME in IML book <https://christophm.github.io/interpretable-ml-book/lime.html>`_
* `LIME paper <https://arxiv.org/abs/1602.04938>`_
* `lime-ml package on GitHub <https://github.com/marcotcr/lime>`_
