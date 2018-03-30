

// TODO implement
console.log("start\n")
var SSH = require('simple-ssh');
var ssh = new SSH({
    host: 'ec2-54-91-69-153.compute-1.amazonaws.com',
    user: 'aarato',
    pass: '820Pawnee'
});
ssh.exec('sudo ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key', {
    pty: true,
    out: function(stdout) {
        console.log(stdout);
    }
}).start();
/*
ssh.exec('sudo ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key', {
    out: function(stdout) {
        console.log("exec\n")
        console.log(stdout);
        callback(null, "stdout");
    }
}).start();
*/
//callback2(null,"hi");
