from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models import BasicTickFormatter, HoverTool


def all_countries_plot(dataframe, y_axis_type):
    """
    This function takes a dataframe, the type of Y_axis you want, linear/log and creates
    a plot of all the countries in the dataframe.
    """
    # creating columnDataSource object, for the dataframe
    source = ColumnDataSource(dataframe)
    # create the figure.
    all_countries_plot = figure(x_axis_type="datetime", y_axis_type= y_axis_type,
                                width=1000, height=600, sizing_mode='fixed')
    # color of the plot
    all_countries_plot.background_fill_color = "whitesmoke"
    all_countries_plot.border_fill_color = "aliceblue"
    # not use use scientific numbers.
    all_countries_plot.yaxis.formatter = BasicTickFormatter(use_scientific=False)
    # create line graphs for each columns.
    all_countries_plot.line(x='Date', y='Afghanistan', source=source, color='Black',
                            line_width=2, legend_label="Afghanistan")
    all_countries_plot.line(x='Date', y='Bangladesh', source=source, color='green',
                            line_width=2, legend_label="Bangladesh")
    all_countries_plot.line(x='Date', y='Bhutan', source=source, color='Orange',
                            line_width=2, legend_label="Bhutan")
    all_countries_plot.line(x='Date', y='India', source=source, color='Red',
                            line_width=2, legend_label="India")
    all_countries_plot.line(x='Date', y='Maldives', source=source, color='Pink',
                            line_width=2, legend_label="Maldives")
    all_countries_plot.line(x='Date', y='Nepal', source=source, color='Blue',
                            line_width=2, legend_label="Nepal")
    all_countries_plot.line(x='Date', y='Pakistan', source=source, color='purple',
                            line_width=2, legend_label="Pakistan")
    all_countries_plot.line(x='Date', y='Sri Lanka', source=source, color='Brown',
                            line_width=2, legend_label="Sri Lanka")
    tooltips = [('Date', '@Date{%F}'), ('Bangladesh', "@Bangladesh"), ('Nepal', "@Nepal"),
                ('India', "@India"), ('Pakistan', '@Pakistan'),
                ('Bhutan', '@Bhutan'), ('Maldives', '@Maldives'),
                ('Sri Lanka', "@{Sri Lanka}"), ('Afghanistan', "@Afghanistan")]
    formatters = {'@Date': 'datetime',
                  '@{Sri Lanka}': 'printf'}
    # create a Hover tool for the figure
    all_countries_plot.add_tools(HoverTool(tooltips=tooltips, formatters=formatters))
    all_countries_plot.title.text_color = "midnightblue"
    all_countries_plot.title.text_font_size = "25px"
    all_countries_plot.xaxis.axis_label = 'Date'
    all_countries_plot.yaxis.axis_label = 'Confirmed Casees'
    all_countries_plot.legend.location = "top_left"
    # hide the plot line of the country, if the country's legend is clicked
    all_countries_plot.legend.click_policy = "hide"

    return all_countries_plot
