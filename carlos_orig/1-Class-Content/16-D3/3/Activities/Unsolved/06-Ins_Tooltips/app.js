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

  var pizzasEatenByMonth = [15, 5, 25, 18, 12, 22, 0, 4, 15, 10, 21, 2];
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

  var svg = d3.select(".chart").append("svg").attr("height", svgHeight).attr("width", svgWidth);

  // line generator
  var line = d3.line()
    .x(function(data, index) {
      return index * svgWidth / 20;
    })
    .y(function(data, index) {
      return 600 - (data * svgHeight / 80);
    });

  var chart = svg.append("g").attr("transform", "translate(100,-300)");

  chart.append("path")
    .attr("d", line(pizzasEatenByMonth))
    .attr("fill", "none")
    .attr("stroke", "blue");

  // Step 1: Append a div to the body to create tooltips, assign it a class
  //= ======================================================
  var div = d3.select("body").append("div").attr("class", "tooltip");
  chart.selectAll("circle")
    .data(pizzasEatenByMonth)
    .enter().append("circle")
    .attr("cx", function(data, index) {
      return index * svgWidth / 20;
    })
    .attr("cy", function(data, index) {
      return 600 - (data * svgHeight / 80);
    })
    .attr("r", "5")
    .attr("fill", "red")
    .on("click", function(data, index) {
      div.style("display", "block");
      div.html("Pizzas eaten: " + pizzasEatenByMonth[index])
        .style("left", d3.event.pageX + "px")
        .style("top", d3.event.pageY + "px");
    })
    // .on("mouseover", function(data, index) {
    //   div.style("display", "block");
    //   div.html("Pizzas eaten: " + pizzasEatenByMonth[index])
    //     .style("left", d3.event.pageX + "px")
    //     .style("top", d3.event.pageY + "px");
    // })
    // .on("mouseout", function(){
    //   div.style("display", "none");
    // })

    // Step 2: Add an onclick event to display an alert message
    //= =======================================================
    // Step 3: Add an onmouseover event to display a tooltip
    ;
}
