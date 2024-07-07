# Instructions to run your service here.

(This code was developed on a linux machine. It is not guaranteed to function on any other tyoe of operating system due to the python packages used can deffer defending on the host OS)

1. Create a python 3.10 virtual environment
2. install requirements


# Run Instructions

1. Create a virtual environment and activate it.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Ensure the model file is in the correct path as referenced in the code.
4. Run the application using the command `./run.sh`.
   1. You may need to use the command `chmod +x run.sh` to make the file executable.
5. The API will be available at `http://127.0.0.1:5000`.
6. You can test the API using tools like Postman or by running the provided test script using `python -m unittest discover`.

