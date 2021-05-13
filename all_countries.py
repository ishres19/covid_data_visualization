from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models import BasicTickFormatter, HoverTool


def all_countries_plot(dataframe, y_axis_type):
    """
    This function takes a dataframe, the type of Y_axis you want, linear/log, and creates
    a plot of all the countries in the dataframe.
    """
    # creating columnDataSource object, for the dataframe
    date_source_for_plot = ColumnDataSource(dataframe)
    # create a figure object with width and height
    all_countries_fig = figure(x_axis_type="datetime", y_axis_type=y_axis_type,
                               width=1000, height=600, sizing_mode='fixed')
    # color of the plot
    all_countries_fig.background_fill_color = "whitesmoke"
    # color of the border
    all_countries_fig.border_fill_color = "aliceblue"
    # not use scientific numbers.
    all_countries_fig.yaxis.formatter = BasicTickFormatter(use_scientific=False)
    # add a line renderer using the date_source_for_plot's two columns. Also add legend Label and color
    all_countries_fig.line(x='Date', y='Afghanistan', source=date_source_for_plot, color='Black',
                           line_width=2, legend_label="Afghanistan")
    all_countries_fig.line(x='Date', y='Bangladesh', source=date_source_for_plot, color='green',
                           line_width=2, legend_label="Bangladesh")
    all_countries_fig.line(x='Date', y='Bhutan', source=date_source_for_plot, color='Orange',
                           line_width=2, legend_label="Bhutan")
    all_countries_fig.line(x='Date', y='India', source=date_source_for_plot, color='Red',
                           line_width=2, legend_label="India")
    all_countries_fig.line(x='Date', y='Maldives', source=date_source_for_plot, color='Pink',
                           line_width=2, legend_label="Maldives")
    all_countries_fig.line(x='Date', y='Nepal', source=date_source_for_plot, color='Blue',
                           line_width=2, legend_label="Nepal")
    all_countries_fig.line(x='Date', y='Pakistan', source=date_source_for_plot, color='purple',
                           line_width=2, legend_label="Pakistan")
    all_countries_fig.line(x='Date', y='Sri Lanka', source=date_source_for_plot, color='Brown',
                           line_width=2, legend_label="Sri Lanka")
    # name and field pairs for the Hover tool
    tooltips = [('Date', '@Date{%F}'), ('Bangladesh', "@Bangladesh"), ('Nepal', "@Nepal"),
                ('India', "@India"), ('Pakistan', '@Pakistan'),
                ('Bhutan', '@Bhutan'), ('Maldives', '@Maldives'),
                ('Sri Lanka', "@{Sri Lanka}"), ('Afghanistan', "@Afghanistan")]
    # formatting scheme of date column
    formatters = {'@Date': 'datetime'}
    # create a Hover tool for the figure with the tooltips and specify the formatting scheme
    all_countries_fig.add_tools(HoverTool(tooltips=tooltips, formatters=formatters))
    all_countries_fig.title.text_color = "midnightblue"
    all_countries_fig.title.text_font_size = "25px"
    all_countries_fig.xaxis.axis_label = 'Date'
    all_countries_fig.yaxis.axis_label = 'Confirmed Cases'
    all_countries_fig.legend.location = "top_left"
    # hide the plot line of the country, if the country's legend is clicked
    all_countries_fig.legend.click_policy = "hide"

    return all_countries_fig
