from flask import Flask
from flask import render_template
from datetime import timedelta
from nepal_viz import *
from individual_country import *
from all_countries import *

app = Flask(__name__)


@app.route('/')
def home():
    cumulative_cases_dataframe = read_csv_file('confirmed-covid.csv')
    daily_cases_dataframe = read_csv_file('daily_cases.csv')
    # calls all_countries_plot function and creates a log plot.
    cases_plot = all_countries_plot(cumulative_cases_dataframe, 'log')
    components_of_cases_plot = find_components(cases_plot)
    cases_plot_script = components_of_cases_plot[0]
    cases_plot_div = components_of_cases_plot[1]
    cases_plot_js_resources = components_of_cases_plot[2]
    cases_plot_css_resources = components_of_cases_plot[3]

    # converts the data to per million
    converted_data = convert_data_to_per_million(daily_cases_dataframe)
    converted_cumulative_data = convert_data_to_per_million(cumulative_cases_dataframe)
    # creates a linear plot for all countries.
    linear_daily_cases_plot = all_countries_plot(converted_data, 'linear')
    linear_cumulative_cases_plot = all_countries_plot(converted_cumulative_data, 'linear')
    # create tabs panels for two plots.
    tabs = tabs_for_cumulative_and_daily(linear_cumulative_cases_plot, linear_daily_cases_plot)
    component_of_plot = find_components(tabs)

    linear_plots_script = component_of_plot[0]
    linear_plots_div = component_of_plot[1]
    linear_plots_js_resources = component_of_plot[2]
    linear_plots_css_resources = component_of_plot[3]
    return render_template('index.html',
                           plot_script=cases_plot_script,
                           plot_div=cases_plot_div,
                           js_resources=cases_plot_js_resources,
                           css_resources=cases_plot_css_resources,

                           plot_script2=linear_plots_script,
                           plot_div2=linear_plots_div,
                           js_resource2=linear_plots_js_resources,
                           css_resources2=linear_plots_css_resources
                           )


@app.route('/Afghanistan/')
def afghanistan():
    # calls the read_csv file function and stores the dataframe
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')
    # calls the functions that makes plots
    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Afghanistan', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Afghanistan', 'log')
    # calls the function that makes tab panels
    tabs_for_linear_and_log = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)
    # finding the components of the tab panels
    components_for_linear_log = find_components(tabs_for_linear_and_log)
    # assigning the returned components
    linear_and_log_plot_script = components_for_linear_log[0]
    linear_and_log_plot_div = components_for_linear_log[1]
    linear_and_log_js_resources = components_for_linear_log[2]
    linear_and_log_css_resources = components_for_linear_log[3]

    # calling functions that make plots with a date slider
    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'Afghanistan', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'Afghanistan', 'deaths')
    # calls the function that makes tab panels
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)
    # finding the components of the tab panels
    components_for_death_and_cases = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    death_and_cases_script = components_for_death_and_cases[0]
    death_and_cases_plot_div = components_for_death_and_cases[1]
    death_and_cases_js_resources = components_for_death_and_cases[2]
    death_and_cases_css_resources = components_for_death_and_cases[3]

    # calling functions that make plots with a date slider
    daily_cases_plot = plot_with_slider(daily_cases_data, 'Afghanistan', 'cases')
    # finding the components of the tab panels
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    # assigning the returned components
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    comparing_countries = compare_countries_cumulative_per_million(cumulative_cases_data, 'Afghanistan', 'Pakistan')
    comparing_countries_components = find_components(comparing_countries)
    comparing_countries_script = comparing_countries_components[0]
    comparing_countries_plot_div = comparing_countries_components[1]
    comparing_countries_js_resources5 = comparing_countries_components[2]
    comparing_countries_css_resources5 = comparing_countries_components[3]

    return render_template("afghanistan.html",
                           plot_script_linear_and_log_plot=linear_and_log_plot_script,
                           plot_div_linear_and_log=linear_and_log_plot_div,
                           js_resources_linear_and_log=linear_and_log_js_resources,
                           css_resources_linear_and_log=linear_and_log_css_resources,
                           plot_script_death_and_cases=death_and_cases_script,
                           plot_div_death_and_cases=death_and_cases_plot_div,
                           js_resources_death_and_cases=death_and_cases_js_resources,
                           css_resources_death_and_cases=death_and_cases_css_resources,
                           plot_script_daily_cases=daily_cases_plot_script,
                           plot_div_daily_cases=daily_cases_plot_div,
                           js_resources_daily_cases=daily_cases_plot_js_resources,
                           css_resources_daily_cases=daily_cases_plot_css_resources,
                           plot_script_comparing_countries=comparing_countries_script,
                           plot_div_comparing_countries=comparing_countries_plot_div,
                           js_resources_comparing_countries=comparing_countries_js_resources5,
                           css_resources_comparing_countries=comparing_countries_css_resources5
                           )


