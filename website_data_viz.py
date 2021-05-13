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
    # calls find_components fuz
    components_of_cases_plot = find_components(cases_plot)
    cases_plot_script = components_of_cases_plot[0]
    cases_plot_div = components_of_cases_plot[1]
    cases_plot_js_resources = components_of_cases_plot[2]
    cases_plot_css_resources = components_of_cases_plot[3]

    converted_data = convert_data_to_per_million(daily_cases_dataframe)
    linear_daily_cases_plot = all_countries_plot(converted_data, 'linear')

    converted_cumulative_data = convert_data_to_per_million(cumulative_cases_dataframe)
    linear_cumulative_cases_plot = all_countries_plot(converted_cumulative_data, 'linear')
    tabs = tabs_for_cumulative_and_daily(linear_cumulative_cases_plot, linear_daily_cases_plot)
    p1 = find_components(tabs)

    script2 = p1[0]
    plot_div2 = p1[1]
    js_resources2 = p1[2]
    css_resources2 = p1[3]
    return render_template('index.html',
                           plot_script=cases_plot_script,
                           plot_div=cases_plot_div,
                           js_resources=cases_plot_js_resources,
                           css_resources=cases_plot_css_resources,

                           plot_script2=script2,
                           plot_div2=plot_div2,
                           js_resource2=js_resources2,
                           css_resources2=css_resources2
                           )


@app.route('/Afghanistan/')
def afghanistan():
    cumulative_cases_data = read_csv_file('confirmed-covid.csv')
    deaths_data = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')

    death_and_cases_linear = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Afghanistan', 'linear')
    death_and_cases_log = death_and_cases_plot(cumulative_cases_data, deaths_data, 'Afghanistan', 'log')
    tabs_for_linear_and_log = tabs_for_linear_and_log_plots(death_and_cases_linear, death_and_cases_log)

    components_for_linear_log = find_components(tabs_for_linear_and_log)
    linear_and_log_plot_script = components_for_linear_log[0]
    linear_and_log_plot_div1 = components_for_linear_log[1]
    linear_and_log_js_resources1 = components_for_linear_log[2]
    linear_and_log_css_resources1 = components_for_linear_log[3]

    cumulative_cases_plot = plot_with_slider(cumulative_cases_data, 'Afghanistan', 'cases')
    cumulative_deaths_plot = plot_with_slider(deaths_data, 'Afghanistan', 'deaths')
    tabs_deaths_and_cases = tabs_for_death_and_cases(cumulative_cases_plot, cumulative_deaths_plot)

    components_for_death_and_cases = find_components(tabs_deaths_and_cases)
    death_and_cases_script = components_for_death_and_cases[0]
    death_and_cases_plot_div = components_for_death_and_cases[1]
    death_and_cases_js_resources = components_for_death_and_cases[2]
    death_and_cases_css_resources = components_for_death_and_cases[3]

    daily_cases_plot = plot_with_slider(daily_cases_data, 'Afghanistan', 'cases')
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    plot5 = compare_countries_cumulative_per_million(cumulative_cases_data, 'Afghanistan', 'Pakistan')
    p5 = find_components(plot5)
    script5 = p5[0]
    plot_div5 = p5[1]
    js_resources5 = p5[2]
    css_resources5 = p5[3]

    return render_template("afghanistan.html",
                           plot_script1=linear_and_log_plot_script,
                           plot_div1=linear_and_log_plot_div1,
                           js_resources1=linear_and_log_js_resources1,
                           css_resources1=linear_and_log_css_resources1,
                           plot_script2=death_and_cases_script,
                           plot_div2=death_and_cases_plot_div,
                           js_resources2=death_and_cases_js_resources,
                           css_resources2=death_and_cases_css_resources,
                           plot_script5=script5,
                           plot_div5=plot_div5,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script6=daily_cases_plot_script,
                           plot_div6=daily_cases_plot_div,
                           js_resources6=daily_cases_plot_js_resources,
                           css_resources6=daily_cases_plot_css_resources
                           )


