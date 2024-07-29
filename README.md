## Technical Exercise: The Tomato Classification Problem
I completed this exercise while i was focussing on my next career move in Bristol. This company has a very interesting product however due to opting to relocate to London it was no longer a good fit.

Upload rights: I think this is acceptable to upload publicly; please contact me if otherwise and I will remove the repo.

## Objective

Our Machine Learning team has provide us with this code base. 
Your task is to turn this into a production-ready service to serve predictions from the model.

The only **requirement** from product is that the predictions **should be served through a REST api**.

You are the Machine Learning Engineer, therefore, you must come up with any extra requirements for this
service to be consider "production ready". Although the time given for this task is quite limited, try to implement some
of your considerations. Any other requirement that you identify but don't have time to implement or improvements proposed
to your current solution you can note down in [`IMPROVEMENTS.md`](./IMPROVEMENTS.md).

If you managed to get a running solution, write down some instructions in [`RUN_INSTRUCTIONS.md`](./RUN_INSTRUCTIONS.md)

## Guidance

Process:

- **Please fork this repository** immediately so that we can see you've successfully accessed the
  exercise.
- **Submit** by creating a pull request back to the source repository. You're welcome to create
  the PR immediately before starting the solution.
- **Exercise duration**: 3 hours. Commits to your fork that are made beyond this time limit will
  be ignored.

Advice:

- **Prioritise demonstrating an overall solution**, rather than devoting too much time to fixing
  little problems at runtime. Bear in mind that to provide a comprehensive solution to the exercise
  might take longer than the allotted time. In our evaluation, we are not focused on the code
  running correctly. We are more interested to see an end to end solution/scaffold focusing in aspects
  like code design, flexibility, extensibility, maintainability, etc.
- **Treat the codebase as your own**. Do not feel constrained in parts of the repository you can edit.
  You are welcome to make any changes to the code (or tooling or anything else) that you see is a
  priority.
- You can use any language/framework you like, but the model that you serve from the api must be the same model that 
    was provided. 

# The Data

Although you should not need to re-train the model for this task, the dataset used to train the model is a plain text
file that stores tabular data formatted as comma-separated values (CSV). 
Here is an example of the first 5 rows in the dataset:

```bash
!head -n5 {train_dataset}

120,4,plum,cherry,beefsteak
6.4,2.8,5.6,2.2,2
5.0,2.3,3.3,1.0,1
4.9,2.5,4.5,1.7,2
4.9,3.1,1.5,0.1,0
```

From this view of the dataset, notice the following:

The first line is a header containing information about the dataset:
There are 120 total examples. Each example has four features and one of three possible label names.
Subsequent rows are data records, one example per line, where:
The first four fields are features: these are the characteristics of an example. Here, the fields hold float numbers representing shape ratios measurements.
The last column is the label: this is the value we want to predict. For this dataset, it's an integer value of 0, 1, or 2 that corresponds to a tomato type.


## Model trained

The model chosen by the researchers to solve the Tomatoes classification consist in neural network. Neural networks can find complex relationships between features and the label. It is a highly-structured graph, organized into one or more hidden layers. Each hidden layer consists of one or more neurons. There are several categories of neural networks and this program uses a dense, or fully-connected neural network: the neurons in one layer receive input connections from every neuron in the previous layer.

Once the model is trained and fed an unlabeled example, it yields three predictions: the likelihood that this tomato is the given type. E.g:

If the prediction response from the model is [0.02, 0.95, 0.03] means:
- 2% for plum type
- 95% for cherry type
- 3% for beefsteak type  
