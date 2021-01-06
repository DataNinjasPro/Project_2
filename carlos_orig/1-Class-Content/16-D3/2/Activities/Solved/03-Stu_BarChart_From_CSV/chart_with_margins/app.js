// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 640;

// Define the chart's margins as an object
var chartMargin = {
  top: 30,
  right: 30,
  bottom: 30,
  left: 30
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3
  .select("body")
  .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth)
  // Append a group to the SVG area and shift ('translate') it to the right and to the bottom

var chartGroup = svg.append("g")
    .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

// Load data from hours-of-tv-watched.csv
d3.csv("hours-of-tv-watched.csv", function(error, tvData) {

  // Throw an error if one exists
  if (error) throw error;

  // Print the tvData
  console.log(tvData);

  // Cast the hours value to a number for each piece of tvData
  tvData.forEach(function(data) {
    data.hours = +data.hours;
  });

  var scaleY = 10; // 10x scale on rect height
  var barWidth = (chartWidth / tvData.length) - chartMargin.right;

  chartGroup.selectAll(".bar")
    .data(tvData)
    .enter()
    .append("rect")
      .attr("class", "bar")
      .attr("x", (d, i) => i * (barWidth + chartMargin.right))
      .attr("y", data => chartHeight - (data.hours * scaleY))
      .attr("width", barWidth)
      .attr("height", function(data) {
        return (data.hours * scaleY);
      });
});
