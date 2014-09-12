##PyDuty

A very basic, class-based, Python decorator which can be used to trigger an incident in PagerDuty when a function returns an error. There are two test-scripts in the directory "TestScripts", one (function_test.py) which can be run from the CLI or via the interpreter, etc...The other, (flask_app_test.py) is a Flask "web-app".

...In the Flask use-case, be sure to apply the decorator first, before "app.run()", which means placing it as the bottom-most decorator.

