===================================
Partial Dependence plot
===================================

.. automethod:: expybox.ExpyBox.pdplot

Method parameters
===================================

* Feature to plot
    Which feature should be plotted

* Number of grid points
    Number of grid points to calculate partial dependence value in (for numeric feature)

* Grid type
    Type of grid points for numeric feature (percentile or equal)

* Custom grid range
    * Custom range minimum/maximum
        Percentile (when :code:`grid_type` = :code:`percentile`) or value (when :code:`grid_type` = :code:`equal`)
        lower/upper bound of range to investigate (for numeric feature)

        (Enabled only when :code:`Custom grid range` is checked and :code:`Variable with grid points` is :code:`None`)

    * Variable with grid points
        Name of variable (or None) from :code:`kernel_globals` with customized list of grid points (list of integers) for numeric feature

* Center the plot
    Whether the plot should be centered (starting at [0,0])

* Plot data points distribution
    Whether to display data points distribution below the plot

* Show precentile buckets
    Whether to show percentile buckets below the plot

* Plot lines - ICE plot
    Whether to plot also lines for single instances (which makes the plot an ICE plot)

    * Lines to plot
        How many lines to plot, can be a integer or a float

        * integer values higher than 1 are interpreted as absolute amount

        * floats are interpreted as fraction (e.g. 0.5 means half of all possible lines)

    * Cluster lines
        Whether to cluster the lines

        * Number of cluster centers - Number of cluster centers for lines

        * Cluster method - Method to use for clustering of lines (KMeans or MiniBatchKMeans)

Resources
===================================
* `Documentation (pdp_isolate) <https://pdpbox.readthedocs.io/en/latest/pdp_isolate.html>`_
* `Documentation (pdp_plot) <https://pdpbox.readthedocs.io/en/latest/pdp_plot.html>`_
* `Partial Dependence plot <https://christophm.github.io/interpretable-ml-book/pdp.html>`_
* `Individual Conditional Expectation <https://christophm.github.io/interpretable-ml-book/ice.html>`_
* `PDPbox on GitHub <https://github.com/SauceCat/PDPbox>`_
