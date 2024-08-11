# imdb
Clone of IMDB using Django and HTMX. Goal is to test Django as the backend and HTMX for handling client-side interactions and partial page updates without the need for a full page reload.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How it looks](#user-interface)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/nbbrdn/imdb.git
    cd dlgo
    ```

2. **Install dependencies:**
    Make sure you have Python 3.10+ installed. Then install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations:**
    Run the next command:
    ```bash
    ./manage.py migrate
    ```

## User Interface
![alt text](docs/Screenshot_66.png)
![alt text](docs/Screenshot_67.png)
![alt text](docs/Screenshot_68.png)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
