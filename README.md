# Welcome to All Things Astroinformatics!

## Building

To deploy a new post, run `./deploy.sh` script which removes contents of the `html` directory
and then rebuilds the site using `make html` command. The new additions to the rebuilt `html` directory
will then be added, committed and pushed to `gh-pages`

This workflow was set up using `git worktree` command, using this
[guide](https://gohugo.io/hosting-and-deployment/hosting-on-github/)


```bash
#!/bin/bash
if [ "$CONDA_DEFAULT_ENV" == "astroxyz" ]; then

    cd docs;
    make html;
    cd _build/html;
    git add --all;
    git commit -m "Publishing to gh-pages";
    git push --all

else

    echo "CONDA_DEFAULT_ENV != astroxyz \n\n
            Run 'conda activate astroxyz'"
```

```bash
(spinningup) 11:31:21 ✔ ~/www/astroinformatics.xyz/docs/_build/html (gh-pages) :: git add --all && git commit -m "Publishing to gh-pages"
[gh-pages 3c44c74] Publishing to gh-pages
 3 files changed, 2 insertions(+), 2 deletions(-)
 create mode 100644 _images/nasa-unsplash-cropped.jpg
(spinningup) 11:32:02 ✔ ~/www/astroinformatics.xyz/docs/_build/html (gh-pages) :: git push

```
