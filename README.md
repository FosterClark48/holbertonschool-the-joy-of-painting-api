# The Joy of Painting API :art:

## About :memo:
The Joy of Painting API is a Flask-based web service that allows users to query information about episodes from the beloved television show "The Joy of Painting" hosted by Bob Ross. It provides endpoints to fetch episode details, including air dates, related colors, and subject matters.

## Features :sparkles:
- Query episodes by air month, color, and subject matter.
- Access detailed episode information, including season and episode numbers.
- Explore the variety of colors and subject matters featured in episodes.

## Installation and Setup :gear:
To get the API up and running on your local machine, follow these steps:

1. **Clone the Repository**
  ```sh
  git clone https://github.com/FosterClark48/holbertonschool-the-joy-of-painting-api.git
  cd holbertonschool-the-joy-of-painting-api
  ```

2. **Set Up the Environment**
- Make sure Python 3 and pip are installed.
- Install the required Python packages:
  ```sh
  pip install -r requirements.txt
  ```

3. **Start the Flask App**
  ```sh
  python3 run.py
  ```


This will start the Flask development server on `http://127.0.0.1:5000/`. The API can be accessed via this URL.

## Using the API :computer:
To query the API, use the following endpoint structure:
  ```sh
  http://localhost:5000/api/episodes?month=<month_name>&subject=<subject_name>&color=<color_name>
  ```

- `month` is the name of the month (e.g., January, February).
- `subject` is the subject matter of the episode (e.g., Trees, Mountains).
- `color` is a color used in the episode (e.g., Alizarin Crimson, Titanium White).

### Example Queries:
- To get episodes aired in January:
  ```sh
  curl "http://localhost:5000/api/episodes?month=January"
  ```

- To find episodes with "Trees" as a subject matter:
  ```sh
  curl "http://localhost:5000/api/episodes?subject=Trees"
  ```

- To search for episodes using "Alizarin Crimson":
  ```sh
  curl "http://localhost:5000/api/episodes?color=Alizarin Crimson"
  ```


## Author :black_nib:
- **Foster Clark** - [fozc](https://github.com/FosterClark48) :octocat:
- **LinkedIn** - [FosterClark12](https://www.linkedin.com/in/fosterclark12/) ![LinkedIn](https://github.com/FosterClark48/holbertonschool-the-joy-of-painting-api/raw/main/flexbox/images/linkedin-original.svg)

---

Feel free to explore, modify, and use the API for your creative projects. Happy coding! 🎨🌲🌄
