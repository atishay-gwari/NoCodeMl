# NO Code ML (Automated Machine Learning with Django) (Ongoing)
NO Code ML is a Django-based web application that automates the process of Machine Learning without requiring users to write code. This application allows users to upload CSV files, select the target column, configure data preprocessing options, and perform machine learning tasks with ease.

### Features
- User-Friendly Interface: NO Code ML provides an intuitive and user-friendly interface for  users to interact with the machine learning process.

- CSV Upload: Users can upload their dataset in CSV format.

- Problem Type Selection: Choose between regression and classification problems.

- Target Column Selection: Select the column from the uploaded dataset that should be used as the target variable.

- Encoding Options: NO Code ML allows users to select which columns need label encoding and one-hot encoding, simplifying data preparation.

- Handling Missing Values: Users can choose whether to handle missing values (drop or impute).

- Train-Test Split: Define the test-train split ratio to partition the dataset.

- Results Display: The application provides a results page to display machine learning outcomes, including accuracy, error metrics, and predictions.

### Installation and Setup
To set up NO Code ML on your local machine, follow these steps:

Clone the repository:

bash
```shell
git clone https://github.com/yourusername/nocode-ml.git
```

Install the required dependencies:

bash
```shell
pip install -r requirements.txt
```
Run migrations to create the database:

bash
```shell
python manage.py migrate
```
Start the development server:

bash
```shell
python manage.py runserver
```
Access the application in your web browser at http://localhost:8000.

### Usage
1. Upload a CSV file containing your dataset.

2. Select the problem type (regression or classification).

3. Choose the target column from the dataset.

4. Configure label encoding, one-hot encoding, and handling of missing values.

5. Define the test-train split ratio.

6. Submit the form to perform machine learning tasks.

7. View the results on the results page.

### Contributing
If you'd like to contribute to NO Code ML, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

```shell
git checkout -b feature-name
```
3. Make your changes, and be sure to add tests if necessary.

4. Commit your changes and push them to your fork:

```shell
git add .
git commit -m "Your commit message"
git push origin feature-name
```
5. Create a pull request on the main repository.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
NO Code ML was created to simplify the process of machine learning for users without coding expertise.
Thank you for using NO Code ML! We hope it helps you in your machine learning endeavors. If you encounter any issues or have suggestions for improvement, please feel free to open an issue or contribute to the project.