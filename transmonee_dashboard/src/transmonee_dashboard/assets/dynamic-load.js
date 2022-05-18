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

//Add a script element to the dom and calls the callback
function addScript(src, callback) {
    var s = document.createElement('script');
    s.setAttribute('src', src);
    s.onload = callback;
    document.body.appendChild(s);
}

//Checks if the browser is supported 
var browserOk = checkBrowser();

if (browserOk) {

    //loaad the json and adds to the page in the callback fun
    loadJson(remote_files_path,
        function (data) {

            var baseUrl = new URL(remote_files_path);
            console.log(baseUrl);

            // The payload is the dash base HTML, need to inspect resources
            var dash = new DOMParser().parseFromString(data, "text/html");
            console.log(dash);

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
            var scripts = dash.getElementsByTagName("script");
            for (var i = 0; i < scripts.length; i++) {
                var script = scripts[i];
                var src = script.getAttribute('src');
                var scriptElement = document.createElement('script');
                if (src) {
                    // ignore this file to prevent load loops
                    if (src.includes('dynamic-load.js')) {
                        continue;
                    }
                    scriptElement.setAttribute('src', src.startsWith('/') ? new URL(src, baseUrl) : src);
                }
                if (script.innerHTML) {
                    scriptElement.innerHTML = script.innerHTML;
                }
                document.body.appendChild(scriptElement);
            }

        });
}