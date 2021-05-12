import csv
import pandas as pd
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.models import Panel, Tabs

def read_csv_file(input_file):
    """
    reads csv file, creates a dataframe and returns the dataframe
    """
    with open(input_file, encoding='utf-8-sig') as fp:
        dct = {}
        reader = csv.reader(fp)
        # next (reader)
        for row in reader:
            dct[row[0]] = row[1:]
    # change the key name from 'Country' to 'Date
    dct['Date'] = dct.pop('Country')
    # create a dataframe of the dictionary
    dataframe = pd.DataFrame(dct)
    # change the format of all other columns to int
    for column in dataframe:
        if column != 'Date':
            dataframe[column] = dataframe[column].astype(int)
    # change the format of date from string to datetime
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    # print(df.dtypes)
    return dataframe


def convert_data_to_per_million(dataframe):
    """
    This function takes a dataframe and converts all the columns of the dataframe
    into per million.
    """
    # divide each data of each country by its population and multiply by 1M to get cases/deaths per million
    afghan_population = 38000000
    dataframe['Afghanistan'] = (dataframe['Afghanistan'] / afghan_population) * 1000000
    india_population = 1393409038
    dataframe['India'] = (dataframe['India'] / india_population) * 1000000
    nepal_population = 29580750
    dataframe['Nepal'] = (dataframe['Nepal'] / nepal_population) * 1000000
    bangladesh_population = 163000000
    dataframe['Bangladesh'] = (dataframe['Bangladesh'] / bangladesh_population) * 1000000
    bhutan_population = 771608
    dataframe['Bhutan'] = (dataframe['Bhutan'] / bhutan_population) * 1000000
    maldives_population = 548610
    dataframe['Maldives'] = (dataframe['Maldives'] / maldives_population) * 1000000
    pakistan_population = 220892340
    dataframe['Pakistan'] = (dataframe['Pakistan'] / pakistan_population) * 1000000
    sri_lanka_population = 220892340
    dataframe['Sri Lanka'] = (dataframe['Sri Lanka'] / sri_lanka_population) * 1000000

    return dataframe


def find_components(plot):
    """
    This function takes the plot and returns all the components,
    necessary to embed the plot into a website.
    """
    plot = plot
    plot_script, plot_div = components(plot)
    plot_js_resources = INLINE.render_js()
    plot_css_resources = INLINE.render_css()
    return plot_script, plot_div, plot_js_resources, plot_css_resources


def tabs_for_cumulative_and_daily(cumulative_cases, daily_cases):
    """
    This function takes two plots, cumulative and daily cases, and creates tabs for it.
    """
    tab1 = Panel(child=cumulative_cases, title="Cumulative")
    tab2 = Panel(child=daily_cases, title="Daily")
    tabs = Tabs(tabs=[tab1, tab2])
    return tabs


def tabs_for_linear_and_log_plots(linear_plot, log_plot):
    tab1 = Panel(child=log_plot, title="Log")
    tab2 = Panel(child=linear_plot, title="Linear")
    tabs = Tabs(tabs=[tab1, tab2])
    return tabs


def tabs_for_death_and_cases(cases_plot, death_plot):
    tab1 = Panel(child=cases_plot, title="Cases")
    tab2 = Panel(child=death_plot, title="Deaths")
    tabs = Tabs(tabs=[tab1, tab2])
    return tabs
