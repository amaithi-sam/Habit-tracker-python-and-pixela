# Habit-tracker-using-python-and-pixela

It's a Simple Python Script to create a Habit tracking System, using the Pixela


## Pixela 
Pixela is the API service. With this service, 
you can get a GitHub like graph that expresses 
the degree of your daily various activities on a 
basis with a vivid gradation. All operations are 
performed by API. And, it's free.

[Link to Pixela Official site ](https://pixe.la/)


## Screenshots

![Pixela Homepage](https://github.com/amaithi-sam/Habit-tracker-python-and-pixela/blob/main/screenshot/Screenshot%20from%202023-01-16%2017-58-42.png?raw=true)


## Documentation

[Documentation](https://linktodocumentation)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Run Locally

Clone the project

```bash
  git clone https://github.com/amaithi-sam/Habit-tracker-python-and-pixela.git
```

Go to the project directory

```bash
  cd Habit-tracker-python-and-pixela
```

Install dependencies

```bash
  pip install requests
```

Run the Project

```bash
  python main.py
```


## Author

- [@amaithi-sam](https://www.github.com/amaithi-sam)

