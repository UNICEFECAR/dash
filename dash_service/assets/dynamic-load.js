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



//The remote_files_path variable must be present in the hosting page HTML.
//Other paramenters can be passed by the hosting page in a dictionary the var name in "host_params"
//  e.g. host_params = {prj: 'brazil', page: 'child-education'}

//Checks if the browser is supported 
var browserOk = checkBrowser();

if (browserOk) {

    var url_to_update = new URL(window.location.href);

    var qparam_prj = url_to_update.searchParams.get("prj");
    var qparam_page = url_to_update.searchParams.get("page");

    //If the params are not in the query string then try to pull them from the host page config
    //This allows to override the hosting page config
    if (qparam_prj == null) {
        if (host_params && "prj" in host_params){
            qparam_prj = host_params["prj"]
        }
    }
    if (qparam_page == null) {
        if (host_params && "page" in host_params){
            qparam_page = host_params["page"]
        }
    }
    //url_to_update.searchParams.set('prj', host_params['prj']);
    url_to_update.searchParams.set('prj', qparam_prj);
    url_to_update.searchParams.set('page', qparam_page);

    window.history.pushState({}, "", url_to_update);

    //url_to_update.searchParams.set('prj', host_params['prj']);

    function loadDash() {
        var dashRenderer = document.createElement('script');
        dashRenderer.setAttribute('id', '_dash-renderer');
        dashRenderer.setAttribute('type', 'text/javascript');
        dashRenderer.innerHTML = "var renderer = new DashRenderer();";
        document.body.appendChild(dashRenderer);
    }

    //load the json and adds to the page in the callback function
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
            var loadedScripts = 0;
            var withSrc = 0;

            for (var i = 0; i < scripts.length; i++) {
                var src = scripts[i].getAttribute('src');
                if (src && !src.includes('dynamic-load.js')) {
                    withSrc += 1;
                }
            }

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
                //each injected script has an onload function, when the loaded scripts == withSrc then trigger LoadDash
                scriptElement.onload = function () { loadedScripts += 1; if (loadedScripts >= withSrc) { loadDash() } };
                document.body.appendChild(scriptElement);
            }
        });
}