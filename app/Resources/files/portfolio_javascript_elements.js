
          function goBack() {
               window.history.back();
          } // This is the function that works with the
            // "Back" button html

          function httpGet(theUrl) {
              var xmlHttp = new XMLHttpRequest();
              xmlHttp.open("GET", theUrl, false); // This makes an
              xmlHttp.send(); // http request and loads it as json data
              return JSON.parse(JSON.parse(xmlHttp.responseText));
          }

          function Main() {
              var Languages = httpGet("/portfolio/files/names");
              console.log(Languages.length);
              var index = -1;
              while (index <= Languages.length) {

                  index++;

                  Language = Languages[index];

                  if (Language == undefined) {
                      return;
                  }

                  Language_Len_Link = "/portfolio/len_files/" + Language;
                  Language_Len = httpGet(Language_Len_Link);

                  var NewLine = document.createElement("br");

                  var lang_anchor = document.createElement("a");
                  lang_anchor.innerHTML = Language;
                  lang_anchor.class = "textClass";
                  lang_anchor.href = "/portfolios/" + Language;

                  var lang_len_anchor = document.createElement("a");
                  lang_len_anchor.innerHTML = Language_Len;
                  lang_len_anchor.class = "textClass";
                  lang_len_anchor.href = "/portfolios/" + Language;

                  var body = document.getElementsByTagName("body")[0];
                  var div = body.getElementsByTagName("div")[0];

                  div.appendChild(lang_anchor);
                  div.appendChild(lang_len_anchor);
                  div.appendChild(NewLine);

              }
          }


          if (document.readyState!='loading') {
              Main();
          }

          else if (document.addEventListener) {
              document.addEventListener('DOMContentLoaded', Main);
          }

          else document.attachEvent('onreadystatechange', function(){
              if (document.readyState=='complete') {
                  Main();
              }
          });



// This is a snippet
// of the code from
// the portfolio page
// that retrives the
// document folders
// and the count for
// each folder