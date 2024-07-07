# Instructions to run your service here.

### Notes:
Does not work locally due to misconfiguration related to the model input formatting. This was not fixed as to focus on the main goal of this exercise.
Does not work in Lambda environment as packages like tensorflow exceed the lambda's /tmp storage allowance. Configuration of an EC2 could be a viable option.

This code was developed on a linux machine. It is not guaranteed to function on any other tyoe of operating system due to the python packages used can deffer defending on the host OS.

# [Flask] Local Run Instructions

1. Create a virtual environment and activate it.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Ensure the model file is in the correct path as referenced in the code.
4. Run the application using the command `./run.sh`.
   1. You may need to use the command `chmod +x run.sh` to make the file executable.
5. The API will be available at `http://127.0.0.1:5000`.
6. You can test the API using tools like Postman or by running the provided test script using `python -m unittest discover`.

# [Zappa] AWS Lambda Deployment

1. Set AWS CLI credentials with `aws configure`
2. On first deploy do `make deploy-dev`
   1. On update deployments do `make update-dev`
3. Tail log with `zappa tail dev`
4. 

