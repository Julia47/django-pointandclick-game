var test_history = ["test1 asafddafdasfsafsaf", "test2 fwqfqwfrefrefrefre", "test3 qfrqfqfefefererefef"];

function render_history(list_history){
   var element = document.getElementById('history');
   str = '';
   for(var i=0;i<list_history.length;i++){
       str += '<li class="mine"><span>' + list_history[i] + '</span></li>';
   }
   element.innerHTML = str;
}

render_history(test_history);



      //  <li class="mine"><span>I have something for you.</span></li>
     //   <li><span>What is it?</span></li>
