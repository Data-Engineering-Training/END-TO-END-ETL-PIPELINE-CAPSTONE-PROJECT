# Akua's Capstone project: End-to-End ETL Pipeline
# COMMERCIAL CARBON EMISSIONS DATA PIPELINE

### Table of Contents
1. Introuction
     * Brief Background
     * Business tasks
     *  Approach
2. Project scope and objectives
    * Project goal
    * Project scope
   * Expected results/deliverables
3. Data pipeleine processes and architecture
4. Requirements
5. Technologies/Tecqniques used
6. Data acquisition
     * Data source identification
     * Description of dataset 
7. Data Extraction processes
8. Data Transformation processes
9. Database setup and data loading processes
    * Database connection
    * Data ingestion into database (data warehouse)

10.Testing
    * Data quality Testing
    * Performance Testing

11.Error handling and logging

12.Data analysis and visualization

    * Data querying
    * Dashboard generation
    * Business data reporting

13.Other relevant Information
    * Challenges and solutions
    * Lessons learned and future considerations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Introuction
    ### Project overview
    ### Project goal
        The project's objective is to develop a a scalable and efficient 	ETL pipeline.This will provide quality and reliable data insights for predicting sustainable solutions to carbon emissions reduction in industries. 
    ### Project scope
        This project primarily focuses on leveraging ETL techniques to extract product carbon footprint (PCF) data, transform and store it into an analytics-friendly data warehouse, providing companies with strategic insights for achieving steeper carbon reduction
    ### Business use case[business problem, task, outcomes]
        When factoring heat generation required for the manufacturing and transportation of products, carbon emissions attributable to products– from foods to appliances to sneakers to cloud infrastructure – make up more than 75% of global emissions. 
        There has been an increasing awareness of the role of product-embodied greenhouse gases also referred to as its product carbon footprint (PCF). This has given rise to an emerging ecosystem of stakeholders, ranging from companies intending to include carbon labels on their products, to consumer-oriented services, as well as financial institutions, aiming to inform consumers about their purchasing-related carbon footprint, and consumers engaging in carbon-conscious purchasing. 
        The opportunities for sustainable management of products value chain are vast but many challenges persist.
        With the increasing pressure from regulators, many industries are now leveraging data analytics and engineering to develop tareted strategies for reducing their ecological footprints, thereby, generating better insights into improving their sustainability performance.  

      ### Business Tasks
        Build a robust pipeline for periodic update of PCF data records
        Analyze trend and relationships in business operations to uncover hidden sustainabily risks
        Identify opportunities for optimization throughought product value chain 

    ### Expected results/ deliverables
        an analytical database designed to store processed data and enable easy access for end-users
        reporting dashboard providing isights into sustainable solutions for optimization throughout product value chains.
## Data acquisition
    ### Data source identification
The project utilizes industrial carbon emissions data derived from the carbon catalogue database, available on figshare.
    ### Description of dataset 
    	866 Industrial product carbon footprint records in carbon catalogue
	25 product-level data fields and 6 stage-level data fields

## Technologies/Tecqniques used

## Data pipeleine processes and architecture: flow process, flow diagram, pipeline processing type
    The pipeline created for this project was for batch processing which runs periodically on a monthly basis. 
    View pipeline architecture using [image file]
5. Requirements
this projects requires the following softwares, packages and tools:
view requirements.txt file

Set up/processes
For local running and testing, follow the following steps
- Preparatory steps
Environment set up:
Ensure Python, docker and docker compose are installed on operating system
Clone the repository : https://github.com/aqualinqs/END-TO-END-ETL-PIPELINE-CAPSTONE-PROJECT
install required python packages using the 'requirement.txt' file
import packages and load the environment variables

- Development steps
A. Data Extraction and transformation processes
    use "extract_transform.py" file to extract PCF data from and trasform it into a useful format
    data tranformation processes include
    - handling missing values
    - eliminating unwanted data

Database setup and data loading processes
     
Data ingestion into local database (data warehouse)
    Use dbconection_ingest_data.py file to create mysql database connection and load data into mysql database
    
    
## Creating airflow connection
Install airflow from PyPI using command:
pip install apache-airflow[mySQL]

import required python libraries
Use 'docker-compose-airflow.yaml' file to create airflow tconnection to postgres database 
run the dag
Data analysis and visualization
    Data querying
    Use the query_data.py script to query the database to answer the key business questions
