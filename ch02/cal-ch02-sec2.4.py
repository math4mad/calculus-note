import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return mo


@app.cell
def _(mo):
    mo.md("""
    # 第 2 章 2.4 节：导数的认识

    导数可以用两种等价的记号表示：

    $$
    \\frac{\\Delta y}{\\Delta x},\\qquad \\frac{dy}{dx}\\approx\\frac{\\Delta y}{\\Delta x}.
    $$

    ## 铜矿开采成本

    设开采 $T$ 吨铜的成本为 $C=f(T)$，并且 $f'(2000)=100$。
    这表示在 $T=2000$ 附近，每增加一吨铜，成本约增加 $100$ 个成本单位。

    当增加 $5$ 吨时：

    $$
    \\Delta C\\approx f'(2000)\\Delta T=100\\times5=500.
    $$
    """)
    return


if __name__ == "__main__":
    app.run()
