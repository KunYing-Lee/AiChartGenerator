# AI Chart Generator

An AI-powered web application for generating different types of charts based on input data using OpenAI and Streamlit.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Introduction

AI Chart Generator is a Streamlit web application that leverages OpenAI to help users generate various types of charts from input data. Whether you have categorical, time-based, or numerical data, this app can create bar charts, area charts, and line charts to visualize your data easily.

## Features

- Create bar charts, area charts, and line charts.
- Customize the x-axis using the most appropriate column from your dataset.
- Upload your own dataset in CSV format.
- User-friendly interface powered by Streamlit.

## Getting Started

### Prerequisites

- Python (>=3.6)
- OpenAI API Key

### Installation

1. Clone the repository:
<pre>
   ```bash
   git clone https://github.com/KunYing-Lee/AIChartGenerator.git
   cd ai-chart-generator
</pre>
2. Install the required dependencies:
<pre>
  ```bash
  pip install -r requirements.txt
</pre>

### Usage
1. Run the Streamlit app:
<pre>
  ```bash
  streamlit run ChartGenerator.py
</pre>
or go to the website https://chartgenerator.streamlit.app/
2. Enter your OpenAI API key in the provided input field.
3. Upload your dataset in CSV format.

### Configuration
To configure the AI Chart Generator, you can modify the following settings in the ChartGenerator.py file:
1. `temperature`:Adjust the temperature parameter for OpenAI model responses.
2. `model`:Choose the desired OpenAI model variant.

### Contributing
Contributions are welcome! If you'd like to contribute to AI Chart Generator, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Submit a pull request.
