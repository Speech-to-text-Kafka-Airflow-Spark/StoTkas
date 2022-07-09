<h1 align="center">Speech-to-text data collection with Kafka, Airflow, and Spark</h1>
<div>
<img src="https://img.shields.io/badge/OS-linux%20%7C%20windows-blue??style=flat&logo=Linux&logoColor=b0c0c0&labelColor=363D44" alt="Operating systems"/>
<a href="https://github.com/Speech-to-text-Kafka-Airflow-Spark/StoTkas/network/members"><img src="https://img.shields.io/github/forks/Speech-to-text-Kafka-Airflow-Spark/StoTkas" alt="Forks Badge"/></a>
<a href="https://github.com/Speech-to-text-Kafka-Airflow-Spark/StoTkas/pulls"><img src="https://img.shields.io/github/issues-pr/Abel-Blue/breastCancer-causal-Inference" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Speech-to-text-Kafka-Airflow-Spark/StoTkas/issues"><img src="https://img.shields.io/github/issues/Speech-to-text-Kafka-Airflow-Spark/StoTkas" alt="Issues Badge"/></a>
<a href="https://github.com/Speech-to-text-Kafka-Airflow-Spark/StoTkas/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Speech-to-text-Kafka-Airflow-Spark/StoTkas?color=2b9348"></a>
<a href="https://github.com/Speech-to-text-Kafka-Airflow-Spark/StoTkas/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Speech-to-text-Kafka-Airflow-Spark/StoTkas?color=2b9348" alt="License Badge"/></a>
</div>

</br>

![causal-image](https://miro.medium.com/max/1072/1*TzRyGCOSa4aZhda3B2H-qg.png)


## Table of Contents

1. [Introduction](#Introduction)
2. [Project Structure](#project-structure)
   - [data](#data)
   - [notebooks](#notebooks)
   - [scripts](#scripts)
   - [tests](#tests)
   - [logs](#logs)
   - [root folder](#root-folder)
3. [Installation guide](#installation-guide)

<hr>

## Introduction
 <p>Large and quality datasets are critical to ensure the performance, fairness, robustness, reliability, and scalability of ML systems. Data scientists often lack diverse and large datasets to train and test the machine learning models they design. This project focuses on developing a tool that can be deployed to process posting and receiving text and audio files from and into a data lake, apply transformation in a distributed manner, and load it into a warehouse in a suitable format to train a speech-t0-text model.  The general objective of the project is to develop a data engineering pipeline using Apache Kafka, Apache Spark and Airflow to allow collection of millions of Amharic and Swahili audio recordings from speakers reading digital text in app and web platforms. These recordings can be used to produce a large and diverse dataset for training and testing speech-to-text processing models.
</p>
<p>The proposed data pipeline was built on Apache Kafka, an open-source distributed event streaming platform. By combining messaging, storage, and stream processing, the data pipeline allow collection, storage and analysis of real-time audio datasets. The data pipeline consists of the following key components:
</p>
<ol>
    <li>Data producers</li>
    <li>Data consumers</li>
    <li>Apache Kafka cluster</li>
    <li>Amazon S3 bucket Connectors</li>
    <li>Apache Spark Stream preprocessors</li>
</ol>
 <p>

## Project Structure

### [images](images):

- `images/` the folder where all snapshot for the project are stored.

### [logs](logs):

- `logs/` the folder where script logs are stored.

### [data](data):

- `data/` the folder where the dataset files are stored.

### [.github](.github):

- `.github/`: the folder where github actions and unit-tests are integrated.
- `cml.yaml`: the file where the cml configuration is stored.
- `unit_test.yml`: the file where the unit-tests are stored.

### [.vscode](.vscode):

- `.vscode/`: the folder where local path are stored.

### [notebooks](notebooks):

- `notebooks/`: a jupyter notebook for preprocessing the data.
- `data_exploration.ipynb`: a jupyter notebook for data exploration.
- `ml_preprocess.ipynb`: a jupyter notebook for preprocessing the data.
- `causal_inference.ipynb`: a jupyter notebook for causal inference feature extraction.
- `ml_model.ipynb`: a jupyter notebook for machine learning model training.

### [scripts](scripts):

- `scripts/`: folder where modules are stored.
- `causality.py`: a module for causal inference.
- `data_manipulation.py`: a module for data manipulation.
- `data_exploration.py`: a module for data exploration.
- `data_preProcessing.py`: a module for data preprocessing.

### [tests](tests):

- `tests/`: the folder containing unit tests for the scripts.
- `test.py`: the file containing unit tests for the scripts.

### [root folder](#)

- `requirements.txt`: a text file listing the projet's dependancies.
- `.travis.yml`: a configuration file Travis CI for unit test.
- `setup.py`: a configuration file for installing the scripts as a package.
- `results.txt`: a text file containing the results of the cml report.
- `train.py`: a script for training the model.
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.

<hr>

# <a name='Installation guide'></a>Installation guide

### <a name='conda'></a>Conda Enviroment

```bash
conda create --name stt python==3.8
conda activate stt
```

### Next

```bash
git clone https://github.com/Speech-to-text-Kafka-Airflow-Spark/StoTkas.git
cd StoTkas
sudo python3 setup.py install
```

<hr>

# <a name='license'></a>License

[MIT](https://github.com/Speech-to-text-Kafka-Airflow-Spark/StoTkas/blob/main/LICENSE)

<!-- <hr> -->

<!-- # <a name='contributors'></a>Contributors -->

<!-- ![contributors list](https://contrib.rocks/image?repo=Speech-to-text-Kafka-Airflow-Spark/StoTkas)

Made with [contrib.rocks](https://contrib.rocks) -->
