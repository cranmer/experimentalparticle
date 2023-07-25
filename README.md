README.md

Instructions:

 1. Clone the repository from
https://github.com/cranmer/experimentalparticle/ 

 2. [Install conda](https://www.anaconda.com/download) or miniconda. Setup a conda environemnt using the `requirements.txt` file.  Something like this:
 `conda env create -f requirements.txt -n pelican-3.7.1`

 This site is based on an old version of pelican (3.7.1) with a lot of old dependencies. This requirements file seems to work on a recent, fresh machine as of July 2023.

 3. Activate the conda environment with `conda activate pelican-3.7.1`
 
  the conda environment is up and running, you can build the site and deploy a local development server with 
`make devserver` or `./develop_server.sh start`

You can then view the site at `localhost:8000`, but the navigation gets wonky and tries to point to the live site. This can be fixed in the configuration, or you can just replace `https://physics.nyu.edu/experimentalparticle/` with `localhost:8000/` by hand.

4. to publish the site, you can use:
`make rsync_upload` (see the Makefile rule for where it is placing it on samba.physics.nyu.edu)
this will need to be updated a bit so that it matches the permissions of the group and where it is being hosted at NYU physics (or wherever).

