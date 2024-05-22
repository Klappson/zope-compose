# Zope-Compose - Run Zope and friends without hustle

## What can this do at the moment?

This compose-repo will start everything you need for a zope-project.

- haproxy
- zeo in combination with zodbsync
- postgres
- zope
  - 3 instances by default

## Preinstalled Zope-Mods and Products

Since the main target is to prevent hustle while setting up a comfortable zope enviroment, the zope-container provided comes with some preinstalled mods:

- PythonScripts
- ZSQLMethods
- RequestWrapping
  - request_init and request_end scripts of a context get called for every request made
- ProtectedPythonScripts
  - PythonScripts are not callable by non-Manager users unless they are suffixed with '\_ext'
  - This can be disabled per context by setting the property 'protectPythonScripts\_' to False

## How to use

It's pretty simple

```bash
mkdir mounts
./StartZopeCompose
```

After that the haproxy-service will be available at

```
http://localhost:80
```

## To-Dos

- Error-Handling
- Background-Tasks
- Low-/No-Code Tools
