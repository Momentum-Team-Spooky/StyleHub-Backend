# StyleHub Backend README

## API Reference

### Production Root URL

```
https://stylehub.herokuapp.com/
```

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

---

#### Get All Closet Items for One User - User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/mycloset/
```

| Body          | Type     | Description                                        |
| :------------ | :------- | :------------------------------------------------- |
| `id`          | `int`    | The closet item pk                                 |
| `category`    | `string` | Main Category Choice top, bottom, outerwear, shoes |
| `subcategory` | `string` | Sub Catergory Choice for Clothing Item             |
| `size`        | `string` | Size for closet item                               |
| `color`       | `string` | Color choice of closet item                        |
| `material`    | `string` | Material input of closet item                      |
| `brand`       | `string` | Input of closet item brand                         |
| `source`      | `string` | Sub-category closet item choice                    |
| `tag`         | `string` | Tags (need to be separated by ,)                   |
| `item_image`  | `string` | Url to image                                       |
| `added_at`    | `string` | Date added                                         |
| `user_id`     | `int`    | User pk who created item pk                        |
| `user`        | `int`    | Date added                                         |

Request Sample:

```
GET /mycloset/
Content-Type: json
Authorization: Required
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
		"category": "top",
		"subcategory": "dress",
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

#### Search All Closet Items- User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/mycloset/?search={""}
```

| Body | Type | Description |
| :--- | :--- | :---------- |
| `""` | `""` | ""          |

Request Sample:

```
GET /mycloset/?search=fun
Content-Type: json
Authorization: Required
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
		"category": "top",
		"subcategory": "shirt",
		"size": "Large",
		"color": "white",
		"material": "Cotton",
		"brand": "Bape",
		"source": "brand_store",
		"tag": [
			"Casual",
			"Fun"
		],
		"item_image": "http://127.0.0.1:8000/media/closet_items/Bape_T-Shirt.jpeg",
		"added_at": "2022-10-20",
		"user_id": 1,
		"user": "admin"
	},
	{
		"id": 2,
		"category": "top",
		"subcategory": "shirt",
		"size": "Medium",
		"color": "white",
		"material": "Cotton",
		"brand": "Bape",
		"source": "brand_store",
		"tag": [
			"Funny",
			"Cool"
		],
		"item_image": "http://127.0.0.1:8000/media/closet_items/Bape_T-Shirt_qWImkPH.jpeg",
		"added_at": "2022-10-19",
		"user_id": 1,
		"user": "admin"
	},
	{
		"id": 5,
		"category": "shoes",
		"subcategory": "heels",
		"size": "8",
		"color": "green",
		"material": "leather",
		"brand": "SImmi",
		"source": "friend",
		"tag": [
			"going out",
			"fun"
		],
		"item_image": "http://127.0.0.1:8000/media/closet_items/Green_Simmi_Shoes.jpeg",
		"added_at": "2022-10-20",
		"user_id": 1,
		"user": "admin"
	}
]
```

---

#### Post Closet-Item - User Authentication **Required**

```http
POST - https://stylehub.herokuapp.com/mycloset/
```

| Body          | Type     | Description                                        |
| :------------ | :------- | :------------------------------------------------- |
| `id`          | `int`    | The closet item pk                                 |
| `category`    | `string` | Main Category Choice top, bottom, outerwear, shoes |
| `subcategory` | `string` | Sub Catergory Choice for Clothing Item             |
| `size`        | `string` | Size for closet item                               |
| `color`       | `string` | Color choice of closet item                        |
| `material`    | `string` | Material input of closet item                      |
| `brand`       | `string` | Input of closet item brand                         |
| `source`      | `string` | Sub-category closet item choice                    |
| `tag`         | `string` | Tags (need to be separated by ,)                   |
| `item_image`  | `string` | Url to image                                       |
| `added_at`    | `string` | Date added                                         |
| `user_id`     | `int`    | User pk who created item pk                        |
| `user`        | `int`    | Date added                                         |

Request Sample:

```
POST /mycloset/
Content-Type: multipart
Authorization: Required
Host: stylehub.herokuapp.com
```

| Name          | Value (Choices Given or User Input)                                                                                                                                                   |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `category`    | `top`, `bottom`, `outerwear`, `shoes`                                                                                                                                                 |
| `subcategory` | `button down`, `dress`, `shirt`, `sweater`, `t-shirt`, `pants`, `shorts`, `skirt`, `cardigan`, `coat`, `jacket`, `vest`, `boots`, `flats`, `heels`, `sandals`, `slippers`, `sneakers` |
| `size`        | `user input`                                                                                                                                                                          |
| `color`       | `white`, `green`, `yellow`, `orange`, `red`, `pink`, `purple`, `turqoise`, `blue`, `brown`, `black`, `grey`, `multi`                                                                  |
| `source`      | `brand store`, `department store`, `thrift shop`, `resale/consignment shop`, `friend`, `other`                                                                                        |
| `brand`       | `user input for brand`                                                                                                                                                                |
| `material`    | `user input for material`                                                                                                                                                             |
| `tag`         | `["tag", "tag", "another tag"]`                                                                                                                                                       |
| `item_image`  | File Url to image                                                                                                                                                                     |

Response Example (201 Created)

```
[
	{
		"id": 5,
		"category": "shoes",
		"subcategory": "heels",
		"size": "8",
		"color": "green",
		"material": "leather",
		"brand": "Simmi",
		"source": "friend",
		"tag": [
			"going out",
			"fun"
		],
		"item_image": "https://stylehub-s3-images.s3.amazonaws.com/closet_items/Green_Simmi_Shoes.jpeg",
		"added_at": "2022-10-20",
		"user_id": 1,
		"user": "admin"
	}
]
```

---

#### Get One Closet Item for One User - User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/closet-item/{closet-item-pk}/
```