@app.route('/Bangladesh/')
def bangladesh():
    # calls the read_csv file function and stores the dataframe
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')
    # calls the functions that makes plots
    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Bangladesh', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Bangladesh', 'log')
    # calls the function that makes tab panels
    tabs_for_linear_and_log = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)
    # finding the components of the tab panels
    components_for_linear_log = find_components(tabs_for_linear_and_log)
    # assigning the returned components
    linear_and_log_plot_script = components_for_linear_log[0]
    linear_and_log_plot_div = components_for_linear_log[1]
    linear_and_log_js_resources = components_for_linear_log[2]
    linear_and_log_css_resources = components_for_linear_log[3]

    # calling functions that make plots with a date slider
    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'Bangladesh', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'Bangladesh', 'deaths')
    # calls the function that makes tab panels
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)
    # finding the components of the tab panels
    components_for_death_and_cases = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    death_and_cases_script = components_for_death_and_cases[0]
    death_and_cases_plot_div = components_for_death_and_cases[1]
    death_and_cases_js_resources = components_for_death_and_cases[2]
    death_and_cases_css_resources = components_for_death_and_cases[3]

    # calling functions that make plots with a date slider
    daily_cases_plot = plot_with_slider(daily_cases_data, 'Bangladesh', 'cases')
    # finding the components of the tab panels
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    # assigning the returned components
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    comparing_countries = compare_countries_cumulative_per_million(cumulative_cases_data, 'Bangladesh', 'Pakistan')
    comparing_countries_components = find_components(comparing_countries)
    comparing_countries_script = comparing_countries_components[0]
    comparing_countries_plot_div = comparing_countries_components[1]
    comparing_countries_js_resources5 = comparing_countries_components[2]
    comparing_countries_css_resources5 = comparing_countries_components[3]

    return render_template("bangladesh.html",
                           plot_script_linear_and_log_plot=linear_and_log_plot_script,
                           plot_div_linear_and_log=linear_and_log_plot_div,
                           js_resources_linear_and_log=linear_and_log_js_resources,
                           css_resources_linear_and_log=linear_and_log_css_resources,
                           plot_script_death_and_cases=death_and_cases_script,
                           plot_div_death_and_cases=death_and_cases_plot_div,
                           js_resources_death_and_cases=death_and_cases_js_resources,
                           css_resources_death_and_cases=death_and_cases_css_resources,
                           plot_script_daily_cases=daily_cases_plot_script,
                           plot_div_daily_cases=daily_cases_plot_div,
                           js_resources_daily_cases=daily_cases_plot_js_resources,
                           css_resources_daily_cases=daily_cases_plot_css_resources,
                           plot_script_comparing_countries=comparing_countries_script,
                           plot_div_comparing_countries=comparing_countries_plot_div,
                           js_resources_comparing_countries=comparing_countries_js_resources5,
                           css_resources_comparing_countries=comparing_countries_css_resources5
                           )


