===================================
SHAP Feature Importance
===================================

.. automethod:: expybox.ExpyBox.shap_feature_importance

Method parameters
===================================
See `shap parameters <https://expybox.readthedocs.io/en/latest/methods/shap.html>`_.

Additional parameter:

* Sample size
    Number of instances from train data to use for calculating mean shap value for each feature.

Resources
===================================
* `SHAP paper <https://arxiv.org/abs/1705.07874>`_
* `SHAP in IML book <https://christophm.github.io/interpretable-ml-book/shap.html>`_
* `Documentation of shap <https://shap.readthedocs.io/en/latest/#shap.KernelExplainer>`_
* `Implementation (currently documentation replacement) of summary plot <https://github.com/slundberg/shap/blob/master/shap/plots/summary.py#L18>`_
