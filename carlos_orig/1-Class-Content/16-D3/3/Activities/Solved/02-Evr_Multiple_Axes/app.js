// Step 0: Set up our chart
//= ================================
var svgWidth = 960;
var svgHeight = 500;

var margin = { top: 20, right: 40, bottom: 60, left: 50 };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3
  .select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)

var chartGroup = svg.append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Import data from the mojoData.csv file
d3.csv("mojoData.csv", function(error, mojoData) {
  if (error) throw error;
  console.log(mojoData);
  console.log([mojoData]);
  // Create a function to parse date and time
  var parseTime = d3.timeParse("%d-%b");

  // Format the data
  mojoData.forEach(function(data) {
    data.date = parseTime(data.date);
    data.morning = +data.morning;
    data.evening = +data.evening;
  });

  // Step 1: Set up the x-axis, and two y-axes
  //= ============================================
  // Set the ranges with scaling functions
  var xTimeScale = d3.scaleTime().range([0, width]);

  var yLinearScale = d3.scaleLinear().range([height, 0]);

  var yLinearScale2 = d3.scaleLinear().range([height, 0]);

  // Create axis functions
  var bottomAxis = d3.axisBottom(xTimeScale);
  var leftAxis = d3.axisLeft(yLinearScale);
  var rightAxis = d3.axisRight(yLinearScale2);

  /* Comments:
Note that we have two scales for the y-axis.
Each row in our dataset contains three points:
  a. The date, which we plot on the x-axis.
  b. Morning, which we plot on the y-axis on the left side.
  c. Evening, which also plot on the y-axis on the right side.
We therefore need to plot morning and evening values separately--they will each have their own y-scale function.

Note also that yAxis is d3.axisRight(). This does not mean that the axis will automatically be placed on the right side of the screen. Rather, it means that the tick marks will be placed to the right side of the axis, wherever the axis i
*/

  // Step 2: Scale the domain for each axis
  //= ============================================
  // Scale the domain
  xTimeScale.domain(
    d3.extent(mojoData, function(data) {
      return data.date;
    })
  );

  yLinearScale.domain([
    0,
    d3.max(mojoData, function(data) {
      return data.morning;
    })
  ]);

  yLinearScale2.domain([
    0,
    d3.max(mojoData, function(data) {
      return data.evening;
    })
  ]);

  /* Comments:
1. Once again, note that we will have two y-axes:  one on the left for morning data, and one on the right for evening data.
*/

  // Line generators for each line
  var line1 = d3
    .line()
    .x(function(data) {
      return xTimeScale(data.date);
    })
    .y(function(data) {
      return yLinearScale(data.morning);
    });

  var line2 = d3
    .line()
    .x(function(data) {
      return xTimeScale(data.date);
    })
    .y(function(data) {
      return yLinearScale2(data.evening);
    });

  // Append a path for line1
  chartGroup.append("path").data([mojoData]).attr("d", line1).attr("class", "line green");

  // Append a path for line2
  chartGroup.append("path").data([mojoData]).attr("d", line2).attr("class", "line orange");

  // Add bottomAxis
  chartGroup.append("g").attr("transform", "translate(0," + height + ")").call(bottomAxis);

  // Add leftAxis to the left side of the display
  chartGroup.append("g").call(leftAxis);

  // Add rightAxis to the right side of the display
  chartGroup.append("g").attr("transform", "translate(" + width + ",0)").call(rightAxis);

  /* Comments:
1. svg.append('g')
    .attr("transform", "translate(" + width + ",0)")
    .call(yAxis1)
To place yAxis1 on the right side of the chart, we translate the axis by the width of the chart on the x-axis. In other words, we shift it from the left side of the chart area all the way to the right.
*/
});
