
//This function just checks the browser version and prevents loading the app if the Browser is not supported
function checkBrowser() {
    var ES6_Error = false;

    function check() {
        "use strict";

        if (typeof Symbol == "undefined") return false;
        try {
            eval("class A {}");
            eval("var B = (x) => x+1");
        } catch (e) {
            return false;
        }

        return true;
    }
    // The engine supports ES6 features you want to use
    if (!check()) {
        ES6_Error = true;
        document.getElementById('main').style.display = "none";
        document.getElementById('mainUpdateBrowser').style.display = "";
        return false;
    }
    return true;
}

//Joins the paths given the parts and the separator
const pathjoin = (parts, sep) => {
    var separator = sep || '/';
    var replace = new RegExp(separator + '{1,}', 'g');
    return parts.join(separator).replace(replace, separator);

}

//Loads a json file and calls the onsuccess callback, ToDo: add a onerror callback
function loadJson(url, onsuccess) {
    var xmlhttp = new XMLHttpRequest();
    /*xmlhttp.setRequestHeader("Accept", 'application/json');
    xmlhttp.withCredentials=true;*/

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {   // XMLHttpRequest.DONE == 4
            if (xmlhttp.status == 200) {
                var data = xmlhttp.responseText;
                onsuccess(data);
            }
            else if (xmlhttp.status == 400) {
                alert('There was an error 400');
            }
            else {
                alert('something else other than 200 was returned');
            }
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

//Gets and returns the URL params that are needed by the data explorer.
function getUrlParams() {
    const url = new URL(window.location);
    const ret = [];
    let dq = url.searchParams.get("dq");
    if (dq) {
        dq = dq.replaceAll(" ", "+");
        ret.push({ param: "dataquery", val: dq });
    }

    let startPeriod = url.searchParams.get("startPeriod");
    let endPeriod = url.searchParams.get("endPeriod");
    if (startPeriod) {
        startPeriod = parseInt(startPeriod);
        ret.push({ param: "startPeriod", val: startPeriod });
    }
    if (endPeriod) {
        endPeriod = parseInt(endPeriod);
        ret.push({ param: "endPeriod", val: endPeriod });
    }

    ret.push({ param: "agencyId", val: url.searchParams.get("ag") });
    ret.push({ param: "dataflowId", val: url.searchParams.get("df") });
    ret.push({ param: "ver", val: url.searchParams.get("version") });


    let lastn = url.searchParams.get("lastnobservations");
    if (lastn) {
        lastn = parseInt(lastn);
        ret.push({ param: "lastnobservations", val: lastn });
    }

    //https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,GLOBAL_DATAFLOW,1.0/UNICEF_ESA.NT_ANT_HAZ_NE2.?dimensionAtObservation=AllDimensions&startPeriod=2010&endPeriod=2020&lastnobservations=1
    return ret;
}

//Add the react scripts to the page
function addReactScripts(de_cfg, remotePath, ver) {
    //The DATAFLOW part of the configuration
    DATAFLOW = de_cfg.DATAFLOW;
    //Get the url params
    const urlParams = getUrlParams();

    //For each URL param override the default config in DATAFLOW
    for (var i = 0; i < urlParams.length; i++) {
        if (urlParams[i].val) {
            if (urlParams[i].param == "startPeriod") {
                DATAFLOW.period[0] = urlParams[i].val;
            }
            else if (urlParams[i].param == "endPeriod") {
                DATAFLOW.period[1] = urlParams[i].val;
            }
            else {
                DATAFLOW[urlParams[i].param] = urlParams[i].val;
            }
        }
    }

    //OVverride the default settings
    SETTINGS.sdmx.datasources = de_cfg.SETTINGS_override;
    SETTINGS.unicef = de_cfg.unicef_settings;
    SETTINGS.hierarchy = de_cfg.HIERARCHY_override;
    SETTINGS.map = de_cfg.map_settings;
    SETTINGS.downloadFullEnabled = de_cfg.downloadFullEnabled;

    if (de_cfg.helpUrl)
        SETTINGS.helpUrl = de_cfg.helpUrl;
    if (de_cfg.timeDimensionOrder) {
        SETTINGS.timeDimensionOrder = de_cfg.timeDimensionOrder;
    }

    //Create a <script> element in th DOM and add the js files 
    var basepath = "/de/static/js/";
    var to_add = ["bundle.js", "2.chunk.js", "main.chunk.js"];
    for (i = 0; i < to_add.length; i++) {
        var node = document.createElement('script')
        node.setAttribute('src', remotePath + basepath + to_add[i] + "?v=" + ver);
        document.body.appendChild(node);
    }
}

//Add a script element to the dom and calls the callback
function addScript(src, callback) {
    var s = document.createElement('script');
    s.setAttribute('src', src);
    s.onload = callback;
    document.body.appendChild(s);
}

//Adds ..css and additional .js resources
function addResources(remote_files_path, version) {
    var to_add_css = [
        "/css/data_explorer.css",
        "/de/static/css/main.chunk.css",
        "/de/static/css/2.chunk.css"
    ];
    var to_add_js = [
        "/js/url_changer.js",
    ];

    for (var i = 0; i < to_add_css.length; i++) {
        var l = document.createElement("link");
        l.rel = "stylesheet";
        l.href = remote_files_path + to_add_css[i] + "?v=" + version;
        document.body.appendChild(l);
    }

    for (var i = 0; i < to_add_js.length; i++) {
        var l = document.createElement("script");
        l.setAttribute("src", remote_files_path + to_add_js[i] + "?v=" + version);
        document.head.appendChild(l);
    }
}

//Checks if the browser is supported 
var browserOk = checkBrowser();

if (browserOk) {
    //Create a string containing the current timestamp
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0
    var yyyy = today.getFullYear();
    var hours = String(today.getHours()).padStart(2, '0');
    //Forces the load a new version every 24/4=6 hours (reduce when the .js is stable)
    hours = Math.floor(hours / 4);
    today = yyyy + mm + dd + hours;

    //json_config is the id passed by the hosting environment (Wordpress, Drupal...)
    //remote files path is hardcoded in the hosting env (should be a param too but we have been asked to reduce to the minimum the params)
    var cfgFileName = json_config + ".json?v=" + today;
    var cfg_url = pathjoin(["configs", cfgFileName]);
    if (remote_files_path.endsWith("/")) {
        cfg_url = remote_files_path + cfg_url;
    }
    else {
        cfg_url = remote_files_path + "/" + cfg_url;
    }

    //loaad the json and adds to the page in the callback fun
    loadJson(cfg_url,
        function (data) {
            //Load the cfg file
            var cfg = JSON.parse(data);
            //settings.js contains the default settings that will be overridden
            addScript(remote_files_path + "/js/de_settings/settings.js" + "?v=" + today,
                function () {
                    //Add all the DataExplorer scripts
                    addReactScripts(cfg, remote_files_path, today);
                }
            );
            //Add the remaining resources
            addResources(remote_files_path, today);
            //addScript(remote_files_path + "/js/url_changer.js" + "?v=" + today)
        });
}

