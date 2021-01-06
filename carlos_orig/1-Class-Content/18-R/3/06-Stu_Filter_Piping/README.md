# The Cerealverse

This activity allows students to practice:

  * Using `select` to extract specific columns of a tibble

  * Using `filter` to extract specific rows of a tibble

  * Using `starts_with`, `ends_with`, and `contains` to specify groups of columns to extract

## Instructions

#### Selection

* Read the data in `cereals.csv` into a tibble, called `cereal.tb`.

* Extract every column in `cereal.tb`, _except_ for `rating`, and any column ending in the string -_ium_. 

  * Save this to a tibble called `cereal2.tb`. 
  
You will use `cereal2.tb` for the remainder of the challenges.

#### Filtering

* Filter out only rows whose `type` value is equal to `"H"`.

* Filter out only rows whose `mfr` value is `"A"`, `"N"`, `"Q"`, or `"R"`.

* Filter all rows with a `calorie` count less than `100` _and_ a `fiber` count greater than or equal to `3`.

* Filter out all rows with a `sugars` count greater than `11` _or_ a `fat` count greater than 3.

## Hints

* See the snippet below for an example of using the `%in%` operator.

```r
example_dataframe %>%
  filter(name %in% c("Moe", "Larry", "Curly"))
```
