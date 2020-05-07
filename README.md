# AC Design Hub

## Setup

Create and activate a virtualenv

Then run:
```
$ bin/setup
```

## Features

* allow users to upload a screenshot of an AC Design
* OCR the image for the following info:
  * design title
  * creator name
  * creator island name
  * design type (custom design, coat, hoodie, balloon-hem dress, etc)
  * creator code `MA-XXXX-XXXX-XXXX`
  * design code `MO-XXXX-XXXX-XXXX`
* auto-fill submission form with OCR data
* auto-crop design thumbnail from screenshot
* allow users to add arbitrary tags (sign, flower, pink, cherry blossom, path, etc)
* allow users to upload additonal screenshots of design applied in-game

* allow users to search designs that have been uploaded by any field value
* display gallery of all designs
* sort by date added
* sort by popularity (views? favorites?)

* display designs grouped by design type (custom design, coat, hoodie, etc)
* display designs with a certain tag
* display designs with a certain creator code

* allow users to click a design thumbnail to see a detailed page
* detailed page should show:
  * original screenshot
  * additional images (ex. screenshot of design applied in-game)
  * tags associated with the design (click a tag to view all designs with that tag)
  * thumbnails of other designs with the same creator code
  * thumbnails of similar designs?

* allow users to click a creator code to see all designs by that creator

* display contact info in site footer to allow reporting site issues

* allow users to create an account
* allow users to favorite designs
