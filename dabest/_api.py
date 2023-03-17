#!/usr/bin/python
# -*-coding: utf-8 -*-
# Author: Joses Ho
# Email : joseshowh@gmail.com


def load(data, idx=None, x=None, y=None, paired=None, id_col=None,
        ci=95, resamples=5000, random_seed=12345, proportional=False, 
        delta2 = False, experiment = None, experiment_label = None,
        x1_level = None, mini_meta=False):
    '''
    Loads data in preparation for estimation statistics.

    This is designed to work with pandas DataFrames.

    Parameters
    ----------
    data : pandas DataFrame
    idx : tuple
        List of column names (if 'x' is not supplied) or of category names
        (if 'x' is supplied). This can be expressed as a tuple of tuples,
        with each individual tuple producing its own contrast plot
    x : string or list, default None
        Column name(s) of the independent variable. This can be expressed as
        a list of 2 elements if and only if 'delta2' is True; otherwise it 
        can only be a string.
    y : string, default None
        Column names for data to be plotted on the x-axis and y-axis.
    paired : string, default None
        The type of the experiment under which the data are obtained
    id_col : default None.
        Required if `paired` is True.
    ci : integer, default 95
        The confidence interval width. The default of 95 produces 95%
        confidence intervals.
    resamples : integer, default 5000.
        The number of resamples taken to generate the bootstraps which are used
        to generate the confidence intervals.
    random_seed : int, default 12345
        This integer is used to seed the random number generator during
        bootstrap resampling, ensuring that the confidence intervals
        reported are replicable.
    proportional : boolean, default False. 
        An indicator of whether the data is binary or not. When set to True, it
        specifies that the data consists of binary data, where the values are
        limited to 0 and 1. The code is not suitable for analyzing proportion
        data that contains non-numeric values, such as strings like ‘yes’ and ‘no’.
        When False or not provided, the algorithm assumes that
        the data is continuous and uses a non-proportional representation.
    delta2 : boolean, default False
        Indicator of delta-delta experiment
    experiment : String, default None
        The name of the column of the dataframe which contains the label of 
        experiments
    experiment_lab : list, default None
        A list of String to specify the order of subplots for delta-delta plots.
        This can be expressed as a list of 2 elements if and only if 'delta2' 
        is True; otherwise it can only be a string. 
    x1_level : list, default None
        A list of String to specify the order of subplots for delta-delta plots.
        This can be expressed as a list of 2 elements if and only if 'delta2' 
        is True; otherwise it can only be a string. 
    mini_meta : boolean, default False
        Indicator of weighted delta calculation.

    Returns
    -------
    A `Dabest` object.

    Example
    --------
    Load libraries.

    >>> import numpy as np
    >>> import pandas as pd
    >>> import dabest

    Create dummy data for demonstration.

    >>> np.random.seed(88888)
    >>> N = 10
    >>> c1 = sp.stats.norm.rvs(loc=100, scale=5, size=N)
    >>> t1 = sp.stats.norm.rvs(loc=115, scale=5, size=N)
    >>> df = pd.DataFrame({'Control 1' : c1, 'Test 1': t1})

    Load the data.

    >>> my_data = dabest.load(df, idx=("Control 1", "Test 1"))

    For proportion plot.
    >>> np.random.seed(88888)
    >>> N = 10
    >>> c1 = np.random.binomial(1, 0.2, size=N)
    >>> t1 = np.random.binomial(1, 0.5, size=N)
    >>> df = pd.DataFrame({'Control 1' : c1, 'Test 1': t1})
    >>> my_data = dabest.load(df, idx=("Control 1", "Test 1"),proportional=True)



    '''
    from ._classes import Dabest

    return Dabest(data, idx, x, y, paired, id_col, ci, resamples, random_seed, proportional, delta2, experiment, experiment_label, x1_level, mini_meta)

