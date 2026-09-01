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
    mo.md(r"""
    # 第 11 章 11.1 节：微分方程简介

    微分方程把未知函数与它的导数联系起来。一阶方程只涉及 $y'$，二阶方程涉及 $y''$。

    例：$y'=100-y$ 的平衡解为 $y=100$。初值 $y(0)=y_0$ 的解是
    $$y(t)=100+(y_0-100)e^{-t}.$$
    """)
    return


@app.cell
def _(np, plt):
    _t = np.linspace(0, 6, 301)
    _fig, _ax = plt.subplots(figsize=(9, 4.5))
    for _initial in [0, 40, 140]:
        _y = 100 + (_initial - 100) * np.exp(-_t)
        _ax.plot(_t, _y, label=f"y(0)={_initial}")
    _ax.axhline(100, color="#d95f02", linestyle="--", label="equilibrium")
    _ax.set(xlabel="t", ylabel="y(t)", title="Solutions of y' = 100 - y")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
