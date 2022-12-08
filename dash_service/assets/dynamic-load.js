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

//Checks if the browser is supported 
var browserOk = checkBrowser();

if (browserOk) {

    //loaad the json and adds to the page in the callback function
    loadJson(remote_files_path,
        function (data) {

            var baseUrl = new URL(remote_files_path);

            // The payload is the dash base HTML, need to inspect resources
            var dash = new DOMParser().parseFromString(data, "text/html");

            // load the css
            var links = dash.getElementsByTagName('link');
            for (var i = 0; i < links.length; i++) {
                var link = links[i];
                var href = link.getAttribute('href');
                var rel = link.getAttribute('rel');
                if (rel == 'stylesheet') {
                    var linkElement = document.createElement('link');
                    linkElement.setAttribute('rel', rel);
                    linkElement.setAttribute('href', href.startsWith('/') ? new URL(href, baseUrl) : href);
                    document.head.appendChild(linkElement);
                }
            }

            // load the html
            var app_entry = dash.getElementById('react-entry-point');
            document.getElementById('root').appendChild(app_entry);

            // load the js
            var scripts = dash.getElementsByTagName("script");
            for (var i = 0; i < scripts.length; i++) {
                var script = scripts[i];
                var src = script.getAttribute('src');
                var id = script.getAttribute('id');
                var type = script.getAttribute('type');
                var scriptElement = document.createElement('script');
                if (src) {
                    // ignore this file to prevent load loops
                    if (src.includes('dynamic-load.js')) {
                        continue;
                    }
                    // set the correct path if it is relative
                    scriptElement.setAttribute('src', src.startsWith('/') ? new URL(src, baseUrl) : src);
                }
                if (id) {
                    scriptElement.setAttribute('id', id);
                }
                if (type) {
                    scriptElement.setAttribute('type', type);
                }
                if (script.innerHTML) {
                    if (script.innerHTML.includes('DashRenderer')) {
                        // Leave the DashRenderer as the last script
                        continue;
                    }
                    if (script.id == '_dash-config') {
                        config = JSON.parse(script.innerHTML);
                        config["url_base_pathname"] = baseUrl;
                        delete config["requests_pathname_prefix"];
                        script.innerHTML = JSON.stringify(config);
                    }
                    scriptElement.innerHTML = script.innerHTML;
                }
                document.body.appendChild(scriptElement);
            }

            function loadDash() {
                // need to wait for the dash libraries to finish loading
                setTimeout(function () {
                    // then load the dash renderer
                    var dashRenderer = document.createElement('script');
                    dashRenderer.setAttribute('id', '_dash-renderer');
                    dashRenderer.setAttribute('type', 'text/javascript');
                    dashRenderer.innerHTML = "var renderer = new DashRenderer();";
                    document.body.appendChild(dashRenderer);
                }, 1000);
            }

            if (document.readyState == 'complete') {
                // load the dash renderer when the page is ready
                loadDash();
            } else {
                // wait for the page to be ready
                document.onreadystatechange = function () {
                    if (document.readyState === "complete") {
                        loadDash();
                    }
                }
            }

        });
}