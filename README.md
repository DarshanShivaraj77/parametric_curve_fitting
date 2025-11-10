
Parametric Curve Fitting
-----------------------------------------------------------------------------------------------
Problem:

Find the values of θ, M, and X for the equations:

x = t*cos(θ) - e^(M*|t|)*sin(0.3t)*sin(θ) + X  
y = 42 + t*sin(θ) + e^(M*|t|)*sin(0.3t)*cos(θ)

Ranges:  
0° < θ < 50°  
-0.05 < M < 0.05  
0 < X < 100  
6 < t < 60  

Files:
- fit_curve.py  
- xy_data.csv  
- architecture.txt  
- README.md  

Execution
Run:
python fit_curve.py

Output:
θ = 29.5823
M = -0.05
X = 55.0135


Final Equation-
(t*cos(29.5823°) - e^(-0.05|t|)*sin(0.3t)*sin(29.5823°) + 55.0135,  
42 + t*sin(29.5823°) + e^(-0.05|t|)*sin(0.3t)*cos(29.5823°))

Approach-
The dataset was fitted to the given parametric model using non-linear least squares to estimate parameters that minimize residual error.

Tools-
NumPy, Pandas, SciPy

Author-
Darshan Shivaraj
