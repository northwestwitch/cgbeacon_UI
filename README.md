# cgbeacon_UI
Flask app for handling variant queries to the Clinical Genomics Beacon

This package contains a query interface to a simple MySQL beacon.
For more info on what's a genomic variant beacon and how the Clinical Genomics Beacon works : https://github.com/Clinical-Genomics/cgbeacon.

To clone and run the interface from your local directory use the following commands:
<pre>
git clone https://github.com/northwestwitch/cgbeacon_UI.git
</pre>

Change directory to the newly created folder and run the app:
<pre>
cd cgbeacon_UI
python3 run.py
</pre>

Your query interface should be now available from a web browser page, at the following address:
<pre>
http://127.0.0.1:5000/
</pre>

The app is designed to connect via SQL Alchemy to a default MySQL database present on the same machine as the app, but you can customize the connections parameter by modifying the parameter "SQLALCHEMY_DATABASE_URI" in the config file present in the "instance" folder.


