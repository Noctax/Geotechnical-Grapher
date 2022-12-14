import streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def streamlit_PDL():
    st.title(f"PDL Grapher")
    # >>--------Upload:-------------------Upload:-------------------Upload:-------------------Upload:----------<<
    st.header('1) Upload your file :')
    uploaded_file = st.file_uploader(label="", type=["csv", "xlsx"])
    global df
    if uploaded_file is not None:
        print(uploaded_file)
        print("Data uploaded successfully")
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)

    # >>--------SideBar:-------------------SideBar:-------------------SideBar:-------------------SideBar:----------<<
    st.header('2) Select variables :')
    first_column, second_column = st.columns(2)
    with first_column:
        Mask = st.selectbox("Select your PDL",
                            options=df["Code"].drop_duplicates(inplace=False).unique())
        if Mask:
            st.success('You selected ' + Mask)
        else:
            st.warning('No option is selected')

    with second_column:
        Color = st.selectbox(
            'How would you like to be contacted?',
            ("Black", 'Red', 'Blue', 'Green', 'Orange', 'Yellow', 'Purple'))
        if Mask:
            st.success('You selected ' + Color + " as your Line color")
        else:
            st.warning('No option is selected')

    # >>--------Visualization:-----------Visualization:-----------Visualization:---------------Visualization:-------<<
    st.header('3)  Data visualization :')

    font1 = {'family': 'arial', 'color': 'Black', 'size': 14}
    font2 = {'family': 'arial', 'color': 'Black', 'size': 10}
    Y = df.loc[df['Code'] == Mask]['Profondeur (m)']
    X = df.loc[df['Code'] == Mask]['Résistance de pointe (bars)']
    x_max = df['Résistance de pointe (bars)'].max()
    y_max = df['Profondeur (m)'].max()

    # round up function for X and Y axis
    def round_up_y(n, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier

    def round_up_x(n):
        return int(math.ceil(n / 100.0)) * 100

    x_max = round_up_x(int(x_max))
    y_max = round_up_y(y_max)

    st.header('Plot of Data')
    fig, ax = plt.subplots(1, 1)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    plt.plot(X, Y, color=Color, label=Mask)
    plt.title("Essai au pénétromètre dynamique : " + Mask, fontdict=font1, pad=20)
    plt.xlabel("Résistance dynamique de pointe (Bars)", fontdict=font2)
    plt.ylabel("Profondeur (m) ", fontdict=font2)
    ax = plt.gca()

    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (0), ls="", marker="v", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)

    # set axes limits
    plt.xlim(0, x_max)
    plt.ylim(0, y_max)
    ax.xaxis.set_label_position('top')
    ax.xaxis.set_ticks(np.arange(0, x_max, 50))
    ax.yaxis.set_ticks(np.arange(0, y_max, 0.5))
    plt.xlim()
    plt.ylim()

    # plotting
    plt.gca().invert_yaxis()
    plt.grid(visible=True, which='major', color='black', linestyle='-', linewidth=0.2)
    plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2, linewidth=0.2)
    plt.minorticks_on()

    # Figure set_up :
    figure = plt.gcf()
    cm = 1 / 2.54
    figure.size = (20 * cm, 10 * cm)
    figure.tight_layout(pad=2.0)
    figure.set_size_inches(8.27, 11.69)
    plt.tight_layout(pad=3)
    st.pyplot(fig)