@app.route('/Bangladesh/')
def bangladesh():
    source = read_csv_file('confirmed-covid.csv')
    source1 = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')

    plot = death_and_cases_plot(source, source1, 'Bangladesh', 'linear')
    plot1 = death_and_cases_plot(source, source1, 'Bangladesh', 'log')
    tabs = tabs_for_linear_and_log_plots(plot, plot1)
    p1 = find_components(tabs)
    script1 = p1[0]
    plot_div1 = p1[1]
    js_resources1 = p1[2]
    css_resources1 = p1[3]

    plot2 = plot_with_slider(source, 'Bangladesh', 'cases')
    plot7 = plot_with_slider(source1, 'Bangladesh', 'deaths')
    tabs = tabs_for_death_and_cases(plot2, plot7)
    p2 = find_components(tabs)
    script2 = p2[0]
    plot_div2 = p2[1]
    js_resources2 = p2[2]
    css_resources2 = p2[3]

    daily_cases_plot = plot_with_slider(daily_cases_data, 'Bangladesh', 'cases')
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    plot5 = compare_countries_cumulative_per_million(source, 'Bangladesh', 'Pakistan')
    p5 = find_components(plot5)
    script5 = p5[0]
    plot_div5 = p5[1]
    js_resources5 = p5[2]
    css_resources5 = p5[3]

    return render_template("bangladesh.html",
                           plot_script1=script1,
                           plot_div1=plot_div1,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script2=script2,
                           plot_div2=plot_div2,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script5=script5,
                           plot_div5=plot_div5,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script6=daily_cases_plot_script,
                           plot_div6=daily_cases_plot_div,
                           js_resources6=daily_cases_plot_js_resources,
                           css_resources6=daily_cases_plot_css_resources
                           )


@app.route('/Nepal/')
def nepal():
    source = read_csv_file('confirmed-covid.csv')
    source1 = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')

    plot = death_and_cases_plot(source, source1, 'Nepal', 'linear')
    plot1 = death_and_cases_plot(source, source1, 'Nepal', 'log')
    tabs = tabs_for_linear_and_log_plots(plot, plot1)
    p1 = find_components(tabs)
    script1 = p1[0]
    plot_div1 = p1[1]
    js_resources1 = p1[2]
    css_resources1 = p1[3]
    
    plot2 = nepal_cases_with_events(source)
    p2 = find_components(plot2)
    script2 = p2[0]
    plot_div2 = p2[1]
    js_resources2 = p2[2]
    css_resources2 = p2[3]
    
    plot3 = plot_with_slider(source, 'Nepal', 'cases')
    plot4 = plot_with_slider(source1, 'Nepal', 'death')
    tabs = tabs_for_death_and_cases(plot3, plot4)
    p3 = find_components(tabs)
    script3 = p3[0]
    plot_div3 = p3[1]
    js_resources3 = p3[2]
    css_resources3 = p3[3]

    plot5 = compare_countries_cumulative_per_million(source, 'Nepal', 'India')
    p5 = find_components(plot5)
    script5 = p5[0]
    plot_div5 = p5[1]
    js_resources5 = p5[2]
    css_resources5 = p5[3]

    daily_cases_plot = plot_with_slider(daily_cases_data, 'Nepal', 'cases')
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]
    
    return render_template("nepal.html",
                           plot_script1=script1,
                           plot_div1=plot_div1,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script2=script2,
                           plot_div2=plot_div2,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script3=script3,
                           plot_div3=plot_div3,
                           js_resources3=js_resources3,
                           css_resources3=css_resources3,
                           plot_script5=script5,
                           plot_div5=plot_div5,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script6=daily_cases_plot_script,
                           plot_div6=daily_cases_plot_div,
                           js_resources6=daily_cases_plot_js_resources,
                           css_resources6=daily_cases_plot_css_resources
                           )


