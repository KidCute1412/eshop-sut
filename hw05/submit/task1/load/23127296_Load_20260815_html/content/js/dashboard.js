/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 44.961977186311785, "KoPercent": 55.038022813688215};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.44961977186311786, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "05 GET /api/categories"], "isController": false}, {"data": [0.0, 500, 1500, "07 GET /api/cart"], "isController": false}, {"data": [0.0, 500, 1500, "06 POST /api/cart"], "isController": false}, {"data": [1.0, 500, 1500, "02 GET /api/products"], "isController": false}, {"data": [1.0, 500, 1500, "03 GET /api/products search"], "isController": false}, {"data": [1.0, 500, 1500, "04 GET /api/products/:id"], "isController": false}, {"data": [0.0, 500, 1500, "01 POST /api/login"], "isController": false}, {"data": [0.0, 500, 1500, "09 GET /api/orders/my-orders"], "isController": false}, {"data": [0.0, 500, 1500, "08 POST /api/checkout"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 1052, 579, 55.038022813688215, 1.831749049429657, 1, 123, 2.0, 2.0, 3.0, 4.0, 4.417384001679614, 1.8614392517845895, 0.9603937578731891], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["05 GET /api/categories", 117, 0, 0.0, 1.7948717948717952, 1, 4, 2.0, 2.0, 3.0, 3.819999999999993, 0.5208820268988821, 0.18210523987285135, 0.10020874931550759], "isController": false}, {"data": ["07 GET /api/cart", 116, 116, 100.0, 1.3534482758620685, 1, 3, 1.0, 2.0, 2.0, 3.0, 0.5131744262179044, 0.14783833567800958, 0.09571905801525367], "isController": false}, {"data": ["06 POST /api/cart", 117, 117, 100.0, 1.6153846153846145, 1, 3, 2.0, 2.0, 3.0, 3.0, 0.5177128596334416, 0.14914579452330592, 0.12922511908501996], "isController": false}, {"data": ["02 GET /api/products", 120, 0, 0.0, 1.8583333333333332, 1, 5, 2.0, 2.9000000000000057, 3.0, 4.789999999999992, 0.5083841011345438, 0.6146284347700833, 0.09681142550901958], "isController": false}, {"data": ["03 GET /api/products search", 118, 0, 0.0, 1.8220338983050848, 1, 5, 2.0, 2.0, 3.0, 4.810000000000002, 0.5107009153664712, 0.15202853487264936, 0.10472935962216788], "isController": false}, {"data": ["04 GET /api/products/:id", 118, 0, 0.0, 1.7203389830508482, 1, 4, 2.0, 2.1000000000000085, 3.0, 3.8100000000000023, 0.5119194811392377, 0.2306416889004577, 0.09848450955510726], "isController": false}, {"data": ["01 POST /api/login", 120, 120, 100.0, 3.125000000000001, 1, 123, 2.0, 3.0, 3.0, 98.42999999999907, 0.5104124132298897, 0.15651318140057166, 0.1362844342291071], "isController": false}, {"data": ["09 GET /api/orders/my-orders", 112, 112, 100.0, 1.392857142857143, 1, 3, 1.0, 2.0, 2.0, 3.0, 0.5030068130476374, 0.14490918930571586, 0.09971717094596719], "isController": false}, {"data": ["08 POST /api/checkout", 114, 114, 100.0, 1.7456140350877194, 1, 5, 2.0, 2.0, 3.0, 4.849999999999994, 0.5089285714285714, 0.14661516462053573, 0.14005824497767858], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["403/Forbidden", 459, 79.27461139896373, 43.631178707224336], "isController": false}, {"data": ["401/Unauthorized", 120, 20.72538860103627, 11.406844106463879], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 1052, 579, "403/Forbidden", 459, "401/Unauthorized", 120, "", "", "", "", "", ""], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": ["07 GET /api/cart", 116, 116, "403/Forbidden", 116, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["06 POST /api/cart", 117, 117, "403/Forbidden", 117, "", "", "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["01 POST /api/login", 120, 120, "401/Unauthorized", 120, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["09 GET /api/orders/my-orders", 112, 112, "403/Forbidden", 112, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["08 POST /api/checkout", 114, 114, "403/Forbidden", 114, "", "", "", "", "", "", "", ""], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
