from flask import Flask, render_template, request, jsonify
import json
import os
from utils.recommendation_engine import get_recommendations
from utils.data_loader import load_hosting_data
from utils.visualization import generate_cost_chart

app = Flask(__name__)

# Load hosting data on startup
hosting_data = load_hosting_data()

@app.route('/')
def home():
    """Render the homepage with the input form"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page with background information"""
    return render_template('about.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    """Process user input and generate recommendations"""
    # Get user requirements from form
    user_requirements = {
        'budget': float(request.form.get('budget', 0)),
        'traffic': int(request.form.get('traffic', 0)),
        'storage': int(request.form.get('storage', 0)),
        'bandwidth': int(request.form.get('bandwidth', 0)),
        'reliability': float(request.form.get('reliability', 1)),  # Changed to float
        'support': request.form.get('support', 'basic') == 'advanced',
        'tech_stack': request.form.getlist('tech_stack')
    }
    
    # Generate recommendations
    recommendations = get_recommendations(hosting_data, user_requirements)
    
    # Generate cost visualization
    chart_filename = generate_cost_chart(recommendations, user_requirements['budget'])
    
    return render_template(
        'recommendations.html', 
        recommendations=recommendations,
        requirements=user_requirements,
        chart_filename=chart_filename
    )

@app.route('/api/hosting-providers', methods=['GET'])
def get_hosting_providers():
    """API endpoint to get hosting provider data"""
    return jsonify(hosting_data)

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    os.makedirs('static/charts', exist_ok=True)
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=3000)