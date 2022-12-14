import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def streamlit_PMT():
    st.title(f"PMT Grapher")
    # >>--------Upload:-------------------Upload:-------------------Upload:-------------------Upload:----------<<
    st.header('1) Upload your file :')
    uploaded_file = st.file_uploader(label="", type=["csv", "xlsx"])
    global df1
    if uploaded_file is not None:
        print(uploaded_file)
        print("Data uploaded successfully")
        try:
            df1 = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df1 = pd.read_excel(uploaded_file)

    # >>--------SideBar:-------------------SideBar:-------------------SideBar:-------------------SideBar:----------<<
    st.header('2) Select variables :')
    first_column, second_column = st.columns(2)
    with first_column:
        Mask = st.selectbox("Select your PMT",
                            options=df1["Code"].drop_duplicates(inplace=False).unique())
        if Mask:
            st.success('You selected ' + Mask)
        else:
            st.warning('No option is selected')

    with second_column:
        Color = st.selectbox(
            'Select your color',
            ("Black", 'Red', 'Blue', 'Green', 'Orange', 'Yellow', 'Purple'))
        if Mask:
            st.success('You selected ' + Color + " as your Line color")
        else:
            st.warning('No option is selected')

    # >>--------Visualization:-----------Visualization:-----------Visualization:---------------Visualization:-------<<
    st.header('3)  Data visualization :')

    # subplots variables :
    font1 = {'family': 'arial', 'color': 'Black', 'size': 10}
    font2 = {'family': 'arial', 'color': 'Black', 'size': 8}
    Y = df1.loc[df1['Code'] == Mask]['Profondeur']
    X0 = df1.loc[df1['Code'] == Mask]['EM']
    X1 = df1.loc[df1['Code'] == Mask]['Pl']
    X2 = df1.loc[df1['Code'] == Mask]['Pf']
    X3 = df1.loc[df1['Code'] == Mask]['EM/Pl']

    Y_max = df1['Profondeur'].max()
    X0_max = X0.max()
    X1_max = X1.max()
    X2_max = X2.max()
    X3_max = X3.max()

    # round up function for X and Y axis
    def round_up_y(n):
        return int(math.ceil(n / 5.0)) * 5

    def round_up_x(n):
        return int(math.ceil(n / 10.0)) * 10

    X0_max = round_up_x(int(X0_max))
    X1_max = round_up_x(int(X1_max))
    X2_max = round_up_x(int(X2_max))
    X3_max = round_up_x(int(X3_max))
    Y_max = round_up_y(int(Y_max))

    # subplots adjust set_up :

    cm = 1 / 2.54
    fig = plt.gcf()
    fig.size = (20 * cm, 10 * cm)
    fig.tight_layout(pad=1)
    fig.subplots_adjust(top=0.87)
    fig.set_size_inches(8.27, 11.69)
    plt.suptitle("Courbes pressiométriques du sondage " + Mask + "", ha='center', fontdict=font1, y=0.97)
    fig, ax = plt.subplots(1, 3)

    plt.subplot(1, 3, 1)
    plt.plot(X0, Y, color='Orange')
    plt.xlabel("Modules pressiométriques EM (Mpa) ", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)
    ax = plt.gca()
    ax.xaxis.set_label_position('top')
    ax.xaxis.set_ticks_position('top')
    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)
    plt.xlim(0, X0_max)
    plt.ylim(0, Y_max)
    ax.xaxis.set_ticks(np.arange(0, X0_max, X0_max / 5))
    ax.yaxis.set_ticks(np.arange(0, Y_max, 5))
    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()
    plt.legend(["EM"])

    plt.subplot(1, 3, 2)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    plt.plot(X1, Y, color='Red')
    plt.plot(X2, Y, color='Blue')
    plt.xlabel("Pressions limites Pl & Pressions de fluage Pf (Mpa)", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)
    ax = plt.gca()
    ax.xaxis.set_label_position('top')
    ax.xaxis.set_ticks_position('top')
    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)
    plt.xlim(0, X1_max)
    plt.ylim(0, Y_max)
    ax.xaxis.set_ticks(np.arange(0, X1_max, X1_max / 5))
    ax.yaxis.set_ticks(np.arange(0, Y_max, 5))
    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()
    plt.legend(["Pl", "Pf"])


    plt.subplot(1, 3, 3)
    plt.plot(X3, Y, color='Green')
    plt.xlabel("Rapports EM/Pl ", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)
    ax = axes = plt.gca()
    axes.xaxis.set_label_position('top')
    ax.xaxis.set_ticks_position('top')
    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)
    plt.xlim(0, X3_max)
    plt.ylim(0, Y_max)
    ax.xaxis.set_ticks(np.arange(0, X3_max, X3_max / 5))
    ax.yaxis.set_ticks(np.arange(0, Y_max, 5))
    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()
    plt.legend(["EM/PL"])

    st.pyplot(fig)
