
window.onload = initall;


var saveAnsButton;

var saveAnsButton2;


function initall(){

    

    saveAnsButton= document.getElementById("save_ans");
    saveAnsButton.onclick = saveans;
    
    saveAnsButton2 = document.getElementById("submitAnswer1").disabled=true ;
    
   
    
}

function saveans(){
    
    var ans = $("input:radio[name=name]:checked").val();

   
    
    

    if(ans == null) {
        alert("Please Select Any Option!")
        saveAnsButton2 = document.getElementById("submitAnswer1").disabled=true;
    }

    if(ans != null){
    alert("NOTE: YOU CANNOT CHANGE THE ANSWER ONCE PRESSED  'OK'         \n                             ANSWER SUBMITTED PRESS 'NEXT' ")
    var url = '/saveans?ans='+ans
    saveAnsButton= document.getElementById("save_ans").disabled=true;
    saveAnsButton2 = document.getElementById("submitAnswer1").disabled=false; 
     
}
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
       // alert(req.responseText)
        }
      };
    
    req.open("GET",url,true);
    req.send();
}




