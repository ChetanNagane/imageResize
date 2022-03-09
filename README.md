<h1>ImageResize</h1>
<h2>Install Guide</h2>
<ol>
<li>After downloading the code created a virtual environment and install all the packages in requirements.txt file.</li>
<li>Start a redis server on your local machine, in a sperate shell, at localhost on port 6379.</li>
<li>If you are using a windows machine then use "python manage.py rqworker --worker-class image_api.simpleworker.SimpleWorker low" on powershell. It is a costom worker for windows devices.</li>
<li>If you are using a linx machine then use "python manage.py rqworker low" on terminal.</li>
<li>Use "python manage.py runserver" command to start server.</li>
</ol>
<h2>Working</h2>
<ol>
<li>I have a model called record with all necessary attributes with a serializer to serialize the data.</li>
<li>There are single route with get and post methods. </li>
<li>Get method allows you the get all the data in the database in json response.</li>
<li>Post method takes data and store it in database and queues a jod to resize the image porvided with request.</li>
</ol>

 
