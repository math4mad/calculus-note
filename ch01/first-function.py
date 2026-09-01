import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return mo


@app.cell
def _(mo):
    mo.md("# 第一个函数")
    return


if __name__ == "__main__":
    app.run()
