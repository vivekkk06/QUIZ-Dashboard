function GetUserRole(name, role){
    switch (role){
        case "Admin":
            console.log(`${name} is Admin, He has full access`)
            break;
        case "subAdmin":
            console.log(`${name} is subAdmin, He has access to remove/add cources`)
            break;
        case "TestPrep":
            console.log(`${name} is TestPrep, He has access to create/delete content`)
            break;
        case "user":
            console.log(`${name} is user, He has access to consume content`)
            break;
        default:
            console.log("it's a trial user")
            break;
    }
}
GetUserRole("hio", "subAdmin");
GetUserRole("hio", "Admin");