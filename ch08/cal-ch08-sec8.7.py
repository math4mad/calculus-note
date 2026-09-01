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
    # 第 8 章 8.7 节：分布函数

    把分组人口比例近似看作每个年龄区间内均匀分布，可以构造连续概率密度。
    密度必须非负，并且在全区间上的积分应为 $1$。
    """)
    return


@app.cell
def _(np, plt):
    _age_groups = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    _fractions = np.array([0.13, 0.14, 0.14, 0.13, 0.14, 0.14, 0.10, 0.05, 0.03])
    _age = np.linspace(0, 100, 501)
    _density = np.where(_age <= 60, 0.013, np.maximum(0, 0.0358 - 0.00038 * _age))
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].bar(_age_groups - 5, _fractions, width=9, color="#176b87")
    _axes[0].set(xlabel="age", ylabel="fraction", title="Grouped age distribution")
    _axes[1].plot(_age, _density, color="#d95f02")
    _axes[1].fill_between(_age, _density, alpha=0.2, color="#d95f02")
    _axes[1].set(xlabel="age", ylabel="p(age)", title="Approximate density")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
