document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const form = document.getElementById('requirements-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const budget = document.getElementById('budget');
            const traffic = document.getElementById('traffic');
            const storage = document.getElementById('storage');
            const bandwidth = document.getElementById('bandwidth');
            
            let valid = true;
            
            // Simple validation for required fields
            if (!budget.value || budget.value <= 0) {
                highlightField(budget, true);
                valid = false;
            } else {
                highlightField(budget, false);
            }
            
            if (!traffic.value || traffic.value < 0) {
                highlightField(traffic, true);
                valid = false;
            } else {
                highlightField(traffic, false);
            }
            
            if (!storage.value || storage.value < 0) {
                highlightField(storage, true);
                valid = false;
            } else {
                highlightField(storage, false);
            }
            
            if (!bandwidth.value || bandwidth.value < 0) {
                highlightField(bandwidth, true);
                valid = false;
            } else {
                highlightField(bandwidth, false);
            }
            
            if (!valid) {
                e.preventDefault();
                alert('Please fill out all required fields with valid values.');
            } else {
                // Show loading animation if valid
                showLoading();
            }
        });
    }
    
    // Sorting functionality for results
    const sortSelect = document.getElementById('sort-by');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            sortResults(this.value);
        });
        
        // Initial sort
        sortResults(sortSelect.value);
    }
    
    // Function to highlight invalid fields
    function highlightField(field, isInvalid) {
        if (isInvalid) {
            field.style.borderColor = 'var(--error)';
        } else {
            field.style.borderColor = 'var(--neutral-300)';
        }
    }
    
    // Function to sort results
    function sortResults(sortBy) {
        const resultsContainer = document.querySelector('.results-cards');
        if (!resultsContainer) return;
        
        const cards = Array.from(resultsContainer.querySelectorAll('.hosting-card'));
        
        cards.sort((a, b) => {
            switch (sortBy) {
                case 'match':
                    return parseFloat(b.dataset.match) - parseFloat(a.dataset.match);
                case 'price-low':
                    return parseFloat(a.dataset.price) - parseFloat(b.dataset.price);
                case 'price-high':
                    return parseFloat(b.dataset.price) - parseFloat(a.dataset.price);
                case 'reliability':
                    return parseFloat(b.dataset.reliability) - parseFloat(a.dataset.reliability);
                case 'scalability':
                    return parseFloat(b.dataset.scalability) - parseFloat(a.dataset.scalability);
                default:
                    return 0;
            }
        });
        
        // Remove all cards
        cards.forEach(card => card.remove());
        
        // Add sorted cards
        cards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            resultsContainer.appendChild(card);
            
            // Animate card appearance with a small delay for each card
            setTimeout(() => {
                card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 50);
        });
    }
    
    // Function to show loading animation
    function showLoading() {
        // Create loading overlay
        const overlay = document.createElement('div');
        overlay.style.position = 'fixed';
        overlay.style.top = '0';
        overlay.style.left = '0';
        overlay.style.width = '100%';
        overlay.style.height = '100%';
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        overlay.style.display = 'flex';
        overlay.style.justifyContent = 'center';
        overlay.style.alignItems = 'center';
        overlay.style.zIndex = '9999';
        
        // Create loading spinner
        const spinner = document.createElement('div');
        spinner.style.width = '50px';
        spinner.style.height = '50px';
        spinner.style.border = '5px solid rgba(255, 255, 255, 0.3)';
        spinner.style.borderTop = '5px solid var(--primary)';
        spinner.style.borderRadius = '50%';
        spinner.style.animation = 'spin 1s linear infinite';
        
        // Add keyframes for spinner animation
        const style = document.createElement('style');
        style.innerHTML = `
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        `;
        document.head.appendChild(style);
        
        // Add spinner to overlay
        overlay.appendChild(spinner);
        
        // Add loading text
        const text = document.createElement('div');
        text.textContent = 'Finding the perfect hosting solution...';
        text.style.color = 'white';
        text.style.marginLeft = '15px';
        text.style.fontWeight = 'bold';
        overlay.appendChild(text);
        
        // Add overlay to body
        document.body.appendChild(overlay);
    }
    
    // Tech stack checkbox highlighting
    const techCheckboxes = document.querySelectorAll('input[name="tech_stack"]');
    if (techCheckboxes.length > 0) {
        techCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const label = this.parentElement;
                if (this.checked) {
                    label.style.fontWeight = 'bold';
                    label.style.color = 'var(--primary)';
                } else {
                    label.style.fontWeight = 'normal';
                    label.style.color = 'var(--neutral-800)';
                }
            });
        });
    }
});