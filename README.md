## Getting Started (MacOS Environment)

These instructions will guide you on how to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Python](https://www.python.org/downloads/)

### Installation

Follow these steps to setup your development environment:

1. Navigate to the repository where you want to save the project.
    ```
    cd <folder name>
    ```
2. Clone the repository.
    ```
    git clone https://github.com/dron4ik86/gm-api-home-interview-assignment.git
    ```
3. Install the virtual environment.
    ```
    pip3 install virtualenv
    ```
4. Create a virtual environment in the project directory.
    ```
    cd gm-api-home-interview-assignment
    virtualenv venv
    ```
5. Activate the virtual environment.
    ```
    source venv/bin/activate
    ```
6. Install project dependencies.
    ```
    pip3 install -r requirements.txt
    ```
7. Please update the `.env.template` file with your own secret values and rename it to `.env`.
   
### Usage
1. To calculate the intent rate and entity rate, we need to pass the intent value and entity value as arguments.
2. Run tests via Pytest.
    ```
    pytest --intent <intent value> --entity <entity value> --utterances "<utterances with comma separated>" -s
    ```
   
## Troubleshooting

### **Problem 1**: 
```
ModuleNotFoundError: No module named '<module name>'
```
- **Possible Cause**:

  The Python interpreter might not be recognizing the project's root directory as part of its path, leading to module resolution issues.

- **Solution**: 

   To include the current directory in the Python path, run the following command in the terminal where you are trying to execute the tests:
```
export PYTHONPATH="${PYTHONPATH}:pwd"
```

