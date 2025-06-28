# Flamingo Merchant TrustScore

This repository contains the open version of the Flamingo Merchant TrustScore algorithm.  
The TrustScore is a metric designed to evaluate merchant credibility based on sales frequency, product types, branch activity, sales interval stability, and other factors.

## Features

- Employee sales frequency weighted scoring
- Product category impact on score
- Branch activity consistency
- Sales interval regularity analysis
- Refund rate penalties
- Verification bonus

## Usage

1. Prepare your merchant data in JSON format (see `sample_data.json`).
2. Run the `trustscore_model.py` script with your data.
3. Get a TrustScore between 0 and 100.

## Example

```python
import json
from trustscore_model import calculate_trustscore

with open('sample_data.json') as f:
    data = json.load(f)

score = calculate_trustscore(data)
print(f"Merchant TrustScore: {score}")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Developed by SahanTech © 2025