@app.route('/Bhutan/')
def bhutan():
    source = read_csv_file('confirmed-covid.csv')
    source1 = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')

    plot = death_and_cases_plot(source, source1, 'Bhutan', 'linear')
    plot1 = death_and_cases_plot(source, source1, 'Bhutan', 'log')
    tabs = tabs_for_linear_and_log_plots(plot, plot1)
    p1 = find_components(tabs)
    script1 = p1[0]
    plot_div1 = p1[1]
    js_resources1 = p1[2]
    css_resources1 = p1[3]

    plot2 = plot_with_slider(source, 'Bhutan', 'cases')
    plot7 = plot_with_slider(source1, 'Bhutan', 'death')
    tabs = tabs_for_death_and_cases(plot2, plot7)
    p2 = find_components(tabs)
    script2 = p2[0]
    plot_div2 = p2[1]
    js_resources2 = p2[2]
    css_resources2 = p2[3]

    plot5 = compare_countries_cumulative_per_million(source, 'Bhutan', 'India')
    p5 = find_components(plot5)
    script5 = p5[0]
    plot_div5 = p5[1]
    js_resources5 = p5[2]
    css_resources5 = p5[3]

    daily_cases_plot = plot_with_slider(daily_cases_data, 'Bhutan', 'cases')
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    return render_template("bhutan.html",
                           plot_script1=script1,
                           plot_div1=plot_div1,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script2=script2,
                           plot_div2=plot_div2,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script5=script5,
                           plot_div5=plot_div5,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script6=daily_cases_plot_script,
                           plot_div6=daily_cases_plot_div,
                           js_resources6=daily_cases_plot_js_resources,
                           css_resources6=daily_cases_plot_css_resources
                           )


@app.route('/Pakistan/')
def pakistan():
    source = read_csv_file('confirmed-covid.csv')
    source1 = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')

    plot = death_and_cases_plot(source, source1, 'Pakistan', 'linear')
    plot1 = death_and_cases_plot(source, source1, 'Pakistan', 'log')
    tabs = tabs_for_linear_and_log_plots(plot, plot1)
    p1 = find_components(tabs)
    script1 = p1[0]
    plot_div1 = p1[1]
    js_resources1 = p1[2]
    css_resources1 = p1[3]

    plot2 = plot_with_slider(source, 'Pakistan', 'cases')
    plot7 = plot_with_slider(source1, 'Pakistan', 'death')
    tabs = tabs_for_death_and_cases(plot2, plot7)
    p2 = find_components(tabs)
    script2 = p2[0]
    plot_div2 = p2[1]
    js_resources2 = p2[2]
    css_resources2 = p2[3]

    plot5 = compare_countries_cumulative_per_million(source, 'Afghanistan', 'Pakistan')
    p5 = find_components(plot5)
    script5 = p5[0]
    plot_div5 = p5[1]
    js_resources5 = p5[2]
    css_resources5 = p5[3]

    daily_cases_plot = plot_with_slider(daily_cases_data, 'Pakistan', 'cases')
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    return render_template("pakistan.html",
                           plot_script1=script1,
                           plot_div1=plot_div1,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script2=script2,
                           plot_div2=plot_div2,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script5=script5,
                           plot_div5=plot_div5,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script6=daily_cases_plot_script,
                           plot_div6=daily_cases_plot_div,
                           js_resources6=daily_cases_plot_js_resources,
                           css_resources6=daily_cases_plot_css_resources
                           )


@app.route('/Sri-Lanka/')
def sri_lanka():
    source = read_csv_file('confirmed-covid.csv')
    source1 = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')

    plot = death_and_cases_plot(source, source1, 'Sri Lanka', 'linear')
    plot1 = death_and_cases_plot(source, source1, 'Sri Lanka', 'log')
    tabs = tabs_for_linear_and_log_plots(plot, plot1)
    p1 = find_components(tabs)
    script1 = p1[0]
    plot_div1 = p1[1]
    js_resources1 = p1[2]
    css_resources1 = p1[3]

    plot2 = plot_with_slider(source, 'Sri Lanka', 'cases')
    plot7 = plot_with_slider(source1, 'Sri Lanka', 'deaths')
    tabs = tabs_for_death_and_cases(plot2, plot7)
    p2 = find_components(tabs)
    script2 = p2[0]
    plot_div2 = p2[1]
    js_resources2 = p2[2]
    css_resources2 = p2[3]

    plot5 = compare_countries_cumulative_per_million(source, 'Sri Lanka', 'India')
    p5 = find_components(plot5)
    script5 = p5[0]
    plot_div5 = p5[1]
    js_resources5 = p5[2]
    css_resources5 = p5[3]

    daily_cases_plot = plot_with_slider(daily_cases_data, 'Sri Lanka', 'cases')
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    return render_template("sri-lanka.html",
                           plot_script1=script1,
                           plot_div1=plot_div1,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script2=script2,
                           plot_div2=plot_div2,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script5=script5,
                           plot_div5=plot_div5,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script6=daily_cases_plot_script,
                           plot_div6=daily_cases_plot_div,
                           js_resources6=daily_cases_plot_js_resources,
                           css_resources6=daily_cases_plot_css_resources
                           )


