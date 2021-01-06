// data
var dataArray = [1, 2, 3];
var dataCategories = ["one", "two", "three"];

// svg container
var height = 200;
var width = 500;

// margins
var margin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
};

// chart area minus margins
var chartHeight = height - margin.top - margin.bottom;
var chartWidth = width - margin.left - margin.right;

// scale y to chart height
var yScale = d3.scaleLinear()
    .domain([0, d3.max(dataArray)])
    .range([chartHeight, 0]);

// scale x to chart width
var xScale = d3.scaleBand()
    .domain(dataCategories)
    .range([0, chartWidth]);

// create axes
var yAxis = d3.axisLeft(yScale);
var xAxis = d3.axisBottom(xScale);

// create svg container
var svg = d3.select("body").append("svg")
    .attr("height", height)
    .attr("width", width);

// shift everything over by the margins
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// set x to the bottom of the chart
chartGroup.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(xAxis);

// set y to the y axis
chartGroup.append("g")
    .call(yAxis);

// Append Data to chartGroup
// chartGroup.selectAll(".bar")
//     .data(dataArray)
//     .enter().append("rect")
//     .attr("class", "bar")
//     .attr("x", function(d, i) {
//         return xScale(dataCategories[i]);
//     })
//     .attr("y", d => yScale(d))
//     .attr("width", xScale.bandwidth())
//     .attr("height", d => chartHeight - yScale(d));

var div = d3.select("body").append("div")
    .attr("id", "tooltip");

chartGroup.selectAll("rect")
    .data(dataArray)
    .enter()
    .append("rect")
    .attr("x", (d, i) => xScale(dataCategories[i]))
    .attr("y", d => yScale(d))
    .attr("width", xScale.bandwidth())
    .attr("height", d => chartHeight - yScale(d))
    .attr("fill", "green")
    .on("mouseover", function () {
        d3.select(this)
            .transition()
            .duration(250)
            .attr("fill", "red");
    })
    .on("mouseout", function () {
        d3.select(this)
            .transition()
            .duration(250)
            .attr("fill", "blue");
    })
    // .on("mouseover", function (d) {
    //     var x = parseFloat(d3.select(this).attr("x")) +
    //         xScale.bandwidth() / 2;

    //     var y = parseFloat(d3.select(this).attr("y")) /
    //         2 + chartHeight / 2;

    //     d3.select("#tooltip")
    //         .style("left", x + "px")
    //         .style("top", y + "px")
    //         .style("display", "block")
    //         .text(d);
    // })
    // .on("mouseout", function () {
    //     d3.select("#tooltip")
    //         .style("display", "none");
    // });
