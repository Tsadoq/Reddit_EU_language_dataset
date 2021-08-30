# Reddit EU language dataset
This dataset has been created for a personal project related to the recognition of the original language of someone writing in english.

## Origin
The dataset has been crawled from the subreddit r/europe and contains around 12 milions posts in it's raw form.

## Structure

This repo contains both the [raw data](https://github.com/Tsadoq/Reddit_EU_language_dataset/tree/main/data) and the [cleaned data](https://github.com/Tsadoq/Reddit_EU_language_dataset/tree/main/cleaned_data), the latter, purged of deleted comments and of those that were not linked to the provenience of the writer, contains around 5mln datapoints and has the following structure:

* body: the text content of the comment
* country_name: extended name of the country
* permalink: link to the comment
* author: username of the creator
* created_utc: utc creation 
* datetime: date and time of creation
* alpha2: ISO country alpha2 code
* alpha3: ISO country alpha3 code
* numeric: ISO country number
* apolitical_name: apolitical country name

As it might be imagined, the dataset is far from being balanced with respect to the nationalities:

![image](https://user-images.githubusercontent.com/28503469/131318115-0eafb47b-8898-4f36-b1d1-8216308668ea.png)

## Download
You can download the whole repository or [only the cleaned dataset from this link](https://downgit.github.io/#/home?url=https://github.com/Tsadoq/Reddit_EU_language_dataset/tree/main/cleaned_data)
