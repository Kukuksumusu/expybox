Anchors
===================================

.. automethod:: expybox.ExpyBox.anchors

Method parameters
===================================

* threshold
    Minimum precision threshold for anchor rules.

* delta
    Used to compute beta.
    The lower the value, the higher the beta parameter for beam search (wider beam) is.
    You can see how exactly beta is computed `here <https://github.com/SeldonIO/alibi/blob/master/alibi/explainers/anchor_base.py#L116>`_.

* tau
    Margin between lower confidence bound and minimum precision or upper bound.
    Here tau is used in place of delta from `IML book <https://christophm.github.io/interpretable-ml-book/anchors.html#finding-anchors>`_
    or the `Anchros paper <https://homes.cs.washington.edu/~marcotcr/aaai18.pdf>`_.

* batch size
    Batch size used for sampling

* discretizer percentiles
    Iterable with percentiles (ints) used for discretization of ordinal features.
    If None, :code:`[25, 50, 75]` will be used.
    Here you need specify the name of the variable with list of percentiles
    that is in the kernel_globals parameter that you passed to ExpyBox.

Resources
===================================
* `Anchors paper <https://homes.cs.washington.edu/~marcotcr/aaai18.pdf>`_
* `Anchors (alibi package) documentation <https://docs.seldon.io/projects/alibi/en/stable/methods/Anchors.html>`_
* `Alibi API reference <https://docs.seldon.io/projects/alibi/en/stable/api/alibi.explainers.anchor_tabular.html>`_
* `compute_beta method in alibi (how B parameter for beam search is calculated from delta) <https://github.com/SeldonIO/alibi/blob/master/alibi/explainers/anchor_base.py#L116>`_