@app.route('/Nepal/')
def nepal():
    # calls the read_csv file function and stores the dataframe
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')
    # calls the functions that makes plots
    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Nepal', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Nepal', 'log')
    # calls the function that makes tab panels
    tabs_deaths_and_cases = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)
    # finding the components of the tab panels
    components_for_linear_and_log = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    linear_and_log_plot_script = components_for_linear_and_log[0]
    linear_and_log_plot_div = components_for_linear_and_log[1]
    linear_and_log_js_resources = components_for_linear_and_log[2]
    linear_and_log_css_resources = components_for_linear_and_log[3]
    # calling functions that makes plots with events
    cases_with_events = nepal_cases_with_events(cumulative_cases_data)
    # finding the components of the plot
    components_for_cases_with_events = find_components(cases_with_events)
    # assigning the returned components
    cases_with_events_script = components_for_cases_with_events[0]
    cases_with_events_plot_div = components_for_cases_with_events[1]
    cases_with_events_js_resources = components_for_cases_with_events[2]
    cases_with_events_css_resources = components_for_cases_with_events[3]
    # calls the functions that makes plots
    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'Nepal', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'Nepal', 'death')
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)
    # finding the components of the tab panels
    components_for_death_cases = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    death_and_cases_script = components_for_death_cases[0]
    death_and_cases_plot_div = components_for_death_cases[1]
    death_and_cases_js_resources = components_for_death_cases[2]
    death_and_cases_css_resources = components_for_death_cases[3]
    # calls the functions that makes plots
    comparing_countries = compare_countries_cumulative_per_million(cumulative_cases_data, 'Nepal', 'India')
    # finding the components of the plot
    comparing_countries_components = find_components(comparing_countries)
    # assigning the returned components
    comparing_countries_script = comparing_countries_components[0]
    comparing_countries_plot_div = comparing_countries_components[1]
    comparing_countries_js_resources = comparing_countries_components[2]
    comparing_countries_css_resources = comparing_countries_components[3]
    # calls the functions that makes plots
    daily_cases_plot = plot_with_slider(daily_cases_data, 'Nepal', 'cases')
    # finding the components of the plot
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    # assigning the returned components
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]
    
    return render_template("nepal.html",
                           linear_and_log_plot_script=linear_and_log_plot_script,
                           linear_and_log_plot_div=linear_and_log_plot_div,
                           linear_and_log_js_resources=linear_and_log_js_resources,
                           linear_and_log_css_resources=linear_and_log_css_resources,
                           cases_with_events_plot_script=cases_with_events_script,
                           cases_with_events_plot_div=cases_with_events_plot_div,
                           cases_with_events_js_resources=cases_with_events_js_resources,
                           cases_with_events_css_resources=cases_with_events_css_resources,
                           death_and_cases_plot_script=death_and_cases_script,
                           death_and_cases_plot_div=death_and_cases_plot_div,
                           death_and_cases_js_resources=death_and_cases_js_resources,
                           death_and_cases_css_resources=death_and_cases_css_resources,
                           comparing_countries_plot_script=comparing_countries_script,
                           comparing_countries_plot_div=comparing_countries_plot_div,
                           comparing_countries_js_resources=comparing_countries_js_resources,
                           comparing_countries_css_resources=comparing_countries_css_resources,
                           daily_cases_plot_script=daily_cases_plot_script,
                           daily_cases_plot_div=daily_cases_plot_div,
                           daily_cases_js_resources=daily_cases_plot_js_resources,
                           daily_cases_css_resources=daily_cases_plot_css_resources
                           )


@app.route('/Bhutan/')
def bhutan():
    # calls the read_csv file function and stores the dataframe
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')
    # calls the functions that makes plots
    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Bhutan', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Bhutan', 'log')
    # calls the function that makes tab panels
    tabs_for_linear_and_log = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)
    # finding the components of the tab panels
    components_for_linear_log = find_components(tabs_for_linear_and_log)
    # assigning the returned components
    linear_and_log_plot_script = components_for_linear_log[0]
    linear_and_log_plot_div = components_for_linear_log[1]
    linear_and_log_js_resources = components_for_linear_log[2]
    linear_and_log_css_resources = components_for_linear_log[3]

    # calling functions that make plots with a date slider
    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'Bhutan', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'Bhutan', 'deaths')
    # calls the function that makes tab panels
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)
    # finding the components of the tab panels
    components_for_death_and_cases = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    death_and_cases_script = components_for_death_and_cases[0]
    death_and_cases_plot_div = components_for_death_and_cases[1]
    death_and_cases_js_resources = components_for_death_and_cases[2]
    death_and_cases_css_resources = components_for_death_and_cases[3]

    # calling functions that make plots with a date slider
    daily_cases_plot = plot_with_slider(daily_cases_data, 'Bhutan', 'cases')
    # finding the components of the tab panels
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    # assigning the returned components
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    comparing_countries = compare_countries_cumulative_per_million(cumulative_cases_data, 'Bhutan', 'India')
    comparing_countries_components = find_components(comparing_countries)
    comparing_countries_script = comparing_countries_components[0]
    comparing_countries_plot_div = comparing_countries_components[1]
    comparing_countries_js_resources5 = comparing_countries_components[2]
    comparing_countries_css_resources5 = comparing_countries_components[3]

    return render_template("bhutan.html",
                           plot_script_linear_and_log_plot=linear_and_log_plot_script,
                           plot_div_linear_and_log=linear_and_log_plot_div,
                           js_resources_linear_and_log=linear_and_log_js_resources,
                           css_resources_linear_and_log=linear_and_log_css_resources,
                           plot_script_death_and_cases=death_and_cases_script,
                           plot_div_death_and_cases=death_and_cases_plot_div,
                           js_resources_death_and_cases=death_and_cases_js_resources,
                           css_resources_death_and_cases=death_and_cases_css_resources,
                           plot_script_daily_cases=daily_cases_plot_script,
                           plot_div_daily_cases=daily_cases_plot_div,
                           js_resources_daily_cases=daily_cases_plot_js_resources,
                           css_resources_daily_cases=daily_cases_plot_css_resources,
                           plot_script_comparing_countries=comparing_countries_script,
                           plot_div_comparing_countries=comparing_countries_plot_div,
                           js_resources_comparing_countries=comparing_countries_js_resources5,
                           css_resources_comparing_countries=comparing_countries_css_resources5
                           )


