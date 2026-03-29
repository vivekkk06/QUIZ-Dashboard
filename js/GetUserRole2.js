function GetUserRole(name, role){
    switch (role){
        case "Admin":
            return `${name} is Admin, He has full access`;
        case "subAdmin":
            return `${name} is subAdmin, He has access to remove/add courses`;
        case "TestPrep":
            return `${name} is TestPrep, He has access to create/delete content`;
        case "user":
            return `${name} is user, He has access to consume content`;
        default:
            return `${name} is a trial user`;
    }
}

console.log(GetUserRole("hio", "subAdmin"));
console.log(GetUserRole("hio", "Admin"));
console.log("hello world");