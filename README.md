# Web Hosting Advisor

## Objective
Recommend hosting plans based on tech needs

## Possible Computational Techniques
1. Requirement matching
2. Feature comparison

## Flask UI Component
1. Budget and traffic inputs; table of results

## Types of Dataset
1. Hosting provider features
2. performance benchmarks

## Possible Sources for Dataset
1. Web hosting comparison sites
2. server performance metrics

## Dataset URLs
1. https://www.netcraft.com/internet-data-mining/hosting-provider-server-count/
2. https://w3techs.com/technologies

## Setup Instructions
24. Hosting Recommendation System
1. Create Flask app with inputs: requirements, budget, traffic
2. Match requirements to hosting features
3. Design comparison algorithms with priority weights
4. Build a database of hosting specs and pricing
5. Predict performance based on traffic
6. Generate hosting recommendations in comparison table
7. Include scalability assessments
8. Visualise cost projections
9. Test with varied project types

# Web Hosting Advisor

A Flask-based application that helps users find the ideal web hosting solution based on their specific requirements, budget constraints, and expected traffic levels.

## Features

- Interactive form for capturing user requirements
- Smart matching algorithm that aligns user needs with hosting provider capabilities
- Comparative results table showcasing recommended hosting plans
- Visual cost projection charts
- Filtering and sorting options for recommendations
- Scalability assessment for future growth

## Technologies Used

- Python 3
- Flask
- Pandas
- Matplotlib
- HTML/CSS/JavaScript

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Jesam105/Web-Hosting-Advisor
   ```
2. Navigate to the project directory:
   ```bash
   cd Web-Hosting-Advisor/project
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Project Structure

- `app.py` - Main Flask application
- `utils/` - Utility modules for data processing and recommendation
  - `data_loader.py` - Functions for loading hosting provider data
  - `recommendation_engine.py` - Algorithm for matching user requirements to hosting options
  - `visualization.py` - Functions for generating data visualizations
- `templates/` - HTML templates for the web interface
- `static/` - Static assets (CSS, JavaScript, images)
- `data/` - Data storage for hosting provider information

## How It Works

1. **Requirement Collection**: Users input their budget, expected traffic, storage requirements, and technology preferences.
2. **Data Analysis**: The application matches these requirements against a database of hosting providers.
3. **Scoring & Ranking**: Each hosting option receives a match score based on how well it meets the user's needs.
4. **Recommendation**: Results are presented in an easy-to-understand format with visualizations.

## Methodology

- **Requirement Matching**: User requirements are translated into structured vectors and matched against hosting features.
- **Feature Comparison**: Hosting plans are analyzed based on their attributes with appropriate weighting.
- **Scalability Assessment**: Evaluates how well each option can accommodate growth.
- **Cost-Benefit Analysis**: Calculates the value proposition by comparing features and performance against cost.

## Team Members

- Obona Jesam Hope - Worked on datasets
- Oyelola Ayomide David - Worked on Flask integration
-  Emmanuel inalegwu - Handled testing and documentation

## Dataset Sources

- https://www.netcraft.com/internet-data-mining/hosting-provider-server-count/, 
- https://w3techs.com/technologies
## Sample Screenshots (Optional)


