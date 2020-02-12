#!/bin/bash
if [ "$CONDA_DEFAULT_ENV" == "astroxyz" ]; then

    cd docs;
    make html;
    cd _build/html;
    git add --all;
    git commit -m "Publishing to gh-pages";
    git push --all

else

    echo "
            CONDA_DEFAULT_ENV != astroxyz

            Run 'conda activate astroxyz'
         "
fi
