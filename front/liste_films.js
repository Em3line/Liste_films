function test() {
  document.write("ok");
}

class Film {
  constructor(titre) {
    this.titre = titre;
  }
}

let films = [];
function addFilm(titre) {
  films.push(new Film(titre));
}


function getFilms(){
  for (let i = 0 ; i < films.length ; i++) {
    document.write("<div><h2>" + films[i].titre + "</h2><span>Note : 10/10</span></div >");
  }
}

addFilm("Dragon");
addFilm("Mulan");
addFilm("The Words");
getFilms();
