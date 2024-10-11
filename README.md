# Data Scraping and Transformation Pipeline
This project is focused on scraping data from public Telegram channels related to Ethiopian medical businesses and cosmetics, 
transforming that data, and storing it in a PostgreSQL database for analysis. The pipeline captures both textual data and images from channels 
like Lobelia Pharmacy and Chemed, using Python libraries such as Telethon for Telegram scraping. The scraped raw data is initially stored in CSV files
before being transformed and cleaned. We address missing values, duplicates, and inconsistent formats, preparing the data for loading into a PostgreSQL database.

For the data transformation, we leverage DBT (Data Build Tool) to create models that automate the cleaning and transformation process. 
DBT allows us to run SQL-based transformations, test the integrity of our data, and document the process, ensuring data quality throughout the pipeline.
Logs are maintained for both the scraping and transformation processes to capture errors and monitor pipeline performance. After transformation, 
the clean data is loaded into PostgreSQL for further analysis, making it ready for deeper business insights or machine learning tasks such as object detection with YOLO.
