README.md

Instructions:

 1. Clone the repository from
https://github.com/cranmer/experimentalparticle/ 

 2. Setup a conda environemnt using the `requirements.txt` file. This is an old version of pelican with a lot of old dependencies. This requirements file seems to work on a recent, fresh machine as of July 2023. 

 3. Once the conda environment is up and running, you can build the site and deploy a local development server with 
`make devserver` or `./develop_server.sh start`

4. to publish, you can use:
`make rsync_upload`
this will need to be updated a bit so that it matches the permissions of the group and where it is being hosted at NYU physics (or wherever).

