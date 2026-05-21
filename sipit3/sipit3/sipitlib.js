function APIQuery(jobj,url, funccall){
    //obj={ name:jparam, prezime:"Pezelj" };
    var objJSON=JSON.stringify(jobj);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        funccall(xmlhttp.response);
      }
    };
    xmlhttp.open("POST", url, true);
    //xmlhttp.responseType="json";
    xmlhttp.responseType="text";
  
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("postVar="+objJSON);
    };