# PyGame Cloud Function Color Picker

## Usage

While `main.py` is running, change the color of the active window with Google Cloud's Cloud Function API call, for example,

```bash
curl -m 70 -X POST https://us-central1-cloud-functions-419021.cloudfunctions.net/function-2 \
-H "Content-Type: application/json" \
-d '{
    "color": "lavender"
}'
```

will set the window color to lavender.

## Set-up

Steps:
1) Create a new Google Cloud Project named `cloud-functions`.
2) Clone the GitHub repository by typing `git clone https://github.com/coradora/CSCI4170-Project/tree/main/cloud-functionsexample` in a terminal.
3) Enable the Cloud Functions API here: [Enable Cloud Functions API](https://console.cloud.google.com/flows/enableapi?apiid=cloudfunctions,cloudbuild.googleapis.com&redirect=https://cloud.google.com/functions/docs/consolequickstart-1st-gen)
4) Go to the Cloud Functions overview page and create a new function.
    - Set environment to 1st gen.
    - Name the function `function-2`.
    - Set Trigger to HTTP.
    - Set Authentication to Allow unauthenticated invocations.
    - UNcheck Require HTTPS.
    - Click Save and then Next.
    - In the “Code” page, select the Python 3.12 runtime.
5) In the `main.py` in the Web UI, copy the contents of `cloud_function.py` from the GitHub repository.
    - Change `cloud-functions-419021` from the db on Line 4 to match your project ID. You can obtain this by typing `gcloud projects list` in the Cloud Shell.
6) In `requirements.txt` in the Web UI, paste `google-cloud-firestore==2.15.0`.
7) Click Deploy.
8) Navigate to Firestore and create a database.
    - Select “Native mode” and continue.
    - Set the database ID to “example”.
    - Set location type to Multi-region, and region to nam5 (United States).
    - Set Secure rules to Test rules and press Create Database.
    - Click “Start Collection” and type “colors” in Collection ID and Document ID.
    ![image](https://github.com/coradora/CSCI4170-Project/assets/78966342/ec66d105-c41c-4f8d-808a-75fd4fa8c517)

9) In a terminal on your local machine, configure a virtual environment in the `cloudfunctions-examples` directory with the following commands:
    - `python3 –m venv venv`
    - Activate the newly created virtual environment
        - On Linux/Mac, type `source venv/bin/activate`
        - On Windows, type `venv\Scripts\activate`
    - Install required packages with `pip3 install –r requirements.txt`
10) Start the application by typing `python3 main.py` in the same terminal window.
11) You should see a black screen with the ‘active’ color being repeated in the terminal:
    - ![image](https://github.com/coradora/CSCI4170-Project/assets/78966342/6230be24-1159-4951-b817-ea800ca9ecab)
    - Call the Cloud Function by either:
        - In a terminal, type the following command, replacing “cloudfunctions-419021" with your project ID:
        ```bash
        curl -m 70 -X POST https://us-central1-cloud-functions419021.cloudfunctions.net/function-2 \
        -H "Content-Type: application/json" \
        -d '{
            "color": "lavender"
        }'
        ```

        - From the Cloud Functions Testing Page, enter in a color in the function call, such as:
            - ![image](https://github.com/coradora/CSCI4170-Project/assets/78966342/a4b3dcb8-515c-427e-9d00-eff237836427)
 

12) If Step 11 was successful, the color should’ve changed from Black to Lavender in the application window, with the console indicating that the color was set to Lavender.
    - ![image](https://github.com/coradora/CSCI4170-Project/assets/78966342/b168dca6-9ddd-48e3-bd11-7662c7537f6e)
