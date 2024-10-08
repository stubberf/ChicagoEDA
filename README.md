# An Investigation of Chicago Home Ownership

tktkt yada yada

### Set Up

1. This project uses Python 3.12. We suggest using [Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) to manage Python installations.

1. We are also using [Poetry](https://python-poetry.org/docs/main/), but you may use whatever you prefer. Dependencies can be found in `pyproject.toml`. You can keep dependency groups organized with commands such as the following:
    
    ```bash
    poetry add --group dev jupyterlab ipykernel
    ```

1. You can create a project-specific notebook kernel as follows:

    ```bash
    poetry run python -m ipykernel install --user --name NEW_PROJECT_NAME
    ```

    And then launch your notebooks with: 
    
    ```bash
    poetry run jupyter lab
    ```

1. Sign up for the Census Api [TODO: add url] and copy your API key into a `.env` file structured like `.env.default`.


### Run

1. Run the app with:
    ```bash
    poetry run streamlit streamlit run app.py
    ```


### Data Sources

1. [Boundaries - ZIP Codes](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-ZIP-Codes/gdcf-axmw), Chicago Data Portal


### Helpful References

1. [Creating Interactive Choropleths with Streamlit](https://arilamstein.com/blog/2024/03/03/creating-interactive-choropleths-with-streamlit/)