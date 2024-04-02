# PyGame Cloud Function Color Picker

## Usage

While main.py is running, change the color of the active window with a Cloud Function API call, for example,
```
curl -m 70 -X POST https://us-central1-cloud-functions-419021.cloudfunctions.net/function-2 \
-H "Content-Type: application/json" \
-d '{
    "color": "lavender"
}'
```

## Set-up

