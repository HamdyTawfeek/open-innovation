## Open-Innovation
-----    

### Introduction

This is a simple API to resize and color image frames.


### Tech Stack

Our tech stack will include:

* **Python** and **FastAPI** as our server language and server framework
* **PostgreSQL** as our database of choice
* **Docker** , **Docker Compose** Application Containerization 


### Main Files: Project Structure
```sh
├── Dockerfile
├── README.md
├── app
│   ├── db.py
│   ├── frames.py
│   ├── main.py
│   └── resources
│       └── img.csv
├── compose.yaml
└── requirements.txt
```

## Quick start

To run the project locally,

1. Open a terminal:
  ```shell
  git clone https://github.com/HamdyTawfeek/open-innovation.git
  cd open-innovation
  docker-compose up
  ```

2. Navigate to  [the Docs page](http://0.0.0.0:80/docs) to view the available endpoints.
  - Set the `depth_min` and `depth_max` query parameters of the `/frames` endpoint and click execute.


## Next Steps
- Enhance resizing functionality and add color map
- Add test cases
- Deploy the app to the cloud
