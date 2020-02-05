# NCSU GIS 714 Spring 2020: Tangible Landscape

## How to add a new activity

### Set up your repository

1. Fork this repository.
1. Clone your fork.

### Develop new analysis

1. Create a new Python file according to the template
   * There is a template called `activity_template.py` in the `activities` directory.
   * Use a unique filename, for example your name or your unique algorithm name.
   * You can use the Simple Python Editor in GRASS GIS.

### Configure an action 

### Create a pull request

We will use command line here, but you can use any Git desktop tool including GitHub Desktop.

Create a new branch for your chaneges and switch to it:

```
git checkout -b creating-awesome-action
```

Add Python file with your function to the repository as a new file:

```
git add activities/your_unique_name.py
git add activities/your_unique_name.json
```

Record the changes:

```
git commit -am "Add awesome activity"
```

Publish the changes into your fork:

```
git push
```

This will give your URL to create pull request on GitHub
or simply go to GitHub and it will suggest you to open a PR.
