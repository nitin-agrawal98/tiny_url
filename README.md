# tiny_url
<h3> This is a project where any long url can be converted to a unique short url which expires after 12 hours</h3>
<h4>To run project follow below steps:</h4>
<ul>
    <li><b>Clone the repository</b></li>
    <li><b>Run <code>pip install -r requirements.txt</code></b></li>
    <li><b>Run <code>python3 manage.py makemigrations</code></b></li>
    <li><b>Run <code>python3 manage.py migrate</code></b></li>
    <li><b>Run <code>python3 manage.py runserver</code></b></li>
    <li><b>Your application will start running at <code>http://localhost:8000</code></b></li>
 </ul>
<h4>List of supported endpoints:</h4>
<ul>
    <li><code>POST /shortened-url</code><b>Creates and returns a shortened url for the provided URL.</b></li>
    <li><code>GET /shortened-url</code><b>Gets all the shortened URLs.</b></li>
    <li><code>GET /shortened-url/{id}</code><b>get the shortened URL by id.</b></li>
    <li><code>DELETE /shortened-url/{id}</code><b>delete the shortened URL by id.</b></li>
    <li><code>GET /short-url/{short_url}</code><b>Redirects to the original url.</b></li>
</ul>

<h4>Time taken</h4>
<ul>
    <li><b>Time to code - 4hrs</b></li>
    <li><b>Time to test - 1hr</b></li>
</ul>