@app.route('/Pakistan/')
def pakistan():
    # calls the read_csv file function and stores the dataframe
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')
    # calls the functions that makes plots
    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Pakistan', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Pakistan', 'log')
    # calls the function that makes tab panels
    tabs_for_linear_and_log = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)
    # finding the components of the tab panels
    components_for_linear_log = find_components(tabs_for_linear_and_log)
    # assigning the returned components
    linear_and_log_plot_script = components_for_linear_log[0]
    linear_and_log_plot_div = components_for_linear_log[1]
    linear_and_log_js_resources = components_for_linear_log[2]
    linear_and_log_css_resources = components_for_linear_log[3]

    # calling functions that make plots with a date slider
    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'Pakistan', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'Pakistan', 'deaths')
    # calls the function that makes tab panels
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)
    # finding the components of the tab panels
    components_for_death_and_cases = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    death_and_cases_script = components_for_death_and_cases[0]
    death_and_cases_plot_div = components_for_death_and_cases[1]
    death_and_cases_js_resources = components_for_death_and_cases[2]
    death_and_cases_css_resources = components_for_death_and_cases[3]

    # calling functions that make plots with a date slider
    daily_cases_plot = plot_with_slider(daily_cases_data, 'Pakistan', 'cases')
    # finding the components of the tab panels
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    # assigning the returned components
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    comparing_countries = compare_countries_cumulative_per_million(cumulative_cases_data, 'Afghanistan', 'Pakistan')
    comparing_countries_components = find_components(comparing_countries)
    comparing_countries_script = comparing_countries_components[0]
    comparing_countries_plot_div = comparing_countries_components[1]
    comparing_countries_js_resources5 = comparing_countries_components[2]
    comparing_countries_css_resources5 = comparing_countries_components[3]

    return render_template("pakistan.html",
                           plot_script_linear_and_log_plot=linear_and_log_plot_script,
                           plot_div_linear_and_log=linear_and_log_plot_div,
                           js_resources_linear_and_log=linear_and_log_js_resources,
                           css_resources_linear_and_log=linear_and_log_css_resources,
                           plot_script_death_and_cases=death_and_cases_script,
                           plot_div_death_and_cases=death_and_cases_plot_div,
                           js_resources_death_and_cases=death_and_cases_js_resources,
                           css_resources_death_and_cases=death_and_cases_css_resources,
                           plot_script_daily_cases=daily_cases_plot_script,
                           plot_div_daily_cases=daily_cases_plot_div,
                           js_resources_daily_cases=daily_cases_plot_js_resources,
                           css_resources_daily_cases=daily_cases_plot_css_resources,
                           plot_script_comparing_countries=comparing_countries_script,
                           plot_div_comparing_countries=comparing_countries_plot_div,
                           js_resources_comparing_countries=comparing_countries_js_resources5,
                           css_resources_comparing_countries=comparing_countries_css_resources5
                           )


