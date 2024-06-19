## Overview
This guide provides instructions for running dbt (Data Build Tool) on Dremio

## Table of Contents

1. [Requirements](#requirements)
2. [Getting Started](#getting-started)
    - Setting Up Docker Compose
    - Install dependencies
    - Generating Fake Data
3. [Running dbt on Dremio](#running-dbt-on-dremio)
4. [Additional Information](#additional-information)

## Requirements

Ensure you have the following software installed on your system:

- docker
- docker Compose
- python (for generating fake data)
- pip

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/prd-huy-thai/dremio-dbt
   cd dremio-dbt
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements/dev.txt
   ```

3. Generating Fake Data:
   ```bash
   python scripts/fake_data.py
   ```

## Running dbt on Dremio
1. Load data into data source
   ```bash
   dbt seed
   ```
2. Running dbt 
   ```bash
   dbt run
   ```

## Additional Information
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices