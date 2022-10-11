# StyleHub-Backend

PRODUCTION URL: https://stylehub.herokuapp.com/

Backend Repository for StyleHub Project

| Method           | URL                      | Input       | Output                                       | Notes                                |
| ---------------- | ------------------------ | ----------- | -------------------------------------------- | ------------------------------------ |
| GET              | myprofile/               | -           | profile for logged in user                   |                                      |
| POST             | myprofile/               | profile     | input profile data informations              |                                      |
| PATCH            | myprofile/               | -           | edit profile                                 |                                      |
| GET              | profile/id/              |             | profile of another user                      |                                      |
| GET              | mycloset/                | -           | list of all items in logged in user's closet |                                      |
| POST             | mycloset/                | closet-item | add new item to closet                       | creates a new item                   |
| GET              | closet-item/:id/         | -           | data for item with specified id              |                                      |
| PATCH            | closet-item/:id/         | card data   | update item                                  | updates the item with specified id   |
| DELETE           | closet-item/:id/         | -           | -                                            | deletes item with specified id       |
| GET              | myoutfits/               | -           | list of all outfits for logged in user       |                                      |
| POST             | myoutfits/               | outfit      | create new outfit                            | creates a new item                   |
| GET              | myoutfits/               | -           | lists all outfits for logged in user         |                                      |
| GET              | outfit/:id/              | -           | data for item with specified id              |                                      |
| PATCH            | outfit/:id/              | card data   | update item                                  | updates the outfit with specified id |
| DELETE           | outfit/:id/              | -           | -                                            | deletes outfit with specified id     |
| GET              | users/                   | -           | list of all users information                | Admin/superuser only                 |
| GET              | closet-items/            | -           | list of all closet-items                     | Admin/superuser only                 |
| GET              | outfits/                 | -           | list of all outfits                          | Admin/superuser only                 |
| GET              | user/:id/closet/         | -           | list of items for user with specified id     | Admin/superuser only                 |
| GET              | user/:id/outfits/        | -           | list of outfits for user with specified id   | Admin/superuser only                 |
| GET/PATCH/DELETE | user/:id/closet-item/:id | -           | item in closet of specified user             | Admin/superuser only                 |
| GET/PATCH/DELETE | user/:id/outfit/:id      | -           | outfit using of specified user               | Admin/superuser only                 |