@app.route('/Sri-Lanka/')
def sri_lanka():
    # calls the read_csv file function and stores the dataframe
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')
    # calls the functions that makes plots
    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Sri Lanka', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Sri Lanka', 'log')
    # calls the function that makes tab panels
    tabs_for_linear_and_log = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)
    # finding the components of the tab panels
    components_for_linear_log = find_components(tabs_for_linear_and_log)
    # assigning the returned components
    linear_and_log_plot_script = components_for_linear_log[0]
    linear_and_log_plot_div = components_for_linear_log[1]
    linear_and_log_js_resources = components_for_linear_log[2]
    linear_and_log_css_resources = components_for_linear_log[3]

    # calling functions that make plots with a date slider
    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'Sri Lanka', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'Sri Lanka', 'deaths')
    # calls the function that makes tab panels
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)
    # finding the components of the tab panels
    components_for_death_and_cases = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    death_and_cases_script = components_for_death_and_cases[0]
    death_and_cases_plot_div = components_for_death_and_cases[1]
    death_and_cases_js_resources = components_for_death_and_cases[2]
    death_and_cases_css_resources = components_for_death_and_cases[3]

    # calling functions that make plots with a date slider
    daily_cases_plot = plot_with_slider(daily_cases_data, 'Sri Lanka', 'cases')
    # finding the components of the tab panels
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    # assigning the returned components
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    comparing_countries = compare_countries_cumulative_per_million(cumulative_cases_data, 'Sri Lanka', 'India')
    comparing_countries_components = find_components(comparing_countries)
    comparing_countries_script = comparing_countries_components[0]
    comparing_countries_plot_div = comparing_countries_components[1]
    comparing_countries_js_resources5 = comparing_countries_components[2]
    comparing_countries_css_resources5 = comparing_countries_components[3]

    return render_template("sri-lanka.html",
                           plot_script_linear_and_log_plot=linear_and_log_plot_script,
                           plot_div_linear_and_log=linear_and_log_plot_div,
                           js_resources_linear_and_log=linear_and_log_js_resources,
                           css_resources_linear_and_log=linear_and_log_css_resources,
                           plot_script_death_and_cases=death_and_cases_script,
                           plot_div_death_and_cases=death_and_cases_plot_div,
                           js_resources_death_and_cases=death_and_cases_js_resources,
                           css_resources_death_and_cases=death_and_cases_css_resources,
                           plot_script_daily_cases=daily_cases_plot_script,
                           plot_div_daily_cases=daily_cases_plot_div,
                           js_resources_daily_cases=daily_cases_plot_js_resources,
                           css_resources_daily_cases=daily_cases_plot_css_resources,
                           plot_script_comparing_countries=comparing_countries_script,
                           plot_div_comparing_countries=comparing_countries_plot_div,
                           js_resources_comparing_countries=comparing_countries_js_resources5,
                           css_resources_comparing_countries=comparing_countries_css_resources5
                           )


@app.route("/Maldives")
def maldives():
    # calls the read_csv file function and stores the dataframe
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')
    # calls the functions that makes plots
    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Maldives', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Maldives', 'log')
    # calls the function that makes tab panels
    tabs_for_linear_and_log = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)
    # finding the components of the tab panels
    components_for_linear_log = find_components(tabs_for_linear_and_log)
    # assigning the returned components
    linear_and_log_plot_script = components_for_linear_log[0]
    linear_and_log_plot_div = components_for_linear_log[1]
    linear_and_log_js_resources = components_for_linear_log[2]
    linear_and_log_css_resources = components_for_linear_log[3]

    # calling functions that make plots with a date slider
    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'Maldives', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'Maldives', 'deaths')
    # calls the function that makes tab panels
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)
    # finding the components of the tab panels
    components_for_death_and_cases = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    death_and_cases_script = components_for_death_and_cases[0]
    death_and_cases_plot_div = components_for_death_and_cases[1]
    death_and_cases_js_resources = components_for_death_and_cases[2]
    death_and_cases_css_resources = components_for_death_and_cases[3]

    # calling functions that make plots with a date slider
    daily_cases_plot = plot_with_slider(daily_cases_data, 'Maldives', 'cases')
    # finding the components of the tab panels
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    # assigning the returned components
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    comparing_countries = compare_countries_cumulative_per_million(cumulative_cases_data, 'Maldives', 'Sri Lanka')
    comparing_countries_components = find_components(comparing_countries)
    comparing_countries_script = comparing_countries_components[0]
    comparing_countries_plot_div = comparing_countries_components[1]
    comparing_countries_js_resources5 = comparing_countries_components[2]
    comparing_countries_css_resources5 = comparing_countries_components[3]

    return render_template("maldives.html",
                           plot_script_linear_and_log_plot=linear_and_log_plot_script,
                           plot_div_linear_and_log=linear_and_log_plot_div,
                           js_resources_linear_and_log=linear_and_log_js_resources,
                           css_resources_linear_and_log=linear_and_log_css_resources,
                           plot_script_death_and_cases=death_and_cases_script,
                           plot_div_death_and_cases=death_and_cases_plot_div,
                           js_resources_death_and_cases=death_and_cases_js_resources,
                           css_resources_death_and_cases=death_and_cases_css_resources,
                           plot_script_daily_cases=daily_cases_plot_script,
                           plot_div_daily_cases=daily_cases_plot_div,
                           js_resources_daily_cases=daily_cases_plot_js_resources,
                           css_resources_daily_cases=daily_cases_plot_css_resources,
                           plot_script_comparing_countries=comparing_countries_script,
                           plot_div_comparing_countries=comparing_countries_plot_div,
                           js_resources_comparing_countries=comparing_countries_js_resources5,
                           css_resources_comparing_countries=comparing_countries_css_resources5
                           )


