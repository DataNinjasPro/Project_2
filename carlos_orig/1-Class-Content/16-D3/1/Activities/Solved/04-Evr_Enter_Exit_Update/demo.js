var austin_temps = [76, 59, 59, 73, 71];

/***********************************************************
 * Basic Data Bind
 ***********************************************************/

//Basic Bind
d3.selectAll('div')
    .data(austin_temps)
    .style("height", function (d) {
        return d + "px";
    });


/***********************************************************
 * Updates only the new elements
 ***********************************************************/
//Enter - Updates New Elements
d3.select("#content").selectAll(".temps")
    .data(austin_temps)
    .enter()
    .append("div")
    .classed("temps", true)
    .style("height", function (d) {
        return d + "px";
    });


/***********************************************************
 * Enter - Updates Old Elements
 ***********************************************************/

var selection = d3.select("#content").selectAll(".temps")
    .data(austin_temps)

selection.enter()
    .append("div")
    .classed("temps", true)

selection.style("height", function (d) {
    return d + "px";
});


/***********************************************************
 * Enter - Updates New Elements
 ***********************************************************/
var selection = d3.select("#content").selectAll(".temps")
    .data(austin_temps);

selection.enter()
    .append("div")
    .classed("temps", true)
    .merge(selection)
    .style("height", function (d) {
        return d + "px";
    });


/***********************************************************
// Exit Pattern
***********************************************************/
var austin_temps = [76];

var selection = d3.select("#content").selectAll(".temps")
    .data(austin_temps);

selection.enter()
    .append("div")
    .classed("temps", true)
    .merge(selection)
    .style("height", function (d) {
        return d + "px";
    });

selection.exit().remove();


/***********************************************************
 * Enter - Update - Exit Pattern
 * https://bl.ocks.org/mbostock/3808218
 ***********************************************************/

function update(data) {

    var selection = d3.select("#content").selectAll(".temps")
        .data(austin_temps);

    selection.enter()
        .append("div")
        .classed("temps", true)
        .merge(selection)
        .style("height", function (d) {
            return d + "px";
        });

    selection.exit().remove();
}

/* Test 1 */
var austin_temps = [100, 103, 105, 110, 100, 98];
update(austin_temps);

/* Test 2 */
austin_temps = [80];
update(austin_temps);
