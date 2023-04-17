# Flask Quickstart for Pycob

## Step 1. Clone the Repo
This downloads the quickstart repository to your local machine
```bash
git clone https://github.com/pycob/flask-quickstart.git
```

## Step 2. Install Requirements
This installs the necessary requirements to run the Flask app
```bash
pip install -r requirements.txt
```

## Step 3. Set your API Key
The API key is used for interacting with Pycob.

If you don't have an API key, get one here: https://www.pycob.com/deploy
```bash
export PYCOB_API_KEY=pycob-key-...
```

## Step 4. Run Locally
This is just to test whether the app works locally
```bash
python main.py
```

## Step 5. Deploy to Pycob
This will:
- Send the files to Pycob
- Opens a browser to complete the deployment setup
- Serves the app on `your_app_name.pycob.app`
```bash
python -m pycob.deploy
```
