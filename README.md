Shop App
- - - -

A web application that allows the customer to add selected products to cart. The cart functionanility is full CRUD.


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
- [ ] Add user authentication and authorization


Challenges/ future fixes
- - - -
- [] Adding a product which already exists in the cart breaks the code.
- [] Deleting all of the items in User's cart once all of the items are purchased.
- [] Displaying the Aggregate cost of cart.
- [] The form in Quantity should only allow positive numbers. In addition, the selection option should be smaller.
- [] The numbers in Product's price should be end in the hundredth decimal place.




Challenges Resolved
- - - -
- [x] Hiding my Secret Key in .ENV.
- [x] Creating unique SubCarts for each user adn Adding a user as an object.
     - This was completed by adding 'user' as a oneToMany relation to the 'User' Model. Then, in views.py, I added the user's unique as part of their subcart. This allows to filter cart by user's id.
- [x] Add user authentication and authorization


