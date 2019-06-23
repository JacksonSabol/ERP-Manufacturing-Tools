# ERP-Manufacturing-Tools
## A Python, Flask, and MySQL Application for Enterprise Resource Planning

### Usage:
* Create a virtual environment
    ```
    $ python3 -m venv erp-manufacturing-tools
    $ source erp-manufacturing-tools/bin/activate
    ```
* Install the required modules 
    ```
    $ pip3 install -r requirements.txt
    ```
* Create the database
    ```
    $ python3 create_schema.py
    ```
* Seed the database (if desired)
    ```
    $ python3 add_seeds.py
    ```
* Start the server
    ```
    $ python3 app.py
    ```
* Navigate to localhost:5000/ in the web browser of your choice