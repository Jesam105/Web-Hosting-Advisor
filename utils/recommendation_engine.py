import numpy as np
from utils.data_loader import convert_to_numeric

def get_recommendations(hosting_data, user_requirements):
    """
    Generate hosting recommendations based on user requirements.
    
    Args:
        hosting_data (list): List of hosting provider dictionaries
        user_requirements (dict): User requirements dictionary
        
    Returns:
        list: Ranked list of hosting providers that match user requirements
    """
    # Process user requirements
    budget = user_requirements['budget']
    expected_traffic = user_requirements['traffic']
    required_storage = user_requirements['storage']
    required_bandwidth = user_requirements['bandwidth']
    min_reliability = user_requirements['reliability']
    advanced_support = user_requirements['support']
    tech_stack = user_requirements['tech_stack']
    
    # Filter hosting options based on hard requirements
    filtered_options = []
    for provider in hosting_data:
        # Skip if over budget
        if provider['price_monthly'] > budget:
            continue
        
        # Skip if storage is insufficient
        provider_storage = convert_to_numeric(provider['storage'])
        if provider_storage != float('inf') and provider_storage < required_storage:
            continue
            
        # Skip if bandwidth is insufficient
        provider_bandwidth = convert_to_numeric(provider['bandwidth'])
        if provider_bandwidth != float('inf') and provider_bandwidth < required_bandwidth:
            continue
            
        # Skip if can't handle traffic
        if provider['max_traffic'] < expected_traffic:
            continue
            
        # Skip if reliability is below minimum
        if provider['reliability'] < min_reliability:
            continue
            
        # Skip if support level doesn't match
        if advanced_support and provider['support_level'] != 'advanced':
            continue
            
        # Check if tech stack is supported
        if tech_stack:
            supported_tech = set(provider['tech_stack'])
            required_tech = set(tech_stack)
            if not required_tech.issubset(supported_tech):
                continue
        
        # If it passes all filters, add to filtered options
        filtered_options.append(provider)
    
    # Calculate match scores
    for provider in filtered_options:
        # Calculate storage score (higher is better)
        provider_storage = convert_to_numeric(provider['storage'])
        if provider_storage == float('inf'):
            storage_score = 1.0
        else:
            storage_score = min(1.0, provider_storage / required_storage) if required_storage > 0 else 1.0
        
        # Calculate bandwidth score (higher is better)
        provider_bandwidth = convert_to_numeric(provider['bandwidth'])
        if provider_bandwidth == float('inf'):
            bandwidth_score = 1.0
        else:
            bandwidth_score = min(1.0, provider_bandwidth / required_bandwidth) if required_bandwidth > 0 else 1.0
        
        # Calculate traffic score (higher is better)
        traffic_score = min(1.0, provider['max_traffic'] / expected_traffic) if expected_traffic > 0 else 1.0
        
        # Calculate reliability score (higher is better)
        reliability_score = provider['reliability'] / 100.0
        
        # Calculate value score (higher is better)
        value_score = 1.0 - (provider['price_monthly'] / budget) if budget > 0 else 0.0
        
        # Calculate feature score (more features is better)
        feature_count = len(provider['features'])
        max_features = max(len(p['features']) for p in hosting_data)
        feature_score = feature_count / max_features
        
        # Calculate tech stack score (more matches is better)
        if tech_stack:
            supported_tech = set(provider['tech_stack'])
            required_tech = set(tech_stack)
            tech_score = len(required_tech.intersection(supported_tech)) / len(required_tech)
        else:
            tech_score = 1.0
        
        # Calculate total score with weightings
        total_score = (
            storage_score * 0.15 +
            bandwidth_score * 0.15 +
            traffic_score * 0.20 +
            reliability_score * 0.20 +
            value_score * 0.15 +
            feature_score * 0.10 +
            tech_score * 0.05
        )
        
        # Add scores to provider object
        provider['match_score'] = round(total_score * 100)
        provider['storage_score'] = round(storage_score * 100)
        provider['bandwidth_score'] = round(bandwidth_score * 100)
        provider['traffic_score'] = round(traffic_score * 100)
        provider['reliability_score'] = round(reliability_score * 100)
        provider['value_score'] = round(value_score * 100)
        
        # Calculate scalability score (how much room to grow)
        if expected_traffic > 0:
            scalability = provider['max_traffic'] / expected_traffic
            provider['scalability'] = min(10, round(scalability))
        else:
            provider['scalability'] = 10
    
    # Sort by match score (descending)
    filtered_options.sort(key=lambda x: x['match_score'], reverse=True)
    
    return filtered_options