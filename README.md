# DABEST-Python

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Recent Version Update

On 20 March 2023, we officially released **DABEST v2023.02.14 for
Python**. This new version provided the following new features:

1.  **Repeated measures.** Augments the prior function for plotting
    (independent) multiple test groups versus a shared control; it can
    now do the same for repeated-measures experimental designs. Thus,
    together, these two methods can be used to replace both flavors of
    the 1-way ANOVA with an estimation analysis.

2.  **Proportional data.** Generates proportional bar plots,
    proportional differences, and calculates Cohen’s h. Also enables
    plotting Sankey diagrams for paired binary data. This is the
    estimation equivalent to a bar chart with Fisher’s exact test.

3.  **The $\Delta\Delta$ plot.** Calculates the delta-delta
    ($\Delta\Delta$) for 2 × 2 experimental designs and plots the four
    groups with their relevant effect sizes. This design can be used as
    a replacement for the 2 × 2 ANOVA.

4.  **Mini-meta.** Calculates and plots a weighted delta ($\Delta$) for
    meta-analysis of experimental replicates. Useful for summarizing
    data from multiple replicated experiments, for example by different
    scientists in the same lab, or the same scientist at different
    times. When the observed values are known (and share a common
    metric), this makes meta-analysis available as a routinely
    accessible tool.

## Contents

<!-- TOC depthFrom:1 depthTo:2 withLinks:1 updateOnSave:1 orderedList:0 -->

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [How to cite](#how-to-cite)
- [Bugs](#bugs)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Testing](#testing)
- [DABEST in other languages](#dabest-in-other-languages)

<!-- /TOC -->

## About

DABEST is a package for **D**ata **A**nalysis using
**B**ootstrap-Coupled **EST**imation.

[Estimation
statistics](https://en.wikipedia.org/wiki/Estimation_statistics) are a
[simple framework](https://thenewstatistics.com/itns/) that avoids the
[pitfalls](https://www.nature.com/articles/nmeth.3288) of significance
testing. It employs familiar statistical concepts such as means, mean
differences, and error bars. More importantly, it focuses on the effect
size of one’s experiment or intervention, rather than succumbing to a
false dichotomy engendered by *P* values.

An estimation plot comprises two key features.

1.  It presents all data points as a swarm plot, ordering each point to
    display the underlying distribution.

2.  It illustrates the effect size as a **bootstrap 95% confidence
    interval** on a **separate but aligned axis**.

![The five kinds of estimation
plots](showpiece.png "The five kinds of estimation plots.")

DABEST powers [estimationstats.com](https://www.estimationstats.com/),
allowing everyone access to high-quality estimation plots.

## Installation

This package is tested on Python 3.6, 3.7, 3.8 and 3.10. It is highly
recommended to download the [Anaconda
distribution](https://www.continuum.io/downloads) of Python in order to
obtain the dependencies easily.

You can install this package via `pip`.

To install, at the command line run

``` shell
conda config --add channels conda-forge
conda install dabest
```

or –\>

``` shell
pip install dabest
```

You can also
[clone](https://help.github.com/articles/cloning-a-repository) this repo
locally.

Then, navigate to the cloned repo in the command line and run

``` shell
pip install .
```

## Usage

``` python3
import pandas as pd
import dabest

# Load the iris dataset. This step requires internet access.
iris = pd.read_csv("https://github.com/mwaskom/seaborn-data/raw/master/iris.csv")

# Load the above data into `dabest`.
iris_dabest = dabest.load(data=iris, x="species", y="petal_width",
                          idx=("setosa", "versicolor", "virginica"))

# Produce a Cumming estimation plot.
iris_dabest.mean_diff.plot();
```

![A Cumming estimation plot of petal width from the iris
dataset](iris.png)

Please refer to the official
[tutorial](https://acclab.github.io/DABEST-python-docs/tutorial.html)
for more useful code snippets.

## How to cite

**Moving beyond P values: Everyday data analysis with estimation plots**

*Joses Ho, Tayfun Tumkaya, Sameer Aryal, Hyungwon Choi, Adam
Claridge-Chang*

Nature Methods 2019, 1548-7105.
[10.1038/s41592-019-0470-3](http://dx.doi.org/10.1038/s41592-019-0470-3)

[Paywalled publisher
site](https://www.nature.com/articles/s41592-019-0470-3); [Free-to-view
PDF](https://rdcu.be/bHhJ4)

## Bugs

Please report any bugs on the [Github issue
tracker](https://github.com/ACCLAB/DABEST-python/issues/new).

## Contributing

All contributions are welcome; please read the [Guidelines for
contributing](CONTRIBUTING.md) first.

We also have a [Code of Conduct](CODE_OF_CONDUCT.md) to foster an
inclusive and productive space.

### A wish list for new features

If you have any specific comments and ideas for new features that you
would like to share with us, please read the [Guidelines for
contributing](CONTRIBUTING.md), create a new issue using Feature request
template or create a new post in [our Google
Group](https://groups.google.com/g/estimationstats).

## Acknowledgements

We would like to thank alpha testers from the [Claridge-Chang
lab](https://www.claridgechang.net/): [Sangyu
Xu](https://github.com/sangyu), [Xianyuan
Zhang](https://github.com/XYZfar), [Farhan
Mohammad](https://github.com/farhan8igib), Jurga Mituzaitė, and
Stanislav Ott.

## Testing

To test DABEST, you need to install
[pytest](https://docs.pytest.org/en/latest) and
[nbdev](https://nbdev.fast.ai/).

- Run `pytest` in the root directory of the source distribution. This
  runs the test suite in the folder `dabest/tests/mpl_image_tests`.
- Run `nbdev_test` in the root directory of the source distribution.
  This runs the value assertion tests in parent folder `dabest/tests`

The test suite ensures that the bootstrapping functions and the plotting
functions perform as expected.

For detailed information, please refer to the [test
folder](nbs/tests/README.md)

## DABEST in other languages

DABEST is also available in R
([dabestr](https://github.com/ACCLAB/dabestr)) and Matlab
([DABEST-Matlab](https://github.com/ACCLAB/DABEST-Matlab)).
