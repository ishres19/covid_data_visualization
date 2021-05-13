from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import BooleanFilter, CDSView, DateRangeSlider, CustomJS, BasicTickFormatter, HoverTool
from bokeh.layouts import column
from utilities import *


def death_and_cases_plot(cases_dataframe, death_dataframe, country_name, y_axis_type):
    """
    This function takes in cases dataframes, deaths dataframe, country name, and y-axis type as a parameter.
    It creates a line chart with cases and deaths of the country that is passed as a parameter. The plots y-axis type
    will either be linear or log, depending on the parameter. Then returns the plot.
    """
    # create a figure object with width and height
    death_and_cases_fig = figure(x_axis_type="datetime", y_axis_type=y_axis_type,
                                 width=1000, height=400, sizing_mode='fixed')
    # creating columnDataSource object, for the dataframes
    cases_source = ColumnDataSource(cases_dataframe)
    death_sources = ColumnDataSource(death_dataframe)
    # not use scientific numbers on Y-axis
    death_and_cases_fig.yaxis.formatter = BasicTickFormatter(use_scientific=False)
    # add a line renderer using the cases_source's two columns with a label, color and line width to the figure object
    death_and_cases_fig.line(x='Date', y=country_name, source=cases_source, color='Blue',
                             line_width=2, legend_label="Cases")
    # add another line renderer using the death_source's two columns with a label, color and line width.
    death_and_cases_fig.line(x='Date', y=country_name, source=death_sources, color='Red',
                             line_width=2, legend_label="Deaths")
    # name and field pairs for the Hover tool
    tooltips = [('Date', '@Date{%F}'), (country_name, "$y{int}")]
    # formatting scheme of date column
    formatters = {'@Date': 'datetime'}
    # create a Hover tool for the figure with the tooltips and specify the formatting scheme
    death_and_cases_fig.add_tools(HoverTool(tooltips=tooltips, formatters=formatters))
    # get rid of the default toolbar
    death_and_cases_fig.toolbar_location = None
    death_and_cases_fig.title.text = 'Covid cases and deaths'
    death_and_cases_fig.title.text_color = "midnightblue"
    death_and_cases_fig.title.text_font_size = "25px"
    death_and_cases_fig.xaxis.axis_label = 'Date'
    death_and_cases_fig.yaxis.axis_label = 'Confirmed Cases'
    return death_and_cases_fig


def plot_with_slider(dataframe, country_name, y_axis_name):
    """"
    this function takes a dataframe, y-axis name and country as a parameter,
    creates a plot with a slider and returns the plot.
    """
    # create a figure object with width and height
    plot = figure(x_axis_type="datetime", width=1000, height=400, sizing_mode='fixed')
    # creating columnDataSource object, for the dataframes
    source = ColumnDataSource(dataframe)
    # initialize the min and max value of the date
    init_value = (dataframe['Date'].min(), dataframe['Date'].max())
    # configuring date range slider with start date end date and value
    date_range_slider = DateRangeSlider(start=init_value[0], end=init_value[1], value=init_value)
    date_filter = BooleanFilter(booleans=[True] * dataframe.shape[0])
    # not use scientific numbers on Y-axis
    plot.yaxis.formatter = BasicTickFormatter(use_scientific=False)

    date_range_slider.js_on_change("value", CustomJS(args=dict(f=date_filter, cases_source=source), code="""\
                                           const [start, end] = cb_obj.value;
                                           f.booleans = Array.from(cases_source.data['Date']).map(d => (d >= start 
                                           && d <= end));
                                           // Needed because of https://github.com/bokeh/bokeh/issues/7273
                                           cases_source.change.emit();
                                       """))

    # add a circle renderer using the source's two columns.
    plot.circle(x='Date', y=country_name, source=source, view=CDSView(source=source, filters=[date_filter]),
                color='Pink', line_width=0.5)
    # name and field pairs for the Hover tool
    tooltips = [('Date', '@Date{%F}'), (country_name, "$y{int}")]
    # formatting scheme of date column
    formatters = {'@Date': 'datetime'}
    # create a Hover tool for the figure with the tooltips and specify the formatting scheme
    plot.add_tools(HoverTool(tooltips=tooltips, formatters=formatters, mode='vline'))
    plot.title.text_color = "midnightblue"
    plot.title.text_font_size = "25px"
    plot.toolbar.active_drag = None
    plot.toolbar_location = None
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = y_axis_name

    return column(plot, date_range_slider)


def compare_countries_cumulative_per_million(cases_dataframe, country1, country2):
    """
    This function takes cases dataframe, country1, country2 as a parameter, creates a line plot for the cases of the
    two countries and returns the plot.
    """
    # convert the values of the dataframe to per million
    converted_dataframe = convert_data_to_per_million(cases_dataframe)
    # create a figure object with width and height
    compare_countries_plot = figure(x_axis_type="datetime", width=1000, height=400, sizing_mode='fixed')
    # creating columnDataSource object, for the dataframes
    cases_source = ColumnDataSource(converted_dataframe)
    compare_countries_plot.yaxis.formatter = BasicTickFormatter(use_scientific=False)
    # add a circle renderers using the source's two columns.
    compare_countries_plot.line(x='Date', y=country1, source=cases_source, color='Green',
                                line_width=2, legend_label=country1)
    compare_countries_plot.line(x='Date', y=country2, source=cases_source, color='purple',
                                line_width=2, legend_label=country2)
    compare_countries_plot.xaxis.axis_label = 'Date'
    compare_countries_plot.yaxis.axis_label = 'Cases'
    compare_countries_plot.toolbar_location = None
    return compare_countries_plot