@app.route('/India/')
def india():
    # calls the read_csv file function and stores the dataframe
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')
    # calls the functions that makes plots
    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'India', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'India', 'log')
    # calls the function that makes tab panels
    tabs_for_linear_and_log = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)
    # finding the components of the tab panels
    components_for_linear_log = find_components(tabs_for_linear_and_log)
    # assigning the returned components
    linear_and_log_plot_script = components_for_linear_log[0]
    linear_and_log_plot_div = components_for_linear_log[1]
    linear_and_log_js_resources = components_for_linear_log[2]
    linear_and_log_css_resources = components_for_linear_log[3]

    # calling functions that make plots with a date slider
    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'India', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'India', 'deaths')
    # calls the function that makes tab panels
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)
    # finding the components of the tab panels
    components_for_death_and_cases = find_components(tabs_deaths_and_cases)
    # assigning the returned components
    death_and_cases_script = components_for_death_and_cases[0]
    death_and_cases_plot_div = components_for_death_and_cases[1]
    death_and_cases_js_resources = components_for_death_and_cases[2]
    death_and_cases_css_resources = components_for_death_and_cases[3]

    # calling functions that make plots with a date slider
    daily_cases_plot = plot_with_slider(daily_cases_data, 'India', 'cases')
    # finding the components of the tab panels
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    # assigning the returned components
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    comparing_countries = compare_countries_cumulative_per_million(cumulative_cases_data, 'India', 'Pakistan')
    comparing_countries_components = find_components(comparing_countries)
    comparing_countries_script = comparing_countries_components[0]
    comparing_countries_plot_div = comparing_countries_components[1]
    comparing_countries_js_resources5 = comparing_countries_components[2]
    comparing_countries_css_resources5 = comparing_countries_components[3]

    return render_template("india.html",
                           plot_script_linear_and_log_plot=linear_and_log_plot_script,
                           plot_div_linear_and_log=linear_and_log_plot_div,
                           js_resources_linear_and_log=linear_and_log_js_resources,
                           css_resources_linear_and_log=linear_and_log_css_resources,
                           plot_script_death_and_cases=death_and_cases_script,
                           plot_div_death_and_cases=death_and_cases_plot_div,
                           js_resources_death_and_cases=death_and_cases_js_resources,
                           css_resources_death_and_cases=death_and_cases_css_resources,
                           plot_script_daily_cases=daily_cases_plot_script,
                           plot_div_daily_cases=daily_cases_plot_div,
                           js_resources_daily_cases=daily_cases_plot_js_resources,
                           css_resources_daily_cases=daily_cases_plot_css_resources,
                           plot_script_comparing_countries=comparing_countries_script,
                           plot_div_comparing_countries=comparing_countries_plot_div,
                           js_resources_comparing_countries=comparing_countries_js_resources5,
                           css_resources_comparing_countries=comparing_countries_css_resources5
                           )

if __name__ == '__main__':
    app.run(debug=True)