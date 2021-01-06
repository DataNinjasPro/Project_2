# GMO Cotton

This activity allows students to practice:

  * Gathering tibbles into key-value pairs

  * Creating plots with Plotly's R API

## Instructions

* Begin by loading `ge_cotton.tsv` into `cotton.tb`.

* Create a tibble, called `gathered.cotton.tb`, which contains key-value pairs with `Year` as the key and `Percent.GMO` as the value.

  * Omit `State` and `"GMO Type"` from gathering.


* Create a tibble, called `ins_resist`, by filtering only insect-resistant GMO cotton from `gathered.cotton.tb`.

* Create a tibble, called `herb_tol`, by filtering only herbicide-tolerant GMO cotton from `gathered.cotton.tb`.

* Use `plot_ly` and `ins_resist` to create a scatter plot of `Percent.GMO` over `Year`.

  * Save the return value of `plot_ly` into `ins_plot`.

* Use `plot_ly` and `herb_tol` to create a scatter plot of `Percent.GMO` over `Year`.

  * Save the return value of `plot_ly` into `herb_plot`.

* Use `subplot` to arrange `ins_plot` and `herb_plot` into two rows.

  * Allow `ins_plot` and `herb_plot` to share the x-axis.
