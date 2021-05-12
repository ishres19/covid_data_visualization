from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import BooleanFilter, CDSView, DateRangeSlider, CustomJS, BasicTickFormatter, HoverTool
from bokeh.layouts import column
from data_viz import *


def death_and_cases_plot(cases_dataframe, death_dataframe, country_name, y_axis_type):
    """
    This function returns a linear line chart with cases and deaths over time in Nepal.
    """
    death_and_cases_fig = figure(x_axis_type="datetime", y_axis_type = y_axis_type, width=1000, height=400, sizing_mode='fixed')
    cases_source = ColumnDataSource(cases_dataframe)
    death_sources = ColumnDataSource(death_dataframe)
    death_and_cases_fig.yaxis.formatter = BasicTickFormatter(use_scientific=False)

    death_and_cases_fig.line(x='Date', y=country_name, source=cases_source, color='Blue',
                             line_width=2, legend_label="Cases")
    death_and_cases_fig.line(x='Date', y=country_name, source=death_sources, color='Red',
                             line_width=2, legend_label="Deaths")

    tooltips = [('Date', '@Date{%F}'), (country_name, "@"+country_name)]
    formatters = {'@Date': 'datetime'}
    death_and_cases_fig.add_tools(HoverTool(tooltips=tooltips, formatters=formatters))

    death_and_cases_fig.toolbar_location = None

    death_and_cases_fig.title.text = 'Covid cases and deaths'
    death_and_cases_fig.title.text_color = "midnightblue"
    death_and_cases_fig.title.text_font_size = "25px"
    death_and_cases_fig.xaxis.axis_label = 'Date'
    death_and_cases_fig.yaxis.axis_label = 'Confirmed Cases'
    return death_and_cases_fig


def plot_with_slider(cases_dataframe, country_name, y_axis_name):
    """"
    this function, creates a plot showing number of cases vs date (time), with
    vertical lines and annotation blocks showing major festivals and events
    """
    cases_plot = figure(x_axis_type="datetime", width=1000, height=400, sizing_mode='fixed')
    init_value = (cases_dataframe['Date'].min(), cases_dataframe['Date'].max())
    date_range_slider = DateRangeSlider(start=init_value[0], end=init_value[1], value=init_value)
    source1 = ColumnDataSource(cases_dataframe)
    date_filter = BooleanFilter(booleans=[True] * cases_dataframe.shape[0])
    cases_plot.yaxis.formatter = BasicTickFormatter(use_scientific=False)

    date_range_slider.js_on_change("value", CustomJS(args=dict(f=date_filter, source1=source1), code="""\
                                          const [start, end] = cb_obj.value;
                                          f.booleans = Array.from(source1.data['Date']).map(d => (d >= start 
                                          && d <= end));
                                          // Needed because of https://github.com/bokeh/bokeh/issues/7273
                                          source1.change.emit();
                                      """))

    tooltips = [('Date', '@Date{%F}'), (country_name, "@"+country_name)]
    formatters = {'@Date': 'datetime'}

    cases_plot.add_tools(HoverTool(tooltips=tooltips, formatters=formatters, mode='vline'))
    cases_plot.title.text_color = "midnightblue"
    cases_plot.title.text_font_size = "25px"
    cases_plot.toolbar.active_drag = None
    cases_plot.toolbar_location = None
    cases_plot.xaxis.axis_label = 'Date'
    cases_plot.yaxis.axis_label = y_axis_name

    cases_plot.circle(x='Date', y=country_name, source=source1, view=CDSView(source=source1, filters=[date_filter]),
                      color='Pink', line_width=0.5)

    return column(cases_plot, date_range_slider)


def compare_countries_cumulative_per_million(cases_dataframe, country1, country2):
    converted_dataframe = convert_data_to_per_million(cases_dataframe)
    nepal_india_plot = figure(x_axis_type="datetime", width=1000, height=400, sizing_mode='fixed')
    cases_source = ColumnDataSource(converted_dataframe)
    nepal_india_plot.yaxis.formatter = BasicTickFormatter(use_scientific=False)
    nepal_india_plot.line(x='Date', y=country1, source=cases_source, color='Green', line_width=2, legend_label=country1)
    nepal_india_plot.line(x='Date', y=country2, source=cases_source, color='purple', line_width=2, legend_label=country2)
    nepal_india_plot.xaxis.axis_label = 'Date'
    nepal_india_plot.yaxis.axis_label = 'Cases'
    nepal_india_plot.toolbar_location = None
    return nepal_india_plot


