const sounds_list = []

function check_piano(){
  if (sounds_list.join('') == piano.password) {
     console.log(piano.password);
     location.href="/catalog/piano_secret"
  }
}

function clean_sounds(){
  sounds_list = [];
}
function play_c(){
  var audio = new Audio(piano_c);
  audio.play();
}
function play_d() {
  var audio = new Audio(piano_d);
  audio.play();
}
function play_e() {
  var audio = new Audio(piano_e);
  audio.play();
}
function play_f() {
  var audio = new Audio(piano_f);
  audio.play();
}
function play_g() {
  var audio = new Audio(piano_g);
  audio.play();
}
function play_a() {
  var audio = new Audio(piano_a);
  audio.play();
}
function play_b() {
  var audio = new Audio(piano_b);
  audio.play();
}

function play_sound(sound) {
    sounds_list.push(sound);
    switch (sound) {
      case 'a':
        play_a();
        break;
      case 'b':
        play_b();
        break;
      case 'c':
        play_c();
        break;
      case 'd':
        play_d();
        break;
      case 'e':
        play_e();
        break;
      case 'f':
        play_f();
        break;
      case 'g':
        play_g();
        break;
    }
    check_piano();
}

