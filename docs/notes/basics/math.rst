####
Math
####

Intro
=====

Matrix Multiplication
=====================

.. math::
    \text{if }\mathbf {A}\text{ is an }m \times n\text{ matrix and }\mathbf {B}\text{ is an }n \times p \text{ matrix, then the matrix multiplication is }\mathbf {C} = \mathbf {AB}\text{ where }\mathbf {C}\text{ is a }m \times p\text{ matrix.}

.. math::
    {\displaystyle \mathbf {A} ={\begin{pmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{m1}&a_{m2}&\cdots &a_{mn}\\\end{pmatrix}},\quad \mathbf {B} ={\begin{pmatrix}b_{11}&b_{12}&\cdots &b_{1p}\\b_{21}&b_{22}&\cdots &b_{2p}\\\vdots &\vdots &\ddots &\vdots \\b_{n1}&b_{n2}&\cdots &b_{np}\\\end{pmatrix}},\quad \mathbf {C} ={\begin{pmatrix}c_{11}&c_{12}&\cdots &c_{1p}\\c_{21}&c_{22}&\cdots &c_{2p}\\\vdots &\vdots &\ddots &\vdots \\c_{m1}&c_{m2}&\cdots &c_{mp}\\\end{pmatrix}}}

.. math::
    \text{where }{\displaystyle c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+\cdots +a_{in}b_{nj}=\sum _{k=1}^{n}a_{ik}b_{kj},}\\
    \text{ for } i=1, ..., m \text{ and } j=1, ..., p

.. math::
    {\displaystyle \mathbf {C} ={\begin{pmatrix}a_{11}b_{11}+\cdots +a_{1n}b_{n1}&a_{11}b_{12}+\cdots +a_{1n}b_{n2}&\cdots &a_{11}b_{1p}+\cdots +a_{1n}b_{np}\\a_{21}b_{11}+\cdots +a_{2n}b_{n1}&a_{21}b_{12}+\cdots +a_{2n}b_{n2}&\cdots &a_{21}b_{1p}+\cdots +a_{2n}b_{np}\\\vdots &\vdots &\ddots &\vdots \\a_{m1}b_{11}+\cdots +a_{mn}b_{n1}&a_{m1}b_{12}+\cdots +a_{mn}b_{n2}&\cdots &a_{m1}b_{1p}+\cdots +a_{mn}b_{np}\\\end{pmatrix}}}

Convolution
===========

Continuous Convolution
----------------------

.. math::
    {\displaystyle f(t)*g(t)\mathrel {:=} \underbrace {\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau } _{(f*g)(t)}}

Discrete Convolution
--------------------

.. math::
    {\displaystyle (f*g)[n]=\sum _{m=-\infty }^{\infty }f[m]g[n-m]}