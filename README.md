# Anduin

### Deployed Link
**TBD**

## Overview
Introducing your one stop shop for all your buying and selling needs. From anywhere in the world, to anywhere in the world, at any time. Anduin.

## Wireframes

ERD

![wireframe](https://i.imgur.com/SAmhMss.png)

Home

![wireframe](https://i.imgur.com/WifIDeC.png)

Profile

![wireframe](https://i.imgur.com/WH14NfC.png)

Product Details

![wireframe](https://i.imgur.com/wyYutUR.png)


## User Stories
1. When I first load the page, I am brought to the all products 'Home' screen
2. I see links to view the home screen, and depending on whether I am logged in or not: I see links to my profile and logout or signup and login, respectively
3. At the signup screen, I am able to enter a name, email, and password to make an account and be logged in
4. At the login screen, I am able to enter an email and password to login to an existing account
5. While on the home page, I am able to click on a single product to view its details and if I am logged in, I can add it to my cart, as well as add my own new product
6. While viewing a products details I see the product's seller, description, overall rating, and reviews. I am able to add the item to my cart. If logged in, I can leave a review about the product
7. If I click on the seller's link I go to their profile and can view their info, reviews, overall rating, and if I am logged in I can leave a review
7. While viewing my profile, there are links to see and edit my account info, as well as see my cart, products, and orders


## Routes
| Request | Route URL | Description | Takes In | Returns |
| ------- | --------- | ----------- | -------- | ------- |
| POST | /users | signup | name, email, password | user |
| POST | /users/login | login | email, password |  user |
| GET | /users/verify | verify user | auth id |  user |
| PUT | /users/update | update user info | auth id, name, email |  updated user |
| GET | /users/reviews | get reviews about user | auth id | user's reviews |
| GET | /users/products | get user's products | auth id | user's products |
| GET | /products | get all products |  | all products |
| GET | /products/:id | get one product |  | one product |
| POST | /products | add new product | auth id, name, description | new product |
| DELETE | /products/:id | remove product | auth id | message |
| GET | /cart | get user's cart | auth id | user's cart |
| POST | /cart | add item to cart | auth id, product id | message, cart, product |
| DELETE | /cart/:id | remove item from cart | auth id | message, cart |
| GET | /orders | get user's orders | auth id | user's orders |
| POST | /orders | create new order | auth id, address, city, state, zip, card | new order |
| POST | /reviews/users/:email | write review about user | auth id, description, rating | written review |
| POST | /reviews/products/:id | write review about product | auth id, description, rating | written review |
<!-- | Request | Route | Description | Takes | Returns | -->

    
## MVP Goals
- User creation and auth
- User profile shows user's info (which can be updated), cart, products, and orders
- User can write reviews about other users and products
- User can add items to their cart as well as remove them and checkout at any time
- User can view all products, and if logged in: submit new products to sell

## Stretch Goals
- CSS
- Notifications
- Better UI (cart item qty icon, dark theme)
- Friends list or favorited sellers