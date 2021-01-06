# Mean Machine

In this activity, we want to calculate the arithmetic mean for a range of numbers excluding any outliers. Outliers in this case will be determined by the [outer fence](https://www.wikihow.com/Calculate-Outliers)

## Instructions

* Create a custom vba function that will accept a range of numbers

* Calculate the outer fence for that range of numbers

* Calculate the mean for all values within the boundaries of the outer fence

  * The lower boundary is the first quartile minus the outer fence

  * The upper boundary is the third quartile plus the outer fence

## Hints

* Use the `Application.WorksheetFunction` to call excel formulas

* Use the excel `quartile` formula to calculate the first and third quartile

- - -

### Copyright

Coding Boot Camp © 2017. All Rights Reserved.
