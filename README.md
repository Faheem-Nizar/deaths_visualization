# Visual Exploration of Cause of Deaths around the World

This file explains how to run the tool and a basic explanation of the interface. The tool can be used to analyse causes of deaths and help in planning for the future.

## Requirements

For running the file, first make sure you have all the packages installed. This can be done by running the `requirements.txt` file
```bash
pip install -r requirements.txt
```

Make sure you have a python version of atleast 3.12^.

## Usage

To run the file, you need to follow the following steps.

### Clone

Clone the file into your local system.

```bash
git clone https://github.com/Faheem-Nizar/deaths_visualization.git
```

### Run the interface

To run the interface, move to the directory and run the dataiz file as
```bash
streamlit run dataviz.py
```

Once the Streamlit server is running, open a web browser and go to `http://localhost:8501` to access the data visualization tool.

## Features

There are five pages in the interface, with each page providing a special type of visualization.

- World Map
- 2 Variable World Map
- Disease Comparisons
- Continent Wise
- Country Wise trend Analysis

Furthermore, there are additional features within each page and specific to pages to visualize more effectively.

- Population normalization: It recalculates the dataset shown in the visualization to show deaths per 1000 people. The feature isn't available for the 2 variable World Map.
- Time variation: Since the dataset is a timeseries one, we have built sliders in each page to see how the values vary.
- Disease Selection: We have dropdowns to select exactly which disease to show.
- Country Selection: For the linear analysis, we can select the country/countries that we need to visualize and compare the deaths with time.
- Navigation: We have opted for a radio button based navigation on the left side of the interface.

More information about specific features and visualizations are given in the project report.