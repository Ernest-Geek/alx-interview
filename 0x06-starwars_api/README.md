
Star Wars API
Description
This project interacts with the Star Wars API to fetch and display information about Star Wars characters based on the movie ID provided as an argument.

Requirements
Allowed editors: vi, vim, emacs
All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/node
A README.md file, at the root of the project folder, is mandatory
Code should be semistandard compliant (Rules of Standard + semicolons on top)
All files must be executable
Do not use var
How to Use
Clone the repository.
Install Node.js 10:
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semi-standard:
$ sudo npm install semistandard --global
Install the request module and use it:
$ sudo npm install request --global
Execute the scripts to interact with the Star Wars API and retrieve character information.
File Descriptions
0-starwars_characters.js: Script to fetch and display information about Star Wars characters based on the movie ID provided as an argument.
README.md: This file, providing an overview of the project and instructions for use.
Example
To fetch and display information about Star Wars characters from a specific movie, run the script 0-starwars_characters.js with the movie ID as an argument:
$ ./0-starwars_characters.js <movie_id>
Replace <movie_id> with the ID of the Star Wars movie for which you want to retrieve character information.

Author
[Ernest Ampene]
