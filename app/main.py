import streamlit as st
from multi_page import MultiPage
from pages import cocomo
from pages import mean_satisfaction_coefficient
from pages import other_page
from pages import third_step_plots


def main():
    # Create an instance of the app
    app = MultiPage()

    # Title of the main page
    st.title("Efficiency Metrics Evaluation")

    # Add all your applications (pages) here
    app.add_page("Cocomo metric", cocomo.app)
    app.add_page("Other page header", other_page.app)
    app.add_page("Result plots", third_step_plots.app)
    app.add_page("Mean satisfaction coefficient",
                 mean_satisfaction_coefficient.app)

    # The main app
    app.run()


if __name__ == '__main__':
    main()