| Body          | Type     | Description                                        |
| :------------ | :------- | :------------------------------------------------- |
| `id`          | `int`    | The closet item pk                                 |
| `category`    | `string` | Main Category Choice top, bottom, outerwear, shoes |
| `subcategory` | `string` | Sub Catergory Choice for Clothing Item             |
| `size`        | `string` | Size for closet item                               |
| `color`       | `string` | Color choice of closet item                        |
| `material`    | `string` | Material input of closet item                      |
| `brand`       | `string` | Input of closet item brand                         |
| `source`      | `string` | Sub-category closet item choice                    |
| `tag`         | `string` | Tags (need to be separated by ,)                   |
| `item_image`  | `string` | Url to image                                       |
| `added_at`    | `string` | Date added                                         |
| `user_id`     | `int`    | User pk who created item pk                        |
| `user`        | `int`    | Date added                                         |

Request Sample:

```
GET /closet-item/{closet-item-pk}/
Content-Type: json
Authorization: Required
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
		"category": "top",
		"subcategory": "shirt",
		"size": "Medium",
		"color": "white",
		"material": "Cotton",
		"brand": "Bape",
		"source": "brand_store",
		"tag": [
			"Casual",
			"Fun"
		],
		"item_image": "url to image",
		"added_at": "2022-10-19",
		"user_id": 1,
		"user": "admin"
	}
]
```

---

#### Delete a Clothing Item - User Authentication **Required**

```http
DELETE - https://stylehub.herokuapp.com/closet-item/{closet-item-pk}/
```

| Body | Type | Description |
| :--- | :--- | :---------- |
| ""   | ""   | ""          |

Request Sample:

```
DELETE /closet-item/{closet-item-pk}/
Content-Type: json
Authorization: Required
Host: stylehub.herokuapp.com

{
	""
}
```

Response Example (204 No Content)

```
{
	"No body returned for response"
}
```

---

#### Edit One Closet Item for One User - User Authentication **Required**

```http
PATCH - https://stylehub.herokuapp.com/closet-item/{closet-item-pk}/
```

| Body          | Type     | Description                                        |
| :------------ | :------- | :------------------------------------------------- |
| `id`          | `int`    | The outfit item pk                                 |
| `closet_item` | `string` | Main Category Choice top, bottom, outerwear, shoes |
| `subcategory` | `string` | Sub Catergory Choice for Clothing Item             |
| `size`        | `string` | Size for closet item                               |
| `color`       | `string` | Color choice of closet item                        |
| `material`    | `string` | Material input of closet item                      |
| `brand`       | `string` | Input of closet item brand                         |
| `source`      | `string` | Sub-category closet item choice                    |
| `tag`         | `string` | Tags (need to be separated by ,)                   |
| `item_image`  | `string` | Url to image                                       |
| `added_at`    | `string` | Date added                                         |
| `user_id`     | `int`    | User pk who created item pk                        |
| `user`        | `int`    | User who created item                              |

Request Sample:

```
PATCH /closet-item/{closet-item-pk}/
Content-Type: json
Authorization: Required
Host: stylehub.herokuapp.com

{
    "size": "Large"
}
```

Response Example (200 OK)

```
[
	{
		"id": 1,
		"category": "top",
		"subcategory": "shirt",
		"size": "Large",
		"color": "white",
		"material": "Cotton",
		"brand": "Bape",
		"source": "brand_store",
		"tag": [
			"Casual",
			"Fun"
		],
		"item_image": "url to image",
		"added_at": "2022-10-19",
		"user_id": 1,
		"user": "admin"
	}
]
```

---

#### Get List of Closet Tops for One User - User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/mycloset-tops/
```

Request Sample:

```
GET /mycloset-tops/
Content-Type: json
Authorization: Required
Host: stylehub.herokuapp.com

{
	""
}
```

---

#### Get List of Closet Bottoms for One User - User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/mycloset-bottoms/
```

Request Sample:

```
GET /mycloset-bottoms/
Content-Type: json
Authorization: Required
Host: stylehub.herokuapp.com

{
	""
}
```

