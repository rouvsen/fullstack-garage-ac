class User {
    constructor(name, surname, password) {
        this.name = name;
        this.surname = surname;
        this.password = password;
    }
    fullname() { return `${this.name} ${this.surname}`; }
}

var user = new User("Alex", "Marckon", "passs");

const writeFullnameLikeUpperCase = () => {
    var fullnameUpper = user.fullname().toUpperCase();
    var p = document.createElement("p");
    p.textContent = fullnameUpper;
    document.body.appendChild(p);
}

writeFullnameLikeUpperCase();