<html>
    <head>
        <title>Search</title>
    </head>
    <body>
        <h1>Search</h1>
        <form method="POST" action="/">
            {{ form.csrf_token }}
            {{ form.search.label }} {{ form.search(size=20) }}
            {{ form.submit() }}
        </form>
        {% if search %}
        <h1>Result</h1>
        <div><p>Last search: {{ search }}</p></div>
        {% for result in results %}
        <div><p>{{ result }} </p></div>
        {% endfor %}
        {% endif %}
    </body>
</html>