from mypythontools import pyvueeel
from mypythontools.pyvueeel import expose
import pyodbc
import plotly as pl
import mypythontools
from pathlib import Path


@expose
def get_plot():

    # encoded_params = mypythontools.pyvueeel.json_to_py(sdf)

    # to delete
    # import store

    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.randn(10000, 3))

    # store.df = pd.DataFrame(np.random.randn(10000, 3))

    return mypythontools.pyvueeel.to_vue_plotly(df)


# Expose python functions to Js with decorator
@expose
def nacti_graf(promenna, pocet_zaznamu, casovani):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP %d %s FROM PLC.dbo.int ORDER BY Timing DESC"""
        % (pocet_zaznamu, promenna)
    )
    ypsilons = cursor.fetchall()

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP %d %s FROM PLC.dbo.int ORDER BY Timing DESC"""
        % (pocet_zaznamu, casovani)
    )
    xes = cursor.fetchall()

    ypsilons_as_list = [x for y in ypsilons for x in y]
    xes_as_list = [x for y in xes for x in y]

    print(ypsilons_as_list)
    print(xes_as_list)

    fig = pl.graph_objs.Figure()

    fig.add_trace(
        pl.graph_objs.Scatter(
            x=xes_as_list,
            y=ypsilons_as_list,
        )
    )
    fig.layout.update(
        yaxis=dict(title=promenna),
        legend_orientation="h",
        paper_bgcolor="#d9f0e8",
        hoverlabel={"namelength": -1},
        height=800,
        width=1600,
        margin={"b": 35, "t": 35, "pad": 4},
    )
    fig.show()
    plot_div = pl.offline.plot(fig, include_plotlyjs=False, output_type="div")

    #                  'content', 'into_paragraph', 'id_parent', 'id_created', 'label', 'added_class'
    pyvueeel.eel.add_HTML_element(
        plot_div, False, "plot_container", "plot", "Interactive plot", ["plot"]
    )
    pyvueeel.eel.execute("plot_container")
    conn.close()
    return 0


@expose
def load_data(neznama):
    # You can return dict - will be object in js
    # You can return list - will be an array in js

    print(666)

    return neznama

    # return {'Hello': 1}


@expose
def nacti_z_db(promenna, pocet_zaznamu):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP %d %s FROM PLC.dbo.bool ORDER BY Timing DESC"""
        % (pocet_zaznamu, promenna)
    )
    rows = cursor.fetchall()
    rows_as_list = [x for y in rows for x in y]
    for row in rows_as_list:
        print(row)
    conn.close()
    return rows_as_list[0] * 1


@expose
def nacti_switch(
    promenna1,
    promenna2,
    promenna3,
    promenna4,
    promenna5,
    promenna6,
    promenna7,
    pocet_zaznamu,
):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP %d %s,%s,%s,%s,%s,%s,%s FROM PLC.dbo.bool ORDER BY Timing DESC"""
        % (
            pocet_zaznamu,
            promenna1,
            promenna2,
            promenna3,
            promenna4,
            promenna5,
            promenna6,
            promenna7,
        )
    )
    rows = cursor.fetchone()
    print(rows)
    conn.close()
    return list(rows)


@expose
def nacti_slider(
    promenna1,
    promenna2,
    promenna3,
    promenna4,
    promenna5,
    promenna6,
    promenna7,
    pocet_zaznamu,
):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP %d %s,%s,%s,%s,%s,%s,%s FROM PLC.dbo.int ORDER BY Timing DESC"""
        % (
            pocet_zaznamu,
            promenna1,
            promenna2,
            promenna3,
            promenna4,
            promenna5,
            promenna6,
            promenna7,
        )
    )
    rows = cursor.fetchone()
    print(rows)
    conn.close()
    return list(rows)


# End of file
if __name__ == "__main__":
    pyvueeel.run_gui()
