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
    # 第 8 章 8.6 节：经济学中的积分应用

    复利模型为 $B=P(1+r)^t$，因此现值为
    $$P=\\frac{B}{(1+r)^t}.$$

    连续复利和连续贴现分别为
    $$B=Pe^{rt},\\qquad P=Be^{-rt}.$$
    """)
    return


if __name__ == "__main__":
    app.run()
