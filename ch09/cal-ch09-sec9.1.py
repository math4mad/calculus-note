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
    # 第 9 章 9.1 节：数列

    数列可以用显式公式、递推公式和图像表示。下面比较收敛、发散和振荡的例子。
    """)
    return


@app.cell
def _(np, plt):
    _n = np.arange(1, 101)
    _sequences = [
        (0.8**_n, r"$0.8^n$"),
        ((1 - np.exp(-_n)) / (1 + np.exp(-_n)), r"$(1-e^{-n})/(1+e^{-n})$"),
        ((_n**2 + 1) / _n, r"$(n^2+1)/n$"),
        (1 + (-1) ** _n, r"$1+(-1)^n$"),
    ]
    _fig, _axes = plt.subplots(2, 2, figsize=(11, 7))
    for _axis, (_values, _title) in zip(_axes.flat, _sequences):
        _axis.scatter(_n, _values, s=12, color="#176b87")
        _axis.set_title(_title)
        _axis.set_xlabel("n")
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 递推数列

    递推关系必须给出初始值。例如 $s_n=s_{n-1}+3$、$s_1=4$ 产生等差数列。
    计算较多项时使用迭代比递归调用更稳妥。
    """)
    return


if __name__ == "__main__":
    app.run()
