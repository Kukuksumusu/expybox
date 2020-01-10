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
    You can see how exactly beta is computed by following a link in resources.

* tau
    Margin between lower confidence bound and minimum precision or upper bound.
    Here tau is used in place of delta from IML book.

* batch size
    Batch size used for sampling

* discretizer percentiles
    Iterable with percentiles (int) used for discretization of ordinal features.
    If None, [25, 50, 75] will be used
    Here you need specify the name of the variable with list of percentiles
    that is in the kernel_globals parameter that you passed to ExpyBox.
