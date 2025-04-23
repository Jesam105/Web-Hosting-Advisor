import json
import os
import pandas as pd

# Sample hosting provider data
SAMPLE_DATA = [
    {
        "id": 1,
        "name": "HostGator",
        "plan_name": "Hatchling",
        "price_monthly": 2.75,
        "price_annual": 29.88,
        "storage": 50000,  # MB
        "bandwidth": 1000,  # GB
        "max_traffic": 100000,  # visitors/month
        "reliability": 99.9,  # percentage
        "support_level": "basic",
        "features": ["WordPress", "cPanel", "SSL Certificate"],
        "tech_stack": ["PHP", "MySQL", "Apache"]
    },
    {
        "id": 2,
        "name": "Bluehost",
        "plan_name": "Basic",
        "price_monthly": 3.95,
        "price_annual": 47.40,
        "storage": 50000,  # MB
        "bandwidth": "Unlimited",
        "max_traffic": 150000,  # visitors/month
        "reliability": 99.95,  # percentage
        "support_level": "basic",
        "features": ["WordPress", "cPanel", "Free Domain", "SSL Certificate"],
        "tech_stack": ["PHP", "MySQL", "Apache"]
    },
    {
        "id": 3,
        "name": "SiteGround",
        "plan_name": "StartUp",
        "price_monthly": 6.99,
        "price_annual": 83.88,
        "storage": 10000,  # MB
        "bandwidth": "Unlimited",
        "max_traffic": 10000,  # visitors/month
        "reliability": 99.99,  # percentage
        "support_level": "advanced",
        "features": ["WordPress", "cPanel", "Free Site Migration", "SSL Certificate", "Daily Backups"],
        "tech_stack": ["PHP", "MySQL", "Apache", "Node.js"]
    },
    {
        "id": 4,
        "name": "DigitalOcean",
        "plan_name": "Basic Droplet",
        "price_monthly": 5.00,
        "price_annual": 60.00,
        "storage": 25000,  # MB
        "bandwidth": 1000,  # GB
        "max_traffic": 500000,  # visitors/month
        "reliability": 99.99,  # percentage
        "support_level": "basic",
        "features": ["SSD Storage", "IPv6", "Monitoring"],
        "tech_stack": ["PHP", "MySQL", "Apache", "Node.js", "Python", "Ruby"]
    },
    {
        "id": 5,
        "name": "AWS",
        "plan_name": "Lightsail",
        "price_monthly": 3.50,
        "price_annual": 42.00,
        "storage": 20000,  # MB
        "bandwidth": 1000,  # GB
        "max_traffic": 400000,  # visitors/month
        "reliability": 99.99,  # percentage
        "support_level": "basic",
        "features": ["SSD Storage", "IPv6", "Load Balancer", "Static IP"],
        "tech_stack": ["PHP", "MySQL", "Apache", "Node.js", "Python", "Ruby", "Java"]
    },
    {
        "id": 6,
        "name": "Dreamhost",
        "plan_name": "Shared Hosting",
        "price_monthly": 2.59,
        "price_annual": 31.08,
        "storage": "Unlimited",
        "bandwidth": "Unlimited",
        "max_traffic": 200000,  # visitors/month
        "reliability": 99.95,  # percentage
        "support_level": "basic",
        "features": ["WordPress", "Free Domain", "SSL Certificate", "SSD Storage"],
        "tech_stack": ["PHP", "MySQL", "Apache", "Python"]
    },
    {
        "id": 7,
        "name": "Netlify",
        "plan_name": "Pro",
        "price_monthly": 19.00,
        "price_annual": 228.00,
        "storage": 1000,  # MB
        "bandwidth": 400,  # GB
        "max_traffic": 1000000,  # visitors/month
        "reliability": 99.99,  # percentage
        "support_level": "advanced",
        "features": ["Continuous Deployment", "Domain Management", "Form Handling", "CDN"],
        "tech_stack": ["JavaScript", "Node.js", "Static"]
    },
    {
        "id": 8,
        "name": "Vercel",
        "plan_name": "Pro",
        "price_monthly": 20.00,
        "price_annual": 240.00,
        "storage": 1000,  # MB
        "bandwidth": 1000,  # GB
        "max_traffic": 1500000,  # visitors/month
        "reliability": 99.99,  # percentage
        "support_level": "advanced",
        "features": ["Continuous Deployment", "Serverless Functions", "Edge Network", "Analytics"],
        "tech_stack": ["JavaScript", "Node.js", "React", "Next.js", "Static"]
    }
]

def load_hosting_data():
    """Load hosting provider data from file or use sample data if file doesn't exist"""
    data_file = 'data/hosting_providers.json'
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    try:
        # Try to load from file
        if os.path.exists(data_file):
            with open(data_file, 'r') as f:
                return json.load(f)
        else:
            # Save sample data to file and return it
            with open(data_file, 'w') as f:
                json.dump(SAMPLE_DATA, f, indent=2)
            return SAMPLE_DATA
    except Exception as e:
        print(f"Error loading hosting data: {e}")
        # Return sample data as fallback
        return SAMPLE_DATA

def convert_to_numeric(value):
    """Convert string 'Unlimited' to a high numeric value for comparison purposes"""
    if value == "Unlimited":
        return float('inf')  # Represent unlimited as infinity
    return value