import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import math
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    return math, mo, np, pd, plt


@app.cell
def _(mo):
    mo.md(r"""
    # 第 10 章 10.1 节：Taylor 多项式

    在 $x=a$ 附近，函数可以用
    $$T_n(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k$$
    近似。线性近似是切线，割线可以用来观察局部线性化。
    """)
    return


@app.cell
def _(mo):
    center = mo.ui.slider(start=-2, stop=2, step=0.1, value=0, label="center a")
    order = mo.ui.dropdown(options={str(item): item for item in range(1, 9)}, value="4", label="order n")
    mo.hstack([center, order])
    return center, order


@app.cell
def _(math, np, pd, plt, center, order):
    _a = center.value
    _n = order.value
    _x = np.linspace(-2.5, 2.5, 501)
    _functions = {
        "cos(x)": (np.cos, lambda x: sum(((-1) ** k) * x ** (2 * k) / math.factorial(2 * k) for k in range(_n + 1))),
        "sin(x)": (np.sin, lambda x: sum(((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1) for k in range(_n + 1))),
        "exp(x)": (np.exp, lambda x: sum(x**k / math.factorial(k) for k in range(_n + 1))),
    }
    _fig, _axes = plt.subplots(1, 3, figsize=(13, 4))
    _rows = []
    for _axis, (_name, (_function, _polynomial)) in zip(_axes, _functions.items()):
        _actual = _function(_x)
        _approx = _polynomial(_x - _a)
        _axis.plot(_x, _actual, color="#176b87", label="f(x)")
        _axis.plot(_x, _approx, color="#d95f02", linestyle="--", label=f"T{_n}(x-a)")
        _axis.axvline(_a, color="#16805b", alpha=0.5)
        _axis.set_title(_name)
        _axis.grid(alpha=0.2)
        _axis.legend()
        _rows.append({"function": _name, "error at a+0.2": abs(_function(_a + 0.2) - _polynomial(0.2))})
    _fig.tight_layout()
    print(pd.DataFrame(_rows).to_string(index=False))
    _fig
    return


if __name__ == "__main__":
    app.run()
