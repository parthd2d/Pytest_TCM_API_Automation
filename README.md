# Pytest_TCM_API_Automation

This project has API and app functional testing using BrowserStack and Pytest. It includes both API tests and app automation tests, integrated with BrowserStack.

## Setup Instructions

### 1. Create and Activate Python Virtual Environment

To isolate dependencies for this project, create and activate a Python virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For macOS/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
```

### 2. Install Required Packages

Install all required Python packages:

```bash
pip install -r requirements.txt
```

**Note:** Add your credentials (username and accesskey) to .yml files

## Running Tests

### API Tests

1. Change BrowserStack config file:
```bash
export BROWSERSTACK_CONFIG_FILE="api_test_config.yml"
```

2. Run API Tests:
```bash
browserstack-sdk pytest tests/test_api.py
```

### App Automation Tests

1. Change BrowserStack config file:
```bash
export BROWSERSTACK_CONFIG_FILE="app_automate_config.yml"
```

2. Run Automation Tests:
```bash
browserstack-sdk pytest tests/test_automation.py
```
