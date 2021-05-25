## Create a backend system for dating APP using Python and Django

## Project summary

The world needs another dating app! But it needs a twist...more like a flip actually! On Upside Town everyones photos are upside down. Your task is to write an API for a tinder-like dating app called Upside Town, that allows people to upload a photo, which then gets flipped upside down on the server, view others flipped photos, match them, and share each others contact information if the match is two-sided.

## Proposer architecture for production system. (Not implemented currently)

![design_document](images/Updown_Town_design_document.png?raw=true)

### Tasks

- Implement assignment using:
  - Language: **Python**
  - Framework: **Django**

- Create 3 API endpoints `/create`, `/list`, and `/match`
  - the `/create` endpoint should allow the user to upload:
    - A photo (limit size to 10M)
      - Flip the photo upside down, then store it
    - Email
    - Gender (m / f)
    - Full name
    - Geo location
      - Geo location should be coordinates (longitude and latitude)

  - the `/match` endpoint should return true if both sides match, and false otherwise:
    - Post t/f
    - Return t/f if both users had their input and decided if to match or not
    - When returning true, send the user the matched persons email

  - the `/list` API should be filterable and paginatable
    - Filter: distance e.g. `/list?gender[eq]=f&distance[lte]=100`
      - You can use the first formula from [this Wikipedia article](https://en.wikipedia.org/wiki/ Great-circle_distance) to calculate distance. Don't forget, you'll need to convert degrees to radians.
    - Pagination: e.g. `/list?page=1`

- Store the data in memory or using sqlite

## Instructions

* Clone the repo to your local machine
  
* Create .env file based on .env_template with all credentials.
  
* Install docker and  run below commands :
  
      docker-compose build
  
      docker-compose up 

* Wait a few minutes for the services to start up.  
  
      docker-compose run web sh start.sh
  
* Wait a few minutes for the services to start up. You can view logs outputs using:
    
      docker-compose -f docker-compose.yml logs -f

## admin UI : 
 * http://localhost:8000/
 
 ![adminui](images/add_profile_at_admin_panel.png?raw=true)

## Rest API: 
 * http://localhost:8000
 
 ![list_api_request](images/list_rest_api.png?raw=true)

 ![create_api_request](images/create_profile_post_api.png?raw=true)

## Print Postgres DB queries in logs for deugging

    docker logs -f postgresql

## Clean up
If you don't have any other docker containers running, you can shut down the ones for this project with the following command:

    docker stop $(docker ps -aq)

Optionally, you can clean up docker images downloaded locally by rinning:

    docker system prune

## TODO: To make it runnable in to production we can add below feature.
  1: CI/CD using git/Jenkins implementation

  2: Unit test cases using pytest module.

  3: Feature test cases using behave framewwork

  4: JWT token based authentication/2-factor authentication to make it secure.

  5: Deployent using Apache