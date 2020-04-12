<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Topics on Convex Optimization


HW1 (due on Jan 27th):

2.3, 2.8, 2.10, 2.11, 2.13, 2.16, 2.18, 2.20, 2.25

HW2 (due on Feb 10th):

3.5, 3.18, 3.19, 3.21, 3.23

HW3 (due on Feb 24th):

4.2, 4.5, 4.7, 4.9, 4.22

HW4 (due on Mar 9th):

5.3, 5.7, 5.11, 5.23, 5.26

HW5 (due on Mar 23rd):
9.1, 9.4, 9.7, 9.8, 9.9

HW6 (due on Apr 6th):

1. Code the Primal-Dual Interior Point algorithm for the QP under linear
   equality & inequality.
2. Code gradient descent & subgradient method for solving the logistic
   regression under ridge and lasso regularization. Compare the number of
   iterations to converge.

HW7 (due on Apr 27th)

1. Consider the fused lasso problem:

   $$\frac{1}{2}\|y- X\beta\|_2^2 + \lambda_1 \|\beta\|_1+ \lambda_2 \sum_{j=2}^p |\beta_j-\beta_{j-1}|$$

   Derive the ADMM algorithm.

2. For the graph lasso, consider augmented Lagrangian

   $$L_{\rho}(\Omega, Z, U) = tr(S\Omega) -\log\det(\Omega) + \lambda\|Z\|_1 + tr(U' (\Omega-Z))+\frac{\rho}{2} \|\Omega-Z\|_F^2$$

   where $U\in \mathbb{S}^p$ 


   (i) Write out the 3-step ADMM algorithm.

   (ii) Prove the $\Omega^+$ is the minimum in step 1.
