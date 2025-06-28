import statistics

def calculate_trustscore(data):
    score = 40  # Base Score

    # Employee Activity
    emp_score = sum(min(e['sales_count'] * 0.4, 10) for e in data['employees'])
    score += min(emp_score, 20)

    # Product Type Score
    category_weight = {'Essential': 1.5, 'General': 1.0, 'Luxury': 0.6}
    prod_score = sum(
        category_weight.get(p['category'], 1.0) * p['quantity']
        for p in data['products_sold']
    )
    score += min(prod_score / 100, 10)

    # Branch Consistency
    branch_score = sum((b['active_days'] / 30) * 5 for b in data['branches'])
    score += min(branch_score, 10)

    # Sales Interval Stability
    try:
        stdev_interval = statistics.stdev(data['intervals'])
        if stdev_interval < 15:
            score += 10
        elif stdev_interval < 30:
            score += 5
    except Exception:
        pass

    # Risk Penalty
    if data.get('refund_rate', 0) > 0.05:
        score -= 5

    # Bonus for verification
    if data.get('verified_docs'):
        score += 3

    # Cap score between 0 and 100
    return max(0, min(int(score), 100))
