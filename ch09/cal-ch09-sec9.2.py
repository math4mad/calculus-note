import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    return mo, np, pd


@app.cell
def _(mo):
    mo.md("""
    # 第 9 章 9.2 节：几何级数

    有限几何和为
    $$a+ar+\\cdots+ar^{n-1}=\\frac{a(1-r^n)}{1-r},\\qquad r\\ne1.$$

    当 $|r|<1$ 时，无穷几何和为 $a/(1-r)$。
    """)
    return


@app.cell
def _(mo, np, pd):
    _dose_number = np.array([1, 2, 5, 10, 100, 1000, 10000])
    _amount = 250 * (1 - 0.04**_dose_number) / (1 - 0.04)
    _data = pd.DataFrame({"dose number": _dose_number, "total amount": _amount})
    mo.ui.table(_data)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 定期存款

    每期存入 $1000$、增长率为 $5\\%$ 时，第 $n$ 期余额可写为
    $$B_n=\\frac{1000((1.05)^n-1)}{1.05-1}.$$
    """)
    return


if __name__ == "__main__":
    app.run()
