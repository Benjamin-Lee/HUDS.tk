# HUDS.tk

## Introduction

This URL redirector was made with love to be a memorable way to access the HUDS menu for Harvard undergraduates. The menu's URL is dynamically generated and therefore impossible to bookmark or remember. No more!

## How it works

The system is a one-function Flask app deployed to AWS Lambda via Zappa. When a user visits HUDS.tk, a microserver is spun up, the correct URL for the menu is calculated, and then served to the user.

## Bugs

I highly doubt there are any bugs (the whole script is <30 lines long), but if there are, please contact me at [benjamin_lee@college.harvard.edu](mailto:benjamin_lee@college.harvard.edu?HUDS.tk). I intend to maintain this app until my graduation in May 2020, so if HUDS changes their menu URL scheme, I'll be sure to update the redirector.