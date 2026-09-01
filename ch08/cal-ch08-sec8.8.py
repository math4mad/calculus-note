import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def _(mo):
    mo.md("""
    # 第 8 章 8.8 节：概率、均值与中位数

    概率密度的区间概率为
    $$\\Pr(a\\le X\\le b)=\\int_a^b p(x)dx.$$

    中位数 $T$ 满足累计概率为 $0.5$。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(2, 8, 601)
    _density = np.where(_x <= 6, 0.04 * _x, -0.06 * _x + 0.6)
    _cdf = np.where(_x <= 6, 0.02 * _x**2 - 0.08, -0.03 * _x**2 + 0.6 * _x - 1.88)
    _probability = np.interp(7, _x, _cdf) - np.interp(5, _x, _cdf)
    _median = np.interp(0.5, _cdf, _x)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_x, _density, color="#176b87")
    _axes[0].set(xlabel="catch", ylabel="p(x)", title="Fishing density")
    _axes[1].plot(_x, _cdf, color="#d95f02", label=f"P(5<X<7)={_probability:.3f}")
    _axes[1].axhline(0.5, color="#16805b", linestyle="--", label=f"median={_median:.2f}")
    _axes[1].set(xlabel="catch", ylabel="P(X <= x)", title="Cumulative probability")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
