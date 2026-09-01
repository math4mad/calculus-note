import marimo

__generated_with = "0.17.2"

app = marimo.App(width="medium")

@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    return mo, np, pd, plt


@app.cell
def __(mo):
    mo.md(
        r"""# 第 1 章 1.1 节：函数和变化

        一个函数由定义域、值域和从定义域到值域的映射规则组成。数学公式只是描述映射规则的一种方便方式。
        本节用数值、文字、公式和图形四种方式观察函数。
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""## 降雪量函数

        下表记录了连续 14 天的降雪量。每天对应一个测量值，因此这是一个从时间到降雪量的函数，
        即使我们没有找到一个描述天气变化的数学公式。
        """
    )
    return


@app.cell
def __(np, pd):
    day = np.arange(1, 15)
    snowfall = np.array(
        [22.1, 0.2, 0, 0.7, 1.3, 0, 16.2, 0, 0, 0.8, 0, 0.9, 7.4, 14.8]
    )
    snowfall_data = pd.DataFrame({"day": day, "snowfall": snowfall})
    return day, snowfall, snowfall_data


@app.cell
def __(mo, snowfall_data):
    mo.ui.table(snowfall_data)
    return


@app.cell
def __(day, snowfall, plt):
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.scatter(day, snowfall, color="#176b87", s=52, label="snowfall")
    _ax.set(
        xlabel="time (day)",
        ylabel="snowfall",
        xticks=day,
        title="Daily snowfall",
    )
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def __(mo):
    mo.md(
        r"""## 雪树蟋蟀的鸣叫频率

        当环境温度高于 $40\,°F$ 时，雪树蟋蟀每分钟的鸣叫次数可以用
        $c = 4t - 160$ 描述；温度低于 $40\,°F$ 时，鸣叫频率取 $0$。
        这里 $t$ 是温度，$c$ 是因变量。
        """
    )
    return


@app.cell
def __(mo):
    range_choice = mo.ui.dropdown(
        options={"前 40 个点的数据": "first", "末尾 40 个点的数据": "last"},
        value="前 40 个点的数据",
        label="显示数据：",
    )
    range_choice
    return (range_choice,)


@app.cell
def __(np, pd, range_choice):
    def cricket_rate(temperature):
        return 0 if temperature < 40 else 4 * temperature - 160

    temperature = np.arange(0, 141)
    cricket_data = pd.DataFrame(
        {
            "temperature": temperature,
            "chirp_rate": [cricket_rate(value) for value in temperature],
        }
    )
    selected_data = (
        cricket_data.head(40)
        if range_choice.value == "前 40 个点的数据"
        else cricket_data.tail(40)
    )
    return cricket_data, selected_data


@app.cell
def __(mo, selected_data):
    mo.ui.table(selected_data)
    return


@app.cell
def __(cricket_data, plt):
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(
        cricket_data["temperature"],
        cricket_data["chirp_rate"],
        color="#d95f02",
        linewidth=2.5,
        label=r"$c = 4t - 160$ for $t \geq 40$",
    )
    _ax.axvline(40, color="#555555", linewidth=1, linestyle="--", alpha=0.7)
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.set(xlabel="temperature (°F)", ylabel="chirps per minute")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def __(mo):
    mo.md(
        r"""## 函数簇

        线性函数的一般形式是 $y=f(x)=b+mx$。其中 $b$ 是截距，$m$ 是斜率；
        固定 $m$ 或 $b$ 的不同取值，就得到一个函数簇。
        """
    )
    return


@app.cell
def __(np, plt):
    _x_values = np.linspace(-3, 3, 601)
    _slopes = [-0.5, -1, -2, 2, 1, 0.5]
    _fig, _ax = plt.subplots(figsize=(7, 5))
    for _slope in _slopes:
        _ax.plot(_x_values, _slope * _x_values, label=f"y = {_slope:g}x")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.set(xlim=(-3, 3), ylim=(-3, 3), title="The family y = mx")
    _ax.set_aspect("equal")
    _ax.grid(alpha=0.2)
    _ax.legend(loc="lower right", fontsize=9)
    _fig.tight_layout()
    _fig
    return


@app.cell
def __(np, plt):
    _x_values = np.linspace(-3, 3, 601)
    _intercepts = [-2, -1, 0, 1, 2]
    _fig, _ax = plt.subplots(figsize=(7, 5))
    for _intercept in _intercepts:
        _ax.plot(
            _x_values,
            _intercept + _x_values,
            label=f"y = x {_intercept:+g}",
        )
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.set(xlim=(-3, 3), ylim=(-3, 3), title="The family y = x + b")
    _ax.set_aspect("equal")
    _ax.grid(alpha=0.2)
    _ax.legend(loc="lower right", fontsize=9)
    _fig.tight_layout()
    _fig
    return


@app.cell
def __(mo):
    mo.md(
        r"""## 递增和递减函数

        对于函数 $y=f(x)$，随着 $x$ 增加而增加的函数是递增函数，随着 $x$ 增加而减小的函数是递减函数。
        下面用带有正弦扰动的线性函数作示意：
        """
    )
    return


@app.cell
def __(np, plt):
    _x_values = np.linspace(0, 50, 501)
    _increasing = np.sin(0.5 * _x_values) + _x_values
    _decreasing = np.sin(0.5 * _x_values) - _x_values
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True)
    _axes[0].plot(_x_values, _increasing, color="#c0392b")
    _axes[0].set_title("Increasing")
    _axes[1].plot(_x_values, _decreasing, color="#16805b")
    _axes[1].set_title("Decreasing")
    for _axis in _axes:
        _axis.set_xlabel("x")
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