---

#### Get List of Closet Outerwear for One User - User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/mycloset-outerwear/
```

Request Sample:

```
GET /mycloset-outerwear/
Content-Type: json
Authorization: Required
Host: stylehub.herokuapp.com

{
	""
}
```

---

#### Get List of Closet Shoes for One User - User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/mycloset-shoes/
```

Request Sample:

```
GET /mycloset-shoes/
Content-Type: json
Authorization: Required
Host: stylehub.herokuapp.com

{
	""
}
```

---

#### Get All Outfits for One User - User Authentication **Required**

```http
GET - https://stylehub.herokuapp.com/myoutfits/
```

| Body          | Type      | Description                              |
| :------------ | :-------- | :--------------------------------------- |
| `id`          | `int`     | The closet item pk                       |
| `title`       | `string`  | Name of Outfit                           |
| `tag`         | `string`  | Tags (need to be separated by ,)         |
| `outfit_date` | `string`  | Date of when you want to wear outfit     |
| `draft`       | `boolean` | True or False if the outfit is a draft   |
| `favorite`    | `boolean` | True or False if the outfit is favorited |
| `user`        | `int`     | User who uploaded outfit                 |

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
		"user": "admin",
		"closet_item": [
			{
				"id": 2,
				"category": "top",
				"subcategory": "shirt",
				"size": "Medium",
				"color": "white",
				"material": "Cotton",
				"brand": "Bape",
				"source": "brand_store",
				"tag": [
					"Funny",
					"Cool"
				],
				"item_image": "https://stylehub-s3-images.s3.amazonaws.com/media/closet_items/Bape_T-Shirt_qWImkPH.jpeg",
				"added_at": "2022-10-19",
				"user_id": 1,
				"user": "admin"
			},
			{
				"id": 3,
				"category": "bottom",
				"subcategory": "pants",
				"size": "33 x 32",
				"color": "blue",
				"material": "Cotton",
				"brand": "Unknown",
				"source": "brand_store",
				"tag": [
					"Casual",
					"Torn"
				],
				"item_image": "https://stylehub-s3-images.s3.amazonaws.com/media/closet_items/Blue_Distressed_Jeans.jpeg",
				"added_at": "2022-10-20",
				"user_id": 1,
				"user": "admin"
			},
			{
				"id": 4,
				"category": "shoes",
				"subcategory": "sneakers",
				"size": "8",
				"color": "turqoise",
				"material": "Leather",
				"brand": "Nike",
				"source": "brand_store",
				"tag": [
					"Fire",
					"Tiffany Blue"
				],
				"item_image": "https://stylehub-s3-images.s3.amazonaws.com/media/closet_items/Nike_Tiffany_Colored_Shoes.jpeg",
				"added_at": "2022-10-20",
				"user_id": 1,
				"user": "admin"
			}
		],
		"title": "Sunday Funday",
		"tag": [
			"Casual",
			"Cool",
			"Simple"
		],
		"outfit_date": "2022-10-20",
		"draft": true,
		"favorite": false
	}
]
```

---

Backend Repository for StyleHub Project

| Method | URL                 | Input       | Output                                           | Notes                                |
| ------ | ------------------- | ----------- | ------------------------------------------------ | ------------------------------------ |
| GET    | mycloset/           | -           | list of all items in logged in user's closet     |                                      |
| POST   | mycloset/           | closet-item | add new item to closet                           | creates a new item                   |
| GET    | mycloset-tops/      | -           | list of all tops in logged in user's closet      |                                      |
| GET    | mycloset-bottoms/   | -           | list of all bottoms in logged in users's closet  |                                      |
| GET    | mycloset-outerwear/ | -           | list of all outerwear in logged in user's closet |                                      |
| GET    | mycloset-shoes/     | -           | list of all shoes in logged in user's closet     |                                      |
| GET    | draft-outfit/       | -           | get draft outfit                                 |                                      |
| POST   | draft-outfit/       | closet-item | add new draft outfit to closet                   | creates a new draft outfit           |
| GET    | closet-item/:id/    | -           | data for item with specified id                  |                                      |
| PATCH  | closet-item/:id/    | card data   | update item                                      | updates the item with specified id   |
| DELETE | closet-item/:id/    | -           | -                                                | deletes item with specified id       |
| GET    | myoutfits/          | -           | list of all outfits for logged in user           |                                      |
| POST   | myoutfits/          | outfit      | create new outfit                                | creates a new item                   |
| GET    | myoutfits/          | -           | lists all outfits for logged in user             |                                      |
| GET    | outfit/:id/         | -           | data for item with specified id                  |                                      |
| PATCH  | outfit/:id/         | card data   | update item                                      | updates the outfit with specified id |
| DELETE | outfit/:id/         | -           | -                                                | deletes outfit with specified id     |
| GET    | closet-composition/ | -           | list all closet compostion stats for user        |                                      |
