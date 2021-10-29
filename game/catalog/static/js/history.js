function get_data(url) {  
   fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        result = response.json()
        status_code = response.status;
        if(status_code != 200) {
            console.log('Error in getting info!')
            return false;
        }      
        return result
    })
	.then(result => {
            console.log(result.html);
	    return result;
        //document.getElementById("new-html").innerHTML = result.html;

    })
    .catch(error => {
        console.log(error)
    })
}

function check_it(){
    url = '/catalog/test_data/'
    get_data(url)
}

function load_note(){
    url = '/catalog/load_note/'
    get_data(url)
}    

load_note()
//check_it()
get_data('/catalog/test_data/')
// template
// <button onClick="sendAnswer(question={{questionId}})>
//  ... 
//    <select>
//       {{ for x in answers }}
//  |
//  | <---- параметри для генерації 
//  |           шаблона(наприклад список відповідей)
//  | <---- конфігурацію аджакс для запитів до сервера
//  |
//  V
//  <button id="sendAnswer(question=12)> 
//    <select id....>
//        <item> Yes </item>
//        <item> No </item>

      //  <li class="mine"><span>I have something for you.</span></li>
     //   <li><span>What is it?</span></li>




// $.ajax({
//     url: "/add_book/",
//     type: "POST",
//     data: $('#form').serialize();
//     success: function(data) {
//         if (data['result'] == 'success') {
//             console.log('ok');
//             $("#form .result").append(data['response']);
//         }
//         else if (data['result'] == 'error') {
//             console.log('error');
//             $("#form .error").append(data['response']);
//         }
//     },
// });
