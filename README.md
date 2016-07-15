Testing tool for AMQ7 Console
=============================
AMQ7 Console testing tool from Messaging QE.

Maintainers: dlenoch <dlenoch@redhat.com>

How to run
----------
### Python virtual environment
Is the best way how to run this tests.

#### Create one which use interpreter python2 by:
```bash
$ mkdir env
$ virtualenv -p /usr/bin/python2.7 env/py2
```

#### Activate this env by:
```bash
$ source env/py2/bin/activate
```

Now you can work under env, like pip install, run tests, whatever.

#### Deactivate env by:
```bash
$ deactivate
```

### Dependencies
You will need install all dependencies.

```bash
$ pip install -Ur requirements.txt
```

### Run the tests
```bash
$ py.test --driver Firefox --user admin --pasword 1234 tests
```