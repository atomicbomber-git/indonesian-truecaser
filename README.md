# Setup

```bash
# Set up a Python 3 virtual environment
python -m virtualenv -p python3 env

# Switch environment (Assuming we're using bash shell)
source env/bin/activate

# Install requirements
pip install -r requirements.txt

# Install asset requirements
yarn

# Start asset compilation (dev)
yarn serve

# Start asset compilation (prod)
yarn build

# Run / serve the webapp
python main.py
```