# StyleHub-Backend

## API Reference

#### API Root

`https://stylehub.herokuapp.com/`

| Body       | Type     | Description                    |
| :--------- | :------- | :----------------------------- |
| `api_root` | `string` | The root entrypoint to the API |

---

#### New User Create

```http
POST - https://stylehub.herokuapp.com/auth/users/
```

| Body       | Type     | Description             |
| :--------- | :------- | :---------------------- |
| `username` | `string` | New Username            |
| `password` | `string` | User generated password |
| `email`    | `string` | User generated email    |

Request Sample:

```
POST /auth/users/
Content-Type: json
Authorization: N/A
Host: stylehub.herokuapp.com

{
	"username": "TestUserLogin" ,
	"password": "TestUserPassword",
	"email": "testemail@email.com"
}
```

Response Example (201 Created)

```
{
	"email": "testemail@email.com",
	"username": "TestUserLogin",
	"id": 1
}
```

---

#### Token Authentication

```http
POST - https://stylehub.herokuapp.com/auth/token/login/
```

| Body       | Type     | Description             |
| :--------- | :------- | :---------------------- |
| `username` | `string` | New Username            |
| `password` | `string` | User generated password |

Request Sample:

```
POST /auth/token/login/
Content-Type: json
Authorization: N/A
Host: stylehub.herokuapp.com

{
	"username": "TestUserLogin" ,
	"password": "TestUserPassword",
}
```

Response Example (200 OK)

```
{
	"auth_token": "****************************************"
}

```

---

#### User Login

```http
POST - https://stylehub.herokuapp.com/auth/token/login/
```

| Body       | Type     | Description             |
| :--------- | :------- | :---------------------- |
| `username` | `string` | New Username            |
| `password` | `string` | User generated password |

Request Sample:

```
POST /auth/token/login/
Content-Type: json
Authorization:
Host: stylehub.herokuapp.com

{
	"username": "TestUserLogin" ,
	"password": "TestUserPassword",
}
```

Response Example (200 OK)

```
{
	"auth_token": "****************************************"
}

```

---

#### User Logout - User Authentication **Required**

```http
POST - https://stylehub.herokuapp.com/auth/token/logout/
```

| Body       | Type     | Description             |
| :--------- | :------- | :---------------------- |
| `username` | `string` | New Username            |
| `password` | `string` | User generated password |

Request Sample:

```
POST /auth/token/logout/
Content-Type: json
Authorization: Required
Host: stylehub.herokuapp.com

{
	"username": "TestUserLogin" ,
	"password": "TestUserPassword",
}
```

Response Example (204 No Content)

```
No body returned for response

```

#### Get All Closet Items for One User - User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/mycloset/
```

| Body          | Type     | Description                             |
| :------------ | :------- | :-------------------------------------- |
| `id`          | `int`    | The closet item pk                      |
| `item_choice` | `string` | Sub-category choice of closet item type |
| `size`        | `string` | Size for closet item                    |
| `color`       | `string` | Color choice of closet item             |
| `material`    | `string` | Material input of closet item           |
| `brand`       | `string` | Input of closet item brand              |
| `source`      | `string` | Sub-category closet item choice         |
| `tag`         | `string` | Tags (need to be separated by ,)        |
| `item_image`  | `string` | Url to image                            |
| `added_at`    | `string` | Date added                              |
| `user_id`     | `int`    | User pk who created item pk             |
| `user`        | `int`    | Date added                              |

Request Sample:

```
GET /mycloset/
Content-Type: json
Authorization: N/A
Host: stylehub.herokuapp.com

{
    ""
}
```

Response Example (200 OK)

```
[
	{
		"id": 1,
		"item_choice": "item choice",
		"size": "size input",
		"color": "color choice",
		"material": "material input",
		"brand": "brand input",
		"source": "source choice",
		"tag": [
			"tag",
            "tag"
		],
		"item_image": url_to_image,
		"added_at": "2022-10-14",
		"user_id": 1,
		"user": "user"
	}
]
```

---

#### Post Closet-Item - User Authentication **Required**

```http
POST - https://stylehub.herokuapp.com/mycloset/
```

| Body          | Type     | Description                             |
| :------------ | :------- | :-------------------------------------- |
| `item_choice` | `string` | Sub-category choice of closet item type |
| `size`        | `string` | Size for closet item                    |
| `color`       | `string` | Color choice of closet item             |
| `material`    | `string` | Material input of closet item           |
| `brand`       | `string` | Input of closet item brand              |
| `source`      | `string` | Sub-category closet item choice         |
| `tag`         | `string` | Tags (need to be separated by ,)        |
| `item_image`  | `string` | Url to image                            |

---

PRODUCTION URL: https://stylehub.herokuapp.com/

Backend Repository for StyleHub Project

| Method | URL              | Input       | Output                                       | Notes                                |
| ------ | ---------------- | ----------- | -------------------------------------------- | ------------------------------------ |
| GET    | mycloset/        | -           | list of all items in logged in user's closet |                                      |
| POST   | mycloset/        | closet-item | add new item to closet                       | creates a new item                   |
| GET    | closet-item/:id/ | -           | data for item with specified id              |                                      |
| PATCH  | closet-item/:id/ | card data   | update item                                  | updates the item with specified id   |
| DELETE | closet-item/:id/ | -           | -                                            | deletes item with specified id       |
| GET    | myoutfits/       | -           | list of all outfits for logged in user       |                                      |
| POST   | myoutfits/       | outfit      | create new outfit                            | creates a new item                   |
| GET    | myoutfits/       | -           | lists all outfits for logged in user         |                                      |
| GET    | outfit/:id/      | -           | data for item with specified id              |                                      |
| PATCH  | outfit/:id/      | card data   | update item                                  | updates the outfit with specified id |
| DELETE | outfit/:id/      | -           | -                                            | deletes outfit with specified id     |
| GET    | myprofile/       | -           | profile for logged in user                   | not ready                            |
| POST   | myprofile/       | profile     | input profile data informations              |                                      |
| PATCH  | myprofile/       | -           | edit profile                                 |                                      |
| GET    | profile/id/      |             | profile of another user                      |                                      |

--- ^^^ ACTIVE above ^^^ --- IN PROCESS below ---

| GET | users/ | - | list of all users information | Admin/superuser only |
| GET | closet-items/ | - | list of all closet-items | Admin/superuser only |
| GET | outfits/ | - | list of all outfits | Admin/superuser only |
| GET | user/:id/closet/ | - | list of items for user with specified id | Admin/superuser only |
| GET | user/:id/outfits/ | - | list of outfits for user with specified id | Admin/superuser only |
| GET/PATCH/DELETE | user/:id/closet-item/:id | - | item in closet of specified user | Admin/superuser only |
| GET/PATCH/DELETE | user/:id/outfit/:id | - | outfit using of specified user | Admin/superuser only |

```

```
