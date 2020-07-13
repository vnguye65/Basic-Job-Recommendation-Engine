# Basic Interest-based Job Recommendation Engine

### Background
This career quiz was built for a job portal, GigKoala.com, which provides a collection of gig companies across various career fields. The website is under the property of Enterprise Hall and at its early stage of development. 

This feature is intended to attract more users on site thus increasing traffic. 

### Methods
This is a very basic engine constructed from a Decision Tree Classifier. The training dataset fed into the model was built from scratch and small. Records collected in the training dataset are from research and commonsense. Our team at Enterprise Hall discussed 9 questions that would not only help user understand his/her potentials and pinpoint his/her interests but also make it easy for the model to distinguish attributes among different career fields. Thus, the records and target career fields in the training data were manually entered and labeled. 

The results of this quiz only include the predicted/most fitted career field with basic requirements and responsibilies along direct links to GigKoala.com, providing further information on current job listings is beyond the scope of this project. 

The user interface is built using Python Dash deployed to Heroku App.
Link to quiz: https://gigkoala.herokuapp.com
