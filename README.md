Shop App
- - - -

A web application mimics a shop that sells atheletic balls. It includes full CRUD functionality, dynamic mathematical operations, and user authenthication and authorization. This project is my capstone for the course I took at General Assembly. For my capstone, I had to learn something thing new on my own. I choose to learn Python, Django, and Material CSS.


Technologies Used
- - - -
* Frontend - HTML, CSS, Material CSS and Django(Opinionated Framework)
* Backend - Python
* Database - PSQL
* Deployment - Heroku

ERD
![ERD](./images/capstone-erd.png)
Initial wireframe for Index Page
![Wireframe-index-page](./images/index-page.png)
Wireframe for Cart Show Page
![Wireframe for Cart Show Page](./images/cart-show-page.png)
Wireframe for Product Show Page
![Wireframe-product-show-page](./images/product-show-page.png)



Getting Started
- - - -
Deployment - https://ed-shop.herokuapp.com/



Future Enhancements
- - - -
- [ ] Make the responsive design better.
- [ ] Add a receipt functionality for users.
- [ ] Add images to Product index page.
- [ ] Add links to my GitHub, Linkedin and Portfolio website.




Challenges/ future fixes
- - - -
- [] The form in Quantity should only allow positive numbers. In addition, the selection option should be smaller.
- [] The numbers in Product's price should end in the hundredth decimal place.




Challenges Resolved
- - - -
- [x] Hiding my Secret Key in .ENV.
- [x] Creating unique SubCarts for each user adn Adding a user as an object.
     - This was completed by adding 'user' as a oneToMany relation to the 'User' Model. Then, in views.py, I added the user's unique as part of their subcart. This allows to filter cart by user's id.
- [x] Add user authentication and authorization
- [x] Adding a product which already exists in the cart breaks the code.
    - This was completed by filtering the SubCart model the check if the product already exists for in the User's cart.
- [x] Displaying the Aggregate cost of cart.
    - This was completed by filtering the SubCart model the check if the product already exists for in the User's cart.
- [x] Deleting all of the items in User's cart once all of the items are purchased.
    - This was completed by filtering by filtering Carts by User's id, then using the delete() to clear everything.


References/ Websites used:

1. https://docs.djangoproject.com/en/4.0/
2. https://materializecss.com/
3. https://www.w3schools.com/python/
4. https://www.youtube.com/c/WebDevSimplified
5. https://www.google.com/