// When the browser window is resized, responsify() is called.
d3.select(window).on("resize", makeResponsive);

// When the browser loads, makeResponsive() is called.
makeResponsive();

// The code for the chart is wrapped inside a function that automatically resizes the chart
function makeResponsive() {
  // if the SVG area isn't empty when the browser loads, remove it and replace it with a resized version of the chart
  var svgArea = d3.select("body").select("svg");
  if (!svgArea.empty()) {
    svgArea.remove();
  }

  // SVG wrapper dimensions are determined by the current width and height of the browser window.
  var svgWidth = window.innerWidth;
  var svgHeight = window.innerHeight;

  var svg = d3
    .select(".chart")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

  d3.csv("pizzaData.csv", function(err, pizzaData) {
    // line generator
    var line = d3
      .line()
      .x(function(data, index) {
        return index * svgWidth / 20;
      })
      .y(function(data, index) {
        return 600 - +data.pizzasEaten * svgHeight / 80;
      });

    var chart = svg.append("g").attr("transform", "translate(100,-300)");

    chart
      .append("path")
      .attr("d", line(pizzaData))
      .attr("fill", "none")
      .attr("stroke", "blue");

    // Append a div to the body to create tooltips, assign it a class
    d3.select("body").append("div").attr("class", "tooltip");

    var toolTip = d3
      .tip()
      .attr("class", "tooltip")
      .offset([40, -60])
      .html(function(data) {
        var numPizzas = +data.pizzasEaten;
        var month = data.month;
        return "The pizza monster ate " + numPizzas + " pizzas in " + month;
      });

    chart.call(toolTip);

    chart
      .selectAll("circle")
      .data(pizzaData)
      .enter()
      .append("circle")
      .attr("cx", function(data, index) {
        return index * svgWidth / 20;
      })
      .attr("cy", function(data, index) {
        return 600 - +data.pizzasEaten * svgHeight / 80;
      })
      .attr("r", "5")
      .attr("fill", "red")
      // onclick event to display an alert message
      .on("click", function(data, index) {
        toolTip.show(data);
      })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });
  });
}
