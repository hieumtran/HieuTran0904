Machine learning basics
=======================

Parametric and Non-parameteric methods
---------------------------------------

1. **Paramteric** approach simplifies the problems of estimating unknown target function :math:`f` to estimating a set of parameters.
Estimating a set of parameters is easier than estimating an arbitrary :math:`f`. 
One problem with this apparoch is that the model we initally choose may far from the true function form.
Therefore, our estimated function :math:`\hat{f}` perform poorly. 
A solution is to choose highly *flexible* models by adding a greater number of paramters. However, this solution may *overfit* the data.

2. Unlike **Parametric** methods, **Non-paramteric** approach does not make assumptions about :math:`f`. 
Instead, they seek an estimate of :math:`f` as close to the true data as possible. 
Since this approach does not explicitly assume a particular form of functional form for :math:`f` which can be far from the true :math:`f`,
it can potentially capture more accurately a wider range of possible shapes of target function. 
However, without reducing the problems to estimating paramters, non-parameteric method can require a large number of observations to obtain an accurate :math:`\hat{f}`.

Prediction Accuracy and Model Interpretability
----------------------------------------------

.. figure:: https://raw.githubusercontent.com/hieumtran/MLANNS/main/figure/ACCvsFLEX.PNG


Supervised, Unsupervised, and Semi-supervised Learning
------------------------------------------------------

1. **Supervised Learning** is an approach that's defined by its use of labeled datasets. It has two main types of problems:

    #. **Classification**: After the learning process, it can separate data into specific categories as output (generally discrete value). 
    For example, the algorithm can categorize between a dog and cat, given images.

    #. **Regression**: This algorithm helps to predict and understand between the dependent (continuos) an independent value. 
    For example, regression can tells the house prices, given the condition and location of the house.

2. **Unsupervised Learning** is an algorithm that analyze unlabled dataset. Even without support from human, it potentially capture hidden pattern.
It is mainly used in three main tasks:

    #. **Clustering**: It can group unlabled data based on their similarity. 
    For example, it can group people who love cat to one group and who does not love cat into one group.

    #. **Association Rule Learning**: This algorithm uses different rules to find the relationships between variables.
    For example, it can be used to find frequent pattern in transactional data.

    #. **Dimensionality Reduction**: It reduces the number of data inputs, without losing the data integrity. 
    For example, it is used iun preprocessing visual data to remnove noise.

3. **Semi-supervised Learning** is a learning problem that involves a small number of labeled examples and a large number of unlabled examples. 
Afterward, the model needs to learn and make predictions on test data.

The Bias-Variance Trade-Off
---------------------------

1. **Variance** refers to the amount by which :math:`\hat{f}` would change if we estimated it using a different training dataset. 
If a method has high variance, small changes in the training data can result in large changes in :math:`\hat{f}`. 
In other words, flexible statical methods have higher variance.

2. **Bias** refers to the error that is introduced by approximating the training data. If the :math:`\hat{f}` does fit well with the training dataset,
the result will produce in relatively low error or **Bias**. More flexible methods result in less **bias**.

More flexible computational models generally have high variance and low bias. 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


..
    Sample H4
    ---------

    Sample H5
    ^^^^^^^^^

    Sample H6
    """""""""

    # Question section
    1. What is a restrictive and flexible model?
    2. Why do they reach to the conclusion of the graph in acc vs interpret?
