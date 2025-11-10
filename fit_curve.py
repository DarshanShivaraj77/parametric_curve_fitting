import numpy as np
import pandas as pd
from scipy.optimize import least_squares
import matplotlib.pyplot as plt

data = pd.read_csv("xy_data.csv", header=None, names=["x", "y"])
data = data.apply(pd.to_numeric, errors="coerce").dropna()
data["t"] = np.linspace(6, 60, len(data))

x = data["x"].values
y = data["y"].values
t = data["t"].values

def model(params, t):
    theta, M, X = params
    x_pred = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y_pred = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x_pred, y_pred

def residuals(params, t, x, y):
    x_pred, y_pred = model(params, t)
    return np.concatenate([(x - x_pred), (y - y_pred)])

bounds = ([np.deg2rad(0), -0.05, 0], [np.deg2rad(50), 0.05, 100])
initial_guess = [np.deg2rad(25), 0, 50]

result = least_squares(residuals, initial_guess, bounds=bounds, args=(t, x, y))

theta_opt, M_opt, X_opt = result.x
print("θ =", np.rad2deg(theta_opt))
print("M =", M_opt)
print("X =", X_opt)

x_fit, y_fit = model(result.x, t)

plt.plot(x, y, 'o', label='Data')
plt.plot(x_fit, y_fit, '-', label='Fitted')
plt.legend()
plt.show()
