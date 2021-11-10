function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

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
            console.log(result);
	    document.getElementById("new-html").innerHTML = result.html;
	    return result;
    })
    .catch(error => {
        console.log(error)
    })
}


function check_it(answer){
    //    url = '/catalog/test_data/'
    // url = '/catalog/load_note/'
    // get_data(url)

    console.log(answer);
    let url = '/catalog/load_question?answer=' + answer;
    console.log(url);
    let data = "heyy";
    let csrftoken = getCookie('csrftoken');
    const request = new Request(
	url,
	{headers: {'X-CSRFToken': csrftoken}}
    );
    fetch(request, {
	method: 'GET',
	// body: answer,
	// data:  JSON.stringify({
	//     data}) ,
	mode: 'same-origin'  // Do not send CSRF token to another domain.
    }).then(response => {
        result = response.json()
        status_code = response.status;
        if(status_code != 200) {
            console.log('Error in getting info!')
            return false;
        }      
        return result
    })
	.then(result => {
            console.log(result);
	    document.getElementById("new-html").innerHTML = result.html;
	    return result;
    })
    .catch(error => {
        console.log(error)
    })

// credentials : 'same-origin'
     // headers: { "X-CSRFToken": csrftoken },
}

function load_note(){
    url = '/catalog/load_note/'
    get_data(url)
}

// !! TO DO Problem with spaces in url

function notes(){
    window.location.assign("notes");
}

function logout(){
    window.location.assign("logout");
}

function yes_start(){
    window.location.assign("/catalog/house/");
}

function no_start(){
    window.location.assign("/catalog/user_table/");
}    

load_note();
//check_it('first_ lk');

