import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

def generate_cost_chart(recommendations, budget):
    """
    Generate a cost comparison chart for recommended hosting providers.
    
    Args:
        recommendations (list): List of recommended hosting providers
        budget (float): User's budget
        
    Returns:
        str: Filename of the generated chart
    """
    # Only use top 5 recommendations
    providers = recommendations[:5] if len(recommendations) > 5 else recommendations
    
    # Extract names and monthly prices
    names = [p['name'] + ' ' + p['plan_name'] for p in providers]
    monthly_prices = [p['price_monthly'] for p in providers]
    annual_prices = [p['price_annual'] / 12 for p in providers]  # Convert to monthly for comparison
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bar width and positions
    bar_width = 0.35
    x = np.arange(len(names))
    
    # Create bars
    monthly_bars = ax.bar(x - bar_width/2, monthly_prices, bar_width, label='Monthly Price', color='#0066CC')
    annual_bars = ax.bar(x + bar_width/2, annual_prices, bar_width, label='Annual Price (Monthly Equivalent)', color='#2E8B57')
    
    # Add budget line
    if budget > 0:
        ax.axhline(y=budget, color='#DC3545', linestyle='--', linewidth=2, label=f'Budget (${budget}/mo)')
    
    # Add labels and title
    ax.set_xlabel('Hosting Providers')
    ax.set_ylabel('Price ($ per month)')
    ax.set_title('Hosting Cost Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=45, ha='right')
    
    # Add value labels on bars
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'${height:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    add_labels(monthly_bars)
    add_labels(annual_bars)
    
    # Add legend
    ax.legend()
    
    # Adjust layout
    plt.tight_layout()
    
    # Save chart to file
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'cost_chart_{timestamp}.png'
    filepath = os.path.join('static', 'charts', filename)
    plt.savefig(filepath)
    plt.close()
    
    return filename