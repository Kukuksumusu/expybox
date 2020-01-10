===================================
SHAP
===================================

.. automethod:: expybox.ExpyBox.shap

Method parameters
===================================

* Plot
    Which plot to draw decision, force or both

* Background data
    What background data will be used to sample from, when simulating "missing" feature

    * KMeans: use KMeans to sample from provided dataset
    * Custom variable: provide variable (that is in :code:`kernel_globals`) with instances to use

* Count of KMeans centers
    Number of means to use when creating background data. Only used if :code:`Background data` is set to :code:`KMeans`

* Background data variable
    Variable with background data from which the "missing" features will be sampled. Only used if :code:`Background data` is set to :code:`Custom variable`

* Link
    A generalized linear model link to connect the feature importance values to the model output

    Since the feature importance values, phi, sum up to the model output, it often makes sense
    to connect them to the ouput with a link function where link(outout) = sum(phi).

    If the model output is a probability then the LogitLink link function makes the feature importance values have log-odds units.

* Model sample size
    Number of times to re-evaluate the model when explaining each prediction.

    More samples lead to lower variance estimates of the SHAP values.

* Auto choose model sample size
    The :code:`auto` setting uses :code:`Model sample size` = 2 * train_data.shape[1] + 2048.

* L1 regularization
    The l1 regularization to use for feature selection (the estimation procedure is based on a debiased lasso).

    You can choose following inputs:

    * The :code:`auto` option currently uses "aic" when less that 20% of the possible sample space is enumerated, otherwise it uses no regularization.

    * The :code:`aic` or :code:`bic` options use the AIC and BIC rules for regularization

    * :code:`Integer` selects a fix number of top features

    * :code:`float` directly sets the "alpha" parameter of the sklearn.linear_model.Lasso model used for feature selection

* Class to plot
    If explaining classification problem, select which class prediction to explain

Resources
===================================
* `SHAP paper <https://arxiv.org/abs/1705.07874>`_
* `SHAP in IML book <https://christophm.github.io/interpretable-ml-book/shap.html>`_
* `Documentation of shap <https://shap.readthedocs.io/en/latest/#shap.KernelExplainer>`_
* `Implementation (currently documentation replacement) of force plot <https://github.com/slundberg/shap/blob/master/shap/plots/force.py#L31>`_
* `Implementation (currently documentation replacement) of decision plot <https://github.com/slundberg/shap/blob/master/shap/plots/decision.py#L216>`_