@app.route("/Maldives")
def maldives():
    source = read_csv_file('confirmed-covid.csv')
    source1 = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')

    plot = death_and_cases_plot(source, source1, 'Sri Lanka', 'linear')
    plot1 = death_and_cases_plot(source, source1, 'Sri Lanka', 'log')
    tabs = tabs_for_linear_and_log_plots(plot, plot1)
    p1 = find_components(tabs)
    script1 = p1[0]
    plot_div1 = p1[1]
    js_resources1 = p1[2]
    css_resources1 = p1[3]

    plot2 = plot_with_slider(source, 'Maldives', 'cases')
    plot7 = plot_with_slider(source1, 'Maldives', 'deaths')
    tabs = tabs_for_death_and_cases(plot2, plot7)
    p2 = find_components(tabs)
    script2 = p2[0]
    plot_div2 = p2[1]
    js_resources2 = p2[2]
    css_resources2 = p2[3]

    plot5 = compare_countries_cumulative_per_million(source, 'Maldives', 'India')
    p5 = find_components(plot5)
    script5 = p5[0]
    plot_div5 = p5[1]
    js_resources5 = p5[2]
    css_resources5 = p5[3]

    daily_cases_plot = plot_with_slider(daily_cases_data, 'Maldives', 'cases')
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    return render_template("maldives.html",
                           plot_script1=script1,
                           plot_div1=plot_div1,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script2=script2,
                           plot_div2=plot_div2,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script5=script5,
                           plot_div5=plot_div5,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script6=daily_cases_plot_script,
                           plot_div6=daily_cases_plot_div,
                           js_resources6=daily_cases_plot_js_resources,
                           css_resources6=daily_cases_plot_css_resources
                           )


@app.route('/India/')
def india():
    source = read_csv_file('confirmed-covid.csv')
    source1 = read_csv_file('covid_deaths.csv')
    daily_cases_data = read_csv_file('daily_cases.csv')

    plot = death_and_cases_plot(source, source1, 'India', 'linear')
    plot1 = death_and_cases_plot(source, source1, 'India', 'log')
    tabs = tabs_for_linear_and_log_plots(plot, plot1)
    p1 = find_components(tabs)
    script1 = p1[0]
    plot_div1 = p1[1]
    js_resources1 = p1[2]
    css_resources1 = p1[3]

    plot2 = plot_with_slider(source, 'India', 'cases')
    plot7 = plot_with_slider(source1, 'India', 'deaths')
    tabs = tabs_for_death_and_cases(plot2, plot7)
    p2 = find_components(tabs)
    script2 = p2[0]
    plot_div2 = p2[1]
    js_resources2 = p2[2]
    css_resources2 = p2[3]

    plot5 = compare_countries_cumulative_per_million(source, 'Bangladesh', 'India')
    p5 = find_components(plot5)
    script5 = p5[0]
    plot_div5 = p5[1]
    js_resources5 = p5[2]
    css_resources5 = p5[3]

    daily_cases_plot = plot_with_slider(daily_cases_data, 'India', 'cases')
    components_for_daily_cases_plot = find_components(daily_cases_plot)
    daily_cases_plot_script = components_for_daily_cases_plot[0]
    daily_cases_plot_div = components_for_daily_cases_plot[1]
    daily_cases_plot_js_resources = components_for_daily_cases_plot[2]
    daily_cases_plot_css_resources = components_for_daily_cases_plot[3]

    return render_template("India.html",
                           plot_script1=script1,
                           plot_div1=plot_div1,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script2=script2,
                           plot_div2=plot_div2,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script5=script5,
                           plot_div5=plot_div5,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script6=daily_cases_plot_script,
                           plot_div6=daily_cases_plot_div,
                           js_resources6=daily_cases_plot_js_resources,
                           css_resources6=daily_cases_plot_css_resources
                           )


if __name__ == '__main__':
    app.run(debug=True)