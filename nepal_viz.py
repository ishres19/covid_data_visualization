from datetime import date, datetime
from bokeh.models import ColumnDataSource, BooleanFilter, CDSView,  BoxAnnotation, DateRangeSlider, Span
from individual_country import *


def nepal_cases_with_events(cases_dataframe):
    """
    This function, creates a plot showing number of cases vs date (time), with
    vertical lines and annotation blocks showing major festivals and events
    """
    # create a figure object with width and height
    cases_with_events_plot = figure(x_axis_type="datetime", width=1000, height=400, sizing_mode='fixed')
    # creating columnDataSource object, for the dataframes
    cases_source = ColumnDataSource(cases_dataframe)
    init_value = (cases_dataframe['Date'].min(), cases_dataframe['Date'].max())
    # configuring date range slider with start date end date and value
    date_range_slider = DateRangeSlider(start=init_value[0], end=init_value[1], value=init_value)
    date_filter = BooleanFilter(booleans=[True] * cases_dataframe.shape[0])
    # not use scientific numbers on Y-axis
    cases_with_events_plot.yaxis.formatter = BasicTickFormatter(use_scientific=False)
    # whenever a slider value updates. The date range sliders, value changes.
    date_range_slider.js_on_change("value", CustomJS(args=dict(f=date_filter, cases_source=cases_source), code="""\
                                          const [start, end] = cb_obj.value;
                                          f.booleans = Array.from(cases_source.data['Date']).map(d => (d >= start 
                                          && d <= end));
                                          // Needed because of https://github.com/bokeh/bokeh/issues/7273
                                          cases_source.change.emit();
                                      """))
    # name and field pairs for the Hover tool
    tooltips = [('Date', '@Date{%F}'), ('Nepal', "@Nepal")]
    # formatting scheme of date column
    formatters = {'@Date': 'datetime'}
    # create a Hover tool for the figure with the tooltips and specify the formatting scheme
    cases_with_events_plot.add_tools(HoverTool(tooltips=tooltips, formatters=formatters, mode='vline'))
    cases_with_events_plot.title.text = 'Confirmed covid Cases'
    cases_with_events_plot.title.text_color = "midnightblue"
    cases_with_events_plot.title.text_font_size = "25px"
    cases_with_events_plot.xaxis.axis_label = 'Date'
    cases_with_events_plot.yaxis.axis_label = 'Confirmed Casees'

    # add a line renderer using the cases_source's two columns with a label, color and line
    cases_with_events_plot.circle(x='Date', y='Nepal', source=cases_source,
                                  view=CDSView(source=cases_source, filters=[date_filter]),
                                  color='purple', line_width=0.5)

    # create a box annotation between the left date to the right date.
    first_lockdown_mid = BoxAnnotation(top=400000, left=datetime(2020, 3, 24).timestamp() * 1000,
                                       right=datetime(2020, 7, 21).timestamp() * 1000,
                                       fill_alpha=0.1, fill_color='gray')
    # add the box annotation to the plot
    cases_with_events_plot.renderers.extend([first_lockdown_mid])
    # label the box annotation in the legend
    cases_with_events_plot.square(legend_label="Lockdown", color='gray')
    # create a box annotation between the left date to the right date.
    tihar = BoxAnnotation(top=400000, left=datetime(2020, 11, 13).timestamp()*1000,
                          right=datetime(2020, 11, 17).timestamp()*1000,
                          fill_alpha=0.1, fill_color='blue')
    # add the box annotation to the plot
    cases_with_events_plot.renderers.extend([tihar])
    # label the box annotation in the legend
    cases_with_events_plot.square(legend_label="Tihar", color='blue')
    # create a box annotation between the left date to the right date.
    dashain = BoxAnnotation(top=400000, left=datetime(2020, 10, 23).timestamp()*1000,
                            right=datetime(2020, 10, 27).timestamp()*1000,
                            fill_alpha=0.1, fill_color='red')
    # add the box annotation to the plot
    cases_with_events_plot.renderers.extend([dashain])
    # label the box annotation in the legend
    cases_with_events_plot.square(legend_label="Dashain", color='pink')
    # create a span
    indra_jatra = Span(location=date(2020, 9, 1), dimension='height', line_color='Yellow',
                       line_dash='dashed', line_width=1.5)
    # label the span in the legend
    cases_with_events_plot.line(legend_label="Indra Jatra", line_dash=[4, 4],
                                line_color="yellow", line_width=2)
    # add the span to the plot
    cases_with_events_plot.add_layout(indra_jatra)
    # create a span
    wedding_season = Span(location=date(2021, 3, 23),
                          dimension='height', line_color='orange',
                          line_dash='dashed', line_width=1.5)
    # label the span in the legend
    cases_with_events_plot.line(legend_label="Wedding season begins", line_dash=[4, 4],
                                line_color="orange", line_width=2)
    # add the span to the plot
    cases_with_events_plot.add_layout(wedding_season)

    cases_with_events_plot.line(legend_label="Beginning of Pahachare", line_dash=[4, 4],
                                line_color="Blue", line_width=2)
    pahachare = Span(location=date(2021, 4, 10),
                     dimension='height', line_color='blue',
                     line_dash='dashed', line_width=1.5)
    cases_with_events_plot.add_layout(pahachare)

    cases_with_events_plot.line(legend_label="Holi", line_dash=[4, 4],
                                line_color="brown", line_width=2)
    holi = Span(location=date(2021, 3, 28),
                dimension='height', line_color='brown',
                line_dash='dashed', line_width=1.5)
    cases_with_events_plot.add_layout(holi)

    cases_with_events_plot.line(legend_label="Biska Jatra", line_dash=[4, 4],
                                line_color="purple", line_width=2)
    biska_jatra = Span(location=date(2021, 4, 13),
                       dimension='height', line_color='purple',
                       line_dash='dashed', line_width=1.5)
    cases_with_events_plot.add_layout(biska_jatra)

    cases_with_events_plot.line(legend_label="Nepali New Year", line_dash=[4, 4],
                                line_color="Green", line_width=2)
    nepali_new_year = Span(location=date(2021, 4, 14),
                           dimension='height', line_color='Green',
                           line_dash='dashed', line_width=1.5)
    cases_with_events_plot.add_layout(nepali_new_year)

    cases_with_events_plot.line(legend_label="Machendranath Jatra", line_dash=[4, 4],
                                line_color="red", line_width=2)
    machendranath = Span(location=date(2021, 4, 20),
                         dimension='height', line_color='red',
                         line_dash='dashed', line_width=1.5)
    cases_with_events_plot.add_layout(machendranath)

    cases_with_events_plot.line(legend_label="Inauguration of Dharahara", line_dash=[4, 4],
                                line_color="black", line_width=2)
    inauguration = Span(location=date(2021, 4, 24),
                        dimension='height', line_color='black',
                        line_dash='dashed', line_width=1.5)
    cases_with_events_plot.add_layout(inauguration)
    # remove the toolbar
    cases_with_events_plot.toolbar_location = None
    cases_with_events_plot.legend.location = "left"
    return column(cases_with_events_plot, date_range_slider)

