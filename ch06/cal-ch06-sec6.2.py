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
    # 第 6 章 6.2 节：用分析方法构造反导函数

    在连通区间上，若 $F'(x)=0$，则 $F(x)=C$。若两个函数导数相同，它们相差一个常数。

    $$
    \\int x^n dx=\\frac{x^{n+1}}{n+1}+C\\ (n\\ne-1),\\qquad
    \\int\\frac{1}{x}dx=\\ln|x|+C.
    $$

    其他基本规则包括

    $$
    \\int e^x dx=e^x+C,\\qquad \\int\\cos xdx=\\sin x+C,\\qquad
    \\int\\sin xdx=-\\cos x+C.
    $$

    积分满足和差法则与常数倍法则。
    """)
    return


if __name__ == "__main__":
    app.run()
