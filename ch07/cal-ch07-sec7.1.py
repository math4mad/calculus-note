import marimo

__generated_with = "0.24.0"
app = marimo.App()


@app.cell
def _():
    # 第 7 章 7.1 节：代换式积分方法
    return


@app.cell
def _():
    import marimo as mo
    from sympy import symbols, integrate, Integral
    from sympy import cos
    from sympy.abc import e

    mo
    return Integral, cos, e, integrate, mo, symbols


@app.cell
def _(Integral, cos, symbols):
    x,y=symbols("x y")

    func_expr=3*(x**2)*cos(x**3)

    Integral(func_expr)

    return func_expr, x, y


@app.cell
def _(Integral, func_expr):
    Integral(func_expr).doit()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ##  intergrate by parts
    """)
    return


@app.cell
def _(e, integrate, y):
    func_expr2 = y * (e**y)
    integrate(func_expr2, y)
    return


@app.cell
def _(x):
    from sympy import log
    func_expr3=log(x)
    func_expr3
    return func_expr3, log


@app.cell
def _(Integral, func_expr3, x):
    Integral(func_expr3, (x, 2, 3))
    return


@app.cell
def _(Integral, func_expr3, x):
    Integral(func_expr3, (x, 2, 3)).doit()
    return


@app.cell
def _(log, x):
    func_expr4=(x**6)*log(x)

    func_expr4
    return (func_expr4,)


@app.cell
def _(Integral, mo):
    def integ_steps(expr):
        """
        display  integrate of function , inlcude
        serval steps
        """
        return (expr,"==>",Integral(expr),"==>",Integral(expr).doit())


    def integ_steps_in_morimo(expr,mo=mo,direction="h"):
        """
         expr: function sympy expression 
         mo : marimo object
         direction : h: horiztanl display
                     v: vertical display
        """
        if direction =="h":
            return  mo.hstack(integ_steps(expr))
        if direction =="v": 
           return mo.vstack(integ_steps(expr))

    return integ_steps, integ_steps_in_morimo


@app.cell
def _(func_expr4, integ_steps, mo):
    from sympy import latex

    _product_rule = mo.md(r"""**Product rule:** $d(uv)=u\,dv+v\,du$

    For $u=\log(x)$ and $dv=x^6dx$: $du=\frac{1}{x}dx$, $v=\frac{x^7}{7}$.
    """)
    _steps = [
        mo.md(f"${latex(item)}$") if item != "==>" else mo.md("$\\Rightarrow$")
        for item in integ_steps(func_expr4)
    ]
    mo.vstack([_product_rule, mo.hstack(_steps)])
    return


@app.cell
def _(func_expr3, integ_steps_in_morimo):
    integ_steps_in_morimo(func_expr3)
    return


@app.cell
def _(integ_steps_in_morimo, x):
    from sympy import  exp, erf

    func_expr5=exp(-x**2)*erf(x)
    integ_steps_in_morimo(func_expr5)

    return (exp,)


@app.cell
def _(exp, x):

    from sympy import  sin
    from sympy.integrals.manualintegrate import integral_steps

    #repr(integral_steps(exp(x) / (1 + exp(2 * x)), x)))
    #print(repr(integral_steps(sin(x), x)))
    #print(repr(integral_steps((x**2 + 3)**2, x)))

    # @Agents: expand each integral_steps result into a readable horizontal derivation.
    integral_steps(exp(x) / (1 + exp(2 * x)), x)
    return


if __name__ == "__main__":
    app.run()
