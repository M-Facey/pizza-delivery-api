# Pizza Delivery API

This is a pizza delivery api created using FastAPI. It is completely based on this [YouTube playlist](https://www.youtube.com/playlist?list=PLEt8Tae2spYnLMAf8RGCNYhovIFZHVsPP) by [Ssali Jonathan](https://www.youtube.com/@SsaliJonathan).

## Routes

Here is a list of all the routes that will be present in the applications.

| **Method** | **Route**                      | **Use**                   | **Access** |
| ---------- | ------------------------------ | ------------------------- | ---------- |
| _POST_     | /api/signup                    | Register new user         | All users  |
| _POST_     | /api/login                     | Log in user               | All users  |
| _POST_     | /api/order                     | Place an order            | All users  |
| _PUT_      | /api/order/update/`{order_id}` | Update an order           | All users  |
| _PUT_      | /api/order/status/`{order_id}` | Update order status       | Super user |
| _DELETE_   | /api/order/delete/`{order_id}` | Delete/Remove an order    | All users  |
| _GET_      | /api/user/orders               | Get user's order          | All users  |
| _GET_      | /api/orders                    | List all orders made      | Super user |
| _GET_      | /api/orders/`{order_id}`       | Retrieves an order        | Super user |
| _GET_      | /api/user/order/`{order_id}`   | Get user's specific order | All users  |
| _GET_      | /api/docs                      | View API docs             | All users  |

## How to Run it

First you need to ensure you have Python installed. You can choose to either install PostgreSQL on your computer, or use a cloud solution. 

Afterwards, clone the repo and navigate to the route of the project
```sh
git clone https://github.com/M-Facey/pizza-delivery-api.git
```

Create a virtual environment using [pipenv](https://pypi.org/project/pipenv/) or [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html). FOr the example below, I am using command for `virtualenv`
```sh
python -m venv env
```

Install the project dependencies
```sh
pip install -r requirements.txt
```

Create a `.env` file and copy (& modify, if necessary) the values from the `.env.sample` file.

Create the tables in your database
```sh
python init_db.py
```

Finally, run the project either with
```sh
unicorn main:app
```

... or with hot-reloading
```sh
unicorn main:app --reload
```

## Progress Tracker

- [x] [Intro to Project](https://youtu.be/QQXQAZuJSdw?si=HGsuuJzFYZjHu9YR)
- [x] [Creating the Project Routes](https://youtu.be/eGsFJbT0ryo?si=9ON0sjohNV7G0Z4F)
- [x] [Database with SQLAlchemy](https://youtu.be/mPHZKqUgnDU?si=_cjOenSToNAea2A8)
- [ ] User Creation (Signing up)
- [ ] JWT Authentication
- [ ] Placing an order (HTTP POST Request)
- [ ] List all orders (HTTP GET Request)
- [ ] Get one order (HTTP GET Request)
- [ ] Get current user's order (HTTP GET Request)
- [ ] Update an order (HTTP PUT Request)
- [ ] Update an order's status (HTTP PUT Request)
- [ ] Delete an order (HTTP DELETE Request)
- [ ] Document the API with Swagger using doc string
- [ ] Bearer JWT on Swagger UI
