# abackup
Asynchronous backup using aioftp.


#### Prerequirements

Script is assumed to be used at server where your site is being hosted.

You have to specify paths for files and directories to be archived and access to database. Currently, script uses *mysqldump* command, but it can easily be changed for other kinds of databases.

One needs:

1. Python 3.8+


#### Usage

Create folder *abackup* and clone this repository there:

    mkdir abackup
    cd abackup
    git clone https://github.com/breduin/abackup.git
or use another appropriate way to copy script files to the directory.

Create and activate virtual environment:

    python3.8 -m venv env
    source env/bin/activate

and install all requirements

    pip install -r requirements.txt
    
Edit *config.py*, check paths and settings.

The script can be run:

    python3.8 abackup 

Optionally, you can run 

    python3.8 abackup db_only
then only database dump will be archived and backuped, or

    python3.8 abackup files_only
then the scripts will handle source files only.

#### Crontab example

Format:

`<crontab parameters>` `cd <abackup directory>` ` && ` `<path to python in virtual env>` `<path to abackup script>` 

Open crontab to edit:

    crontab -e

Say, run script every 15 minutes in period from ten to twelve o'clock:

    */15 10-12 * * * cd /var/www/u1/data/abackup && /var/www/u1/data/abackup/env/bin/python /var/www/u1/data/abackup/abackup.py db_only

Save and exit